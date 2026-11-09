"""Páginas estáticas para buscadores: una por lugar (lugares/<id>/), la página
«Todos los lugares» (lugares/), miniaturas, sitemap.xml y los bloques SEO de la portada.
Se ejecuta después de build2.py (que lo llama al final)."""
"""Genera las páginas para buscadores de «Descubrí Artigas» a partir de index.html:
  - lugares/<id>/index.html  (una página por lugar, con textos, fotos, mapa y datos para Google)
  - lugares/index.html       (todos los lugares, por zona)
  - lugares/th/<id>.jpg      (miniaturas; necesita Pillow: pip install pillow)
  - sitemap.xml
  - la lista de lugares del pie y los datos estructurados de index.html

Uso, desde la carpeta del repositorio:   python3 herramientas/generar_paginas.py
Hay que volver a ejecutarlo cada vez que se cambian textos, lugares o fotos en index.html.
"""
import json, os, re, sys, html, math
from datetime import date
from pathlib import Path
try:
    from PIL import Image, ImageOps
except ImportError:
    Image = None

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
SITE = str(ROOT) + "/"
U = "https://cei-javierdeviana.github.io/descubri-artigas/"
TODAY = date.today().isoformat()

def js_to_json(t):
    """Convierte el literal de JavaScript de PLACES (claves sin comillas) a JSON."""
    out, i, n, last = [], 0, len(t), ""
    while i < n:
        c = t[i]
        if c == '"':
            j = i + 1
            while t[j] != '"':
                j += 2 if t[j] == "\\" else 1
            out.append(t[i:j + 1]); last = '"'; i = j + 1; continue
        if c == "/" and t[i + 1] == "*":
            i = t.index("*/", i) + 2; continue
        if c == "/" and t[i + 1] == "/":
            i = t.index("\n", i); continue
        if c.isalpha() or c in "_$":
            j = i
            while j < n and (t[j].isalnum() or t[j] in "_$"): j += 1
            word, k = t[i:j], j
            while k < n and t[k] in " \t\r\n": k += 1
            out.append(f'"{word}"' if k < n and t[k] == ":" and last in "{," else word)
            last = "w"; i = j; continue
        if not c.isspace(): last = c
        out.append(c); i += 1
    return re.sub(r",(\s*[\]}])", r"\1", "".join(out))

_idx = open(SITE + "index.html", encoding="utf-8").read()
P = json.loads(js_to_json(re.search(r"const PLACES = (\[.*?\n\]);", _idx, re.S).group(1)))
PH = json.loads(re.search(r"const PHOTOS = (\{.*?\n\});", _idx, re.S).group(1))
BY = {p["id"]: p for p in P}

CATS = {"nat": "Naturaleza", "ame": "Amatistas y piedras", "his": "Historia y cultura", "rio": "Río y frontera"}
ZONES = [
    ("bella-union", "Bella Unión y la triple frontera", "Bella Unión",
     ["estacion-fluvial", "parque-rivera", "museo-santa-rosa", "isla-brasilera", "rincon-de-franquia"]),
    ("norte", "Baltasar Brum y el norte del Cuareim", None,
     ["baltasar-brum", "codo-del-cuareim", "cueva-del-indio"]),
    ("javier-de-viana", "Javier de Viana y el arroyo Tres Cruces", "Javier de Viana",
     ["puente-tres-cruces", "javier-de-viana", "capilla-santa-margarita", "cei-javier-de-viana", "destacamento-policial-12"]),
    ("ciudad", "Ciudad de Artigas", "Artigas",
     ["centro-artigas", "jefatura-de-policia", "museo-historico", "carnaval-de-artigas", "museo-piedra-preciosa", "paseo-7-de-setiembre"]),
    ("amatistas", "Piedra Pintada y la zona de las amatistas", None,
     ["piedra-pintada", "safari-minero", "los-catalanes"]),
]
ZONE_OF = {i: z for z in ZONES for i in z[3]}
LOCALITY = {i: z[2] for z in ZONES for i in z[3]}
LOCALITY["baltasar-brum"] = "Baltasar Brum"
assert sorted(ZONE_OF) == sorted(BY), set(BY) ^ set(ZONE_OF)

EXTRA_TYPE = {"museo-santa-rosa": "Museum", "javier-de-viana": "Museum", "museo-historico": "Museum",
              "museo-piedra-preciosa": "Museum", "parque-rivera": "Park", "paseo-7-de-setiembre": "Park",
              "piedra-pintada": "Park", "rincon-de-franquia": "Park", "capilla-santa-margarita": "Church",
              "centro-artigas": "Landmark"}

e = lambda s: html.escape(str(s), quote=True)

def dms(v, pos, neg):
    h = neg if v < 0 else pos; v = abs(v)
    d = math.floor(v); mf = (v - d) * 60; m = math.floor(mf); s = round((mf - m) * 60)
    if s == 60: s, m = 0, m + 1
    if m == 60: m, d = 0, d + 1
    return f"{d}°{m:02d}′{s:02d}″ {h}"

def coord(p): return f"{dms(p['lat'], 'N', 'S')} · {dms(p['lon'], 'E', 'O')}"

def title_for(p):
    loc = LOCALITY.get(p["id"])
    if loc and loc != "Artigas" and loc not in p["name"]:
        return f"{p['name']} · {loc}, Artigas | Descubrí Artigas"
    return f"{p['name']} · Artigas, Uruguay | Descubrí Artigas"

def desc_for(p):
    d = p["short"].strip()
    if len(d) < 120:
        d = d.rstrip(".") + ". " + p["where"].rstrip(".") + "."
    if len(d) > 165:
        d = d[:162].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return d

def ficha_of(i):
    for ext in ("jpg", "png", "jpeg"):
        if os.path.exists(f"{SITE}fichas/{i}.{ext}"): return True
    return False

def lic_html(ph):
    lic = "Dominio público" if ph.get("lic") == "Public domain" else ph.get("lic", "")
    if not lic: return ""
    return f' · <a href="{e(ph["licUrl"])}" rel="noopener">{e(lic)}</a>' if ph.get("licUrl") else f" · {e(lic)}"

def credit(ph):
    who = f'<a href="{e(ph["page"])}" rel="noopener">{e(ph["by"])}</a>' if ph.get("page") else e(ph.get("by", ""))
    ref = " · Foto de referencia" if ph.get("ref") else ""
    return f"Foto: {who}{lic_html(ph)}{ref}"

def gmaps_embed(p):
    z = p.get("zoom") or (13 if p.get("approx") else 16)
    t = "&t=h" if z <= 14 else ""
    return f"https://maps.google.com/maps?q={p['lat']}%2C{p['lon']}&z={z}{t}&hl=es&output=embed"

def obj_pos(ph):
    return f' style="object-position:{e(ph["pos"])}"' if ph.get("pos") else ""

FAV = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 22 26'%3E%3Cpath d='M11 0 21 8 17 26H5L1 8Z' "
       "fill='%237B45B6'/%3E%3Cpath d='M11 0 7 9l4 17 4-17Z' fill='%23fff' fill-opacity='.3'/%3E%3C/svg%3E")
GEM = ('<svg viewBox="0 0 22 26" aria-hidden="true"><path d="M11 0 21 8 17 26H5L1 8Z" fill="#B48BEA"/>'
       '<path d="M11 0 7 9l4 17 4-17Z" fill="#fff" fill-opacity=".3"/><path d="M1 8h20" stroke="#fff" stroke-opacity=".45"/></svg>')
PIN = ('<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/>'
       '<circle cx="12" cy="10" r="2.6"/></svg>')
CF = ("<script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' "
      "data-cf-beacon='{\"token\": \"3e86b5993cf8472e838f679430cf5d32\"}'></script>")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900'
         '&family=IBM+Plex+Mono:wght@400;500&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&display=swap">')
PUBLISHER = {"@type": "EducationalOrganization", "name": "CEI Javier de Viana",
             "address": {"@type": "PostalAddress", "addressLocality": "Javier de Viana", "addressRegion": "Artigas", "addressCountry": "UY"}}

def head(title, desc, canon, img, css, extra_ld):
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in extra_ld)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<link rel="icon" href="{FAV}">
<meta name="theme-color" content="#1E1529">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Descubrí Artigas">
<meta property="og:locale" content="es_UY">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(title.split(' | ')[0])}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
{FONTS}
<link rel="stylesheet" href="{css}">
{ld}
</head>
<body>"""

def topbar(home, hub):
    return f"""<header class="top"><div class="wrap top-in">
  <a class="brand" href="{home}">{GEM}<span>Descubrí Artigas</span></a>
  <nav aria-label="Secciones"><a href="{home}#explorar">Mapa</a><a href="{hub}">Lugares</a></nav>
</div></header>"""

FOOT = """<footer class="foot"><div class="wrap">
  <p class="foot-credit">{gem}<span>Un proyecto del <b>CEI Javier de Viana</b>, Artigas, Uruguay.</span></p>
  <dl class="foot-team">
    <div><dt>Idea original y acompañamiento docente</dt><dd>Docentes de la Coordinación de Centro del CEI Javier de Viana (maestras y profesores), año 2026</dd></div>
    <div><dt>Desarrollo, ejecución y creación</dt><dd>Niños y niñas de Educación Inicial y Primaria y estudiantes de Educación Secundaria del CEI Javier de Viana</dd></div>
    <div><dt>Diseño y desarrollo web</dt><dd>Prof. Pablo Montaña Conti</dd></div>
  </dl>
  <p>Horarios, tarifas y accesos pueden cambiar: confirmá antes de viajar. Cada lugar indica sus fuentes y el origen, autor y licencia de sus fotos.</p>
</div></footer>""".replace("{gem}", GEM)

# --- miniaturas --------------------------------------------------------------
os.makedirs(SITE + "lugares/th", exist_ok=True)
def thumb(i):
    ph = PH[i][0]; srcf = SITE + ph["src"]; out = f"{SITE}lugares/th/{i}.jpg"
    if Image is None:
        return
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(srcf):
        return
    im = Image.open(srcf).convert("RGB")
    cy = 0.5
    m = re.search(r"(\d+)%\s*$", ph.get("pos", ""))
    if m: cy = int(m.group(1)) / 100
    im = ImageOps.fit(im, (640, 420), Image.LANCZOS, centering=(0.5, cy))
    im.save(out, quality=78, optimize=True, progressive=True)
for p in P: thumb(p["id"])
def th(i, prefix):
    """Ruta de la miniatura (o de la foto de portada si no hay miniatura)."""
    return f"{prefix}th/{i}.jpg" if os.path.exists(f"{SITE}lugares/th/{i}.jpg") else f"{prefix}../{PH[i][0]['src']}"

# --- página de cada lugar ----------------------------------------------------
def place_page(idx, p):
    i = p["id"]; photos = PH.get(i, []); cover = photos[0] if photos else None
    z = ZONE_OF[i]; home = "../../"; hub = "../"
    canon = f"{U}lugares/{i}/"; img = U + cover["src"] if cover else U + "og-image.jpg"
    title, desc = title_for(p), desc_for(p)
    types = ["TouristAttraction"] + ([EXTRA_TYPE[i]] if i in EXTRA_TYPE else [])
    addr = {"@type": "PostalAddress", "addressRegion": "Artigas", "addressCountry": "UY"}
    if LOCALITY.get(i): addr["addressLocality"] = LOCALITY[i]
    ld_place = {"@context": "https://schema.org", "@type": types if len(types) > 1 else types[0], "name": p["name"],
                "description": p["short"], "url": canon, "image": [U + ph["src"] for ph in photos[:6]],
                "geo": {"@type": "GeoCoordinates", "latitude": p["lat"], "longitude": p["lon"]},
                "address": addr, "touristType": CATS[p["cat"]],
                "containedInPlace": {"@type": "AdministrativeArea", "name": "Departamento de Artigas, Uruguay"},
                "isPartOf": {"@type": "WebSite", "name": "Descubrí Artigas", "url": U}}
    ld_crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Descubrí Artigas", "item": U},
        {"@type": "ListItem", "position": 2, "name": "Lugares", "item": U + "lugares/"},
        {"@type": "ListItem", "position": 3, "name": p["name"], "item": canon}]}
    out = [head(title, desc, canon, img, "../estilo.css", [ld_place, ld_crumbs]), topbar(home, hub)]

    approx = (f'<p class="approx">{PIN}<span><b>Ubicación aproximada.</b> '
              f'{e(p.get("approxNote") or "El punto indica la zona; no es la ubicación exacta.")}</span></p>') if p.get("approx") else ""
    gm_view = f"https://www.google.com/maps/search/?api=1&query={p['lat']}%2C{p['lon']}"
    gm_dir = f"https://www.google.com/maps/dir/?api=1&destination={p['lat']}%2C{p['lon']}"
    ficha = f'<a class="btn btn-ghost" href="{home}#{i}/ficha">Ver la ficha</a>' if ficha_of(i) else ""
    out.append(f"""<main>
<section class="p-hero c-{p['cat']}"><div class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="{home}">Inicio</a><span>›</span><a href="{hub}">Lugares</a><span>›</span><a href="{hub}#{z[0]}">{e(z[1])}</a></nav>
  <p class="kicker"><i class="dot"></i>{e(CATS[p['cat']])} · Lugar {idx + 1:02d} de {len(P)}</p>
  <h1>{e(p['name'])}</h1>
  <p class="where">{e(p['where'])}</p>
  <p class="lead">{e(p['short'])}</p>
  <p class="coords">{coord(p)}{' · ubicación aproximada' if p.get('approx') else ''}</p>
  <p class="actions"><a class="btn" href="{home}#{i}">Verlo en el mapa interactivo</a><a class="btn btn-ghost" href="{gm_view}" rel="noopener">{PIN}Google Maps</a>{ficha}</p>
</div></section>""")
    if cover:
        out.append(f'<div class="wrap"><figure class="cover"><img src="{home}{e(cover["src"])}" alt="{e(cover["alt"])}"{obj_pos(cover)} width="1600" height="1000" fetchpriority="high"><figcaption>{e(cover["alt"])} · {credit(cover)}</figcaption></figure></div>')

    body = []
    for b in p["body"]:
        body.append(f"<h2>{e(b['h'])}</h2>")
        for para in b.get("p", []): body.append(f"<p>{e(para)}</p>")
        if b.get("list"): body.append("<ul>" + "".join(f"<li>{e(li)}</li>" for li in b["list"]) + "</ul>")
    if p.get("curious"):
        body.append(f'<aside class="curious"><h2>¿Sabías que…?</h2><p>{e(p["curious"])}</p></aside>')
    vids = p.get("videos") or []
    if vids:
        cards = []
        for v in vids:
            url = f"https://www.youtube.com/{'shorts/' if v.get('vertical') else 'watch?v='}{e(v['yt'])}"
            cards.append(f'<li><a href="{url}" rel="noopener"><img src="https://i.ytimg.com/vi/{e(v["yt"])}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">'
                         f'<span>▶ {e(v.get("title") or p["name"])}{" · " + e(v["by"]) if v.get("by") else ""}</span></a></li>')
        body.append(f'<section class="vids"><h2>Videos</h2><ul>{"".join(cards)}</ul></section>')
    if len(photos) > 1:
        figs = "".join(f'<figure><img src="{home}{e(ph["src"])}" alt="{e(ph["alt"])}"{obj_pos(ph)} loading="lazy" width="800" height="600">'
                       f'<figcaption><b>{e(ph["alt"])}</b><br>{credit(ph)}</figcaption></figure>' for ph in photos[1:])
        body.append(f'<section class="gal"><h2>Fotos</h2><div class="gal-grid">{figs}</div></section>')

    facts = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in p["facts"])
    srcs = "".join(f'<li><a href="{e(u)}" rel="noopener">{e(t)}</a></li>' for t, u in p["sources"])
    side = f"""<aside class="side">
  <section class="box"><h2>Datos útiles</h2><dl class="facts">{facts}</dl></section>
  <section class="box"><h2>Cómo llegar</h2>{approx}
    <iframe class="gmap" src="{gmaps_embed(p)}" title="Mapa de Google Maps: {e(p['name'])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    <p>{e(p['howto'])}</p>
    <p><a class="btn btn-quiet" href="{gm_dir}" rel="noopener">{PIN}Cómo llegar con Google Maps</a></p>
  </section>
  <section class="box"><h2>Fuentes</h2><ul class="srcs">{srcs}</ul></section>
</aside>"""
    out.append(f'<div class="wrap grid"><article class="txt">{"".join(body)}</article>{side}</div>')

    # navegación
    prev_p, next_p = P[idx - 1] if idx > 0 else None, P[idx + 1] if idx + 1 < len(P) else None
    pn = '<nav class="pn wrap" aria-label="Otros lugares">'
    pn += f'<a class="pn-prev" href="../{prev_p["id"]}/"><small>← Anterior</small>{e(prev_p["name"])}</a>' if prev_p else "<span></span>"
    pn += f'<a class="pn-next" href="../{next_p["id"]}/"><small>Siguiente →</small>{e(next_p["name"])}</a>' if next_p else "<span></span>"
    pn += "</nav>"
    same = [BY[j] for j in z[3] if j != i]
    near = "".join(f'<li><a href="../{q["id"]}/"><img src="{th(q["id"], "../")}" alt="" loading="lazy" width="640" height="420"><span>{e(q["name"])}</span></a></li>' for q in same)
    out.append(pn + f'<section class="near wrap"><h2>Más lugares en {e(z[1])}</h2><ul class="cards">{near}</ul>'
               f'<p class="all"><a class="btn btn-quiet" href="{hub}">Ver los {len(P)} lugares</a></p></section></main>')
    out.append(FOOT + "\n" + CF + "\n</body>\n</html>\n")
    os.makedirs(f"{SITE}lugares/{i}", exist_ok=True)
    open(f"{SITE}lugares/{i}/index.html", "w", encoding="utf-8").write("\n".join(out))

for k, p in enumerate(P): place_page(k, p)

# --- página «Todos los lugares» ---------------------------------------------
hub_title = "Lugares para visitar en Artigas, Uruguay | Descubrí Artigas"
hub_desc = ("Los 22 lugares de Descubrí Artigas, de Bella Unión a las minas de amatistas: museos, ríos, la triple frontera, "
            "viejas estaciones de tren, Piedra Pintada y el carnaval.")
ld_list = {"@context": "https://schema.org", "@type": "ItemList", "name": "Lugares para visitar en Artigas, Uruguay",
           "numberOfItems": len(P), "itemListElement": [
               {"@type": "ListItem", "position": k + 1, "url": f"{U}lugares/{p['id']}/", "name": p["name"]} for k, p in enumerate(P)]}
hub = [head(hub_title, hub_desc, U + "lugares/", U + "og-image.jpg", "estilo.css", [ld_list]), topbar("../", "./")]
hub.append(f"""<main>
<section class="p-hero hub"><div class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="../">Inicio</a><span>›</span><span>Lugares</span></nav>
  <p class="kicker">Departamento de Artigas · Uruguay</p>
  <h1>{len(P)} lugares para descubrir</h1>
  <p class="lead">Del río Uruguay a las minas de amatistas: museos, ríos, viejas estaciones de tren, la triple frontera y el carnaval. Cada lugar tiene su historia, sus fotos, sus datos útiles y cómo llegar.</p>
  <p class="actions"><a class="btn" href="../#explorar">Ver todos en el mapa interactivo</a></p>
  <nav class="zones" aria-label="Zonas">{''.join(f'<a href="#{z[0]}">{e(z[1])}</a>' for z in ZONES)}</nav>
</div></section>""")
n = 0
for z in ZONES:
    cards = []
    for j in z[3]:
        q = BY[j]; n = P.index(q) + 1
        cards.append(f'<li class="c-{q["cat"]}"><a href="{j}/"><img src="{th(j, "")}" alt="{e(PH[j][0]["alt"])}" loading="lazy" width="640" height="420">'
                     f'<span class="n">{n:02d}</span><b>{e(q["name"])}</b><small>{e(q["where"])}</small><p>{e(q["short"])}</p></a></li>')
    hub.append(f'<section class="zone wrap" id="{z[0]}"><h2>{e(z[1])}</h2><ul class="cards big">{"".join(cards)}</ul></section>')
hub.append("</main>\n" + FOOT + "\n" + CF + "\n</body>\n</html>\n")
open(SITE + "lugares/index.html", "w", encoding="utf-8").write("\n".join(hub))


# --- sitemap -----------------------------------------------------------------
def url_block(loc, imgs, prio):
    im = "".join(f"\n    <image:image><image:loc>{U}{s}</image:loc></image:image>" for s in imgs)
    return f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{prio}</priority>{im}\n  </url>"
blocks = [url_block(U, ["og-image.jpg"], "1.0"), url_block(U + "lugares/", [], "0.9")]
blocks += [url_block(f"{U}lugares/{p['id']}/", [ph["src"] for ph in PH.get(p["id"], [])], "0.8") for p in P]
open(SITE + "sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(blocks) + "\n</urlset>\n")

# --- bloques de la portada (lista de lugares del pie y datos estructurados) ---
def home_blocks(base):
    links = "".join(f'<li><a href="{base}lugares/{p["id"]}/">{e(p["name"])}</a></li>' for p in P)
    nav = (f'<nav class="foot-places" aria-label="Todos los lugares"><h2><a href="{base}lugares/">Los {len(P)} lugares</a></h2>'
           f'<ul>{links}</ul></nav>')
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "Descubrí Artigas", "url": U, "inLanguage": "es-UY",
           "description": "Guía y mapa interactivo de lugares para visitar en el departamento de Artigas, Uruguay.",
           "publisher": PUBLISHER}, ld_list]
    ldh = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return nav, ldh

def put_home_blocks(fname, base):
    s = open(fname, encoding="utf-8").read()
    nav, ldh = home_blocks(base)
    for tag, val in (("SEO_LINKS", nav), ("SEO_JSONLD", ldh)):
        s, k = re.subn(rf"<!--{tag}-->.*?<!--/{tag}-->", lambda m: f"<!--{tag}-->{val}<!--/{tag}-->", s, flags=re.S)
        assert k == 1, (fname, tag)
    open(fname, "w", encoding="utf-8").write(s)

put_home_blocks(SITE + "index.html", "")
print(f"Listo: {len(P)} páginas de lugares, la página de todos los lugares y sitemap.xml" + ("" if Image else " (sin miniaturas: falta Pillow)"))
