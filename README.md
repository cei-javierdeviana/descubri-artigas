# Descubrí Artigas

Un proyecto del **CEI Javier de Viana** (Artigas, Uruguay).

- **Idea original y acompañamiento docente:** Docentes de la Coordinación de Centro del CEI Javier de Viana (maestras y profesores), año 2026
- **Desarrollo, ejecución y creación:** Niños y niñas de Educación Inicial y Primaria y estudiantes de Educación Secundaria del CEI Javier de Viana
- **Diseño y desarrollo web:** Prof. Pablo Montaña

Dirección de la web: **https://cei-javierdeviana.github.io/descubri-artigas/**

Guía web con veinte lugares para conocer en el departamento de Artigas (Uruguay): un mapa interactivo, una postal por lugar y una ficha completa con fotos, datos útiles y fuentes.

Es un sitio estático: no necesita servidor ni instalación. Todo está en `index.html`, las fotos en la carpeta `img/` y las fichas de cada lugar en la carpeta `fichas/`.

## Contenido de la carpeta

| Archivo | Qué es |
|---|---|
| `index.html` | La página completa (textos, mapa, estilos y código) |
| `img/` | Las fotos de cada lugar (portadas, tarjetas y galerías) |
| `fichas/` | Las fichas (láminas) que elaboran los docentes, una por lugar |
| `.nojekyll` | Le indica a GitHub Pages que publique los archivos tal cual |

## Publicarla en GitHub Pages (organización del CEI)

La web se publica en una **organización** de GitHub llamada `cei-javierdeviana`. La organización se crea desde una cuenta personal de GitHub: no hace falta otro usuario ni otra contraseña.

### 1. Crear la organización

1. En GitHub, tocá tu foto de perfil (arriba a la derecha) → **Settings**.
2. En la barra lateral, sección *Access*, entrá a **Organizations** → **New organization**.
3. Elegí el plan **Free**.
4. Nombre: `cei-javierdeviana`. Como correo de contacto conviene usar uno del CEI.

### 2. Crear el repositorio y subir los archivos

1. En la organización, tocá **New repository**. Revisá que el dueño (*Owner*) sea `cei-javierdeviana`.
2. Nombre: `descubri-artigas`. Visibilidad: **Public**. No agregues README.
3. En el repositorio vacío, entrá al enlace **uploading an existing file**.
4. Arrastrá **el contenido** de esta carpeta (el `index.html`, las carpetas `img` y `fichas` y el `README.md`), no la carpeta entera. GitHub acepta hasta 100 archivos por vez y esta carpeta tiene 115.
5. Tocá **Commit changes**.

### 3. Activar la página

1. En el repositorio: **Settings** → **Pages**.
2. En *Build and deployment*, elegí **Deploy from a branch**, rama **main** y carpeta **/ (root)**. Tocá **Save**.
3. En uno o dos minutos la web queda en `https://cei-javierdeviana.github.io/descubri-artigas/`.

> El archivo `.nojekyll` empieza con punto y en macOS queda oculto. Si no se sube, la página funciona igual.

## Agregar fotos propias

1. Copiá la foto a `img/` con un nombre sin espacios ni tildes, por ejemplo `piedra-pintada-3.jpg`. Conviene que sea horizontal y de unos 1280 px de ancho.
2. Abrí `index.html`, buscá `const PHOTOS` y agregá una línea en el lugar que corresponda:

```js
{"src": "img/piedra-pintada-3.jpg", "alt": "Qué muestra la foto", "by": "Nombre de quien la sacó", "lic": "Todos los derechos reservados", "page": ""},
```

3. La **primera** foto de cada lugar es la portada del mapa, la postal y la ficha. Para cambiar la portada, mové la línea al primer lugar.
4. Si una foto muestra el entorno o el tema y no el lugar exacto, agregá `"ref": true` y la página la marca como «Foto de referencia».

## Agregar la ficha de un lugar

Cada lugar puede tener una ficha: una lámina informativa hecha por docentes. Cuando un lugar tiene ficha, su página muestra el botón **Ver ficha**. Si no la tiene, el botón no aparece y la página se ve igual que siempre.

1. Guardá la ficha como imagen **JPG** (también sirve PNG), en formato vertical. Con unos 1000 a 1500 px de ancho se lee bien.
2. Ponele exactamente el nombre del lugar que figura en la tabla de abajo, por ejemplo `piedra-pintada.jpg`: en minúsculas, sin tildes ni espacios.
3. Copiala en la carpeta `fichas/`.
4. En GitHub Desktop: escribí un resumen (por ejemplo «Agrego ficha de Piedra Pintada»), tocá **Commit to main** y después **Push origin**.

No hay que tocar `index.html`: la página encuentra la ficha sola por su nombre. Para reemplazar una ficha, guardá la nueva con el mismo nombre encima de la anterior.

| Lugar | Nombre del archivo |
|---|---|
| Estación Fluvial de Bella Unión | `estacion-fluvial.jpg` |
| Parque Rivera | `parque-rivera.jpg` |
| Museo Santa Rosa del Cuareim | `museo-santa-rosa.jpg` |
| Isla Brasilera y la triple frontera | `isla-brasilera.jpg` |
| Rincón de Franquía | `rincon-de-franquia.jpg` |
| Estación de Baltasar Brum | `baltasar-brum.jpg` |
| Codo del Cuareim | `codo-del-cuareim.jpg` |
| Cueva del Indio | `cueva-del-indio.jpg` |
| CEI Javier de Viana | `cei-javier-de-viana.jpg` |
| Destacamento Policial N.º 12 | `destacamento-policial-12.jpg` |
| Capilla Santa Margarita | `capilla-santa-margarita.jpg` |
| Museo Ferroviario «Bibiano Gómez» (Javier de Viana) | `javier-de-viana.jpg` |
| Plaza Artigas e Iglesia San Eugenio | `centro-artigas.jpg` |
| Jefatura de Policía de Artigas | `jefatura-de-policia.jpg` |
| Museo Histórico Departamental | `museo-historico.jpg` |
| Carnaval de Artigas | `carnaval-de-artigas.jpg` |
| Museo de la Piedra Preciosa | `museo-piedra-preciosa.jpg` |
| Paseo 7 de Setiembre y Puente de la Concordia | `paseo-7-de-setiembre.jpg` |
| Piedra Pintada | `piedra-pintada.jpg` |
| Minas de amatistas de Los Catalanes | `los-catalanes.jpg` |

## Videos

Un lugar puede mostrar videos de YouTube en su página, en la sección **Video**, entre el texto y la galería. Primero se ve la miniatura y el video recién carga cuando alguien lo toca, así la página no se pone lenta.

También funcionan los Shorts (videos verticales): se muestran en formato vertical.

Para sumar un video, subilo a YouTube (por ejemplo, al canal del CEI) como público o no listado, y pasá el enlace a quien mantiene la web.

| Lugar | Video |
|---|---|
| Rincón de Franquía | [«Rincón de Franquía»](https://www.youtube.com/watch?v=Ao5kOan3eeQ), canal CEI Javier de Viana |
| CEI Javier de Viana | [«Estudiantes de Ed. Primaria en clase de Ed. Física»](https://www.youtube.com/watch?v=gfcR1DPMEkc), canal CEI Javier de Viana |
| CEI Javier de Viana | [«Niños de Ed. Inicial disfrutando del recreo»](https://www.youtube.com/shorts/DhRsoy7eizA) (Short, vertical), canal CEI Javier de Viana |

## Sumar a otras personas del CEI

Para que la web no dependa de una sola persona, sumá al menos a otra persona del CEI como dueña de la organización:

1. En la organización: **People** → **Invite member**.
2. Escribí su usuario o correo de GitHub y elegí el rol **Owner**.
3. La persona acepta la invitación desde su correo.

Quien vaya a editar la web necesita su propia cuenta de GitHub. Para verla no hace falta ninguna cuenta. Aunque cambien los dueños, la dirección de la web se mantiene.

Si más adelante el CEI quiere una web propia en la dirección principal `https://cei-javierdeviana.github.io/`, se crea otro repositorio en la organización llamado `cei-javierdeviana.github.io`. Esta guía sigue funcionando en `/descubri-artigas/`.

## Créditos de las fotos

La mayoría de las fotos vienen de [Wikimedia Commons](https://commons.wikimedia.org) y tienen licencias libres. Las licencias CC BY y CC BY-SA piden citar al autor y la licencia: por eso cada ficha muestra estos datos y no hay que borrarlos. Las fotos del Museo Histórico Departamental salen de una lámina informativa aportada por docentes del CEI. Las del CEI Javier de Viana son de la propia institución; se mejoraron el brillo, el contraste y la nitidez, y se redujeron de tamaño para la web. Las de la Cueva del Indio son capturas del capítulo 6 del documental «La Huella de Sepé» (Identidad Antídoto y TNU, 2011), tomadas por estudiantes y mejoradas con inteligencia artificial para la web. Las del Museo Ferroviario «Bibiano Gómez» son del CEI Javier de Viana y de Víctor Hernández; en la de portada se borraron con inteligencia artificial dos personas (ninguna es Bibiano Gómez) y su sombra. Las fotos se redujeron o ampliaron de tamaño para la web.

**Estación Fluvial de Bella Unión**

- `img/estacion-fluvial-1.jpg` — El río Uruguay frente a Bella Unión, con Monte Caseros (Argentina) en la otra orilla. Foto: [Mx. Granger](https://commons.wikimedia.org/wiki/File:Monte_Caseros_seen_from_Uruguay.jpg), CC0. *(foto de referencia)*
- `img/estacion-fluvial-2.jpg` — Plaza 25 de Agosto, en el centro de Bella Unión. Foto: [Mx. Granger](https://commons.wikimedia.org/wiki/File:Plaza_25_de_Agosto%2C_Bella_Uni%C3%B3n_1.jpg), CC0.
- `img/estacion-fluvial-3.jpg` — Edificio del Municipio de Bella Unión. Foto: [Ulises Icardi](https://commons.wikimedia.org/wiki/File:Edificio_de_la_Municipalidad_de_Bella_Uni%C3%B3n.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

**Parque Rivera**

- `img/parque-rivera-1.jpg` — Un quiosco del Parque Rivera frente al río Uruguay. Foto: [Mx. Granger](https://commons.wikimedia.org/wiki/File:Parque_Rivera%2C_Bella_Uni%C3%B3n_2.jpg), CC0.
- `img/parque-rivera-2.jpg` — La calle costera del Parque Rivera. Foto: [Mx. Granger](https://commons.wikimedia.org/wiki/File:Parque_Rivera%2C_Bella_Uni%C3%B3n_1.jpg), CC0.
- `img/parque-rivera-3.jpg` — Atardecer en el Parque Rivera. Foto: [Artigas12](https://commons.wikimedia.org/wiki/File:Parque_rivera301.jpg), CC0.
- `img/parque-rivera-4.jpg` — Quinchos del Balneario Los Pinos. Foto: [Artigas12](https://commons.wikimedia.org/wiki/File:Los_pinos_bu201.jpg), CC0.
- `img/parque-rivera-5.jpg` — Embarcaciones en el río Uruguay, en Bella Unión. Foto: [Vince Alongi](https://commons.wikimedia.org/wiki/File:Riouruguay.jpg), [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).

**Museo Santa Rosa del Cuareim**

- `img/museo-santa-rosa-1.jpg` — Entrada del Museo Santa Rosa del Cuareim. Foto: [Mx. Granger](https://commons.wikimedia.org/wiki/File:Museo_Privado_Santa_Rosa_del_Cuareim.jpg), CC0.

**Isla Brasilera y la triple frontera**

- `img/isla-brasilera-1.jpg` — La Isla Brasilera y la costa argentina, vistas desde el mirador de Rincón de Franquía. Foto: [Gmmv1980](https://commons.wikimedia.org/wiki/File:Vista_desde_el_mangrullo_de_la_triple_frontera%2C_en_Rinc%C3%B3n_de_Franqu%C3%ADa%2C_Bella_Uni%C3%B3n%2C_departamento_de_Artigas%2C_Uruguay.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/isla-brasilera-2.jpg` — El río Uruguay desde Rincón de Franquía; al fondo, la Isla Brasilera. Foto: [Gmmv1980](https://commons.wikimedia.org/wiki/File:R%C3%ADo_Uruguay%2C_desde_Rinc%C3%B3n_de_Franqu%C3%ADa.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/isla-brasilera-3.jpg` — La isla vista desde un satélite, en la unión de los ríos Cuareim y Uruguay. Foto: [NASA](https://commons.wikimedia.org/wiki/File:Isla_Brasilera_57.62646W_30.18248S.jpg), Dominio público.
- `img/isla-brasilera-4.jpg` — Monolito que recuerda el punto donde se unen los tres países, en la isla. Foto: [Pedroborches](https://commons.wikimedia.org/wiki/File:Monolito_en_referencia_al_punto_tripartito.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/isla-brasilera-5.jpg` — La triple frontera desde la costa uruguaya. Foto: [MEL LAPAZ](https://commons.wikimedia.org/wiki/File:Triple_frontera.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

**Rincón de Franquía**

- `img/rincon-de-franquia-1.jpg` — Atardecer en Rincón de Franquía. Foto: [Giannina Pradella](https://commons.wikimedia.org/wiki/File:ATARDECER_EN_RINCON_DE_FRANQUIA.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/rincon-de-franquia-2.jpg` — Paisaje del área protegida. Foto: [Siliaia3](https://commons.wikimedia.org/wiki/File:Paisaje_de_Rinc%C3%B3n_de_franqu%C3%ADa.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/rincon-de-franquia-3.jpg` — Chajás en los humedales del área protegida. Foto: [SebasFN](https://commons.wikimedia.org/wiki/File:Chaj%C3%A1_1.png), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/rincon-de-franquia-4.jpg` — Espátula rosada en Rincón de Franquía. Foto: [SebasFN](https://commons.wikimedia.org/wiki/File:Esp%C3%A1tula_Rosada_1.png), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/rincon-de-franquia-5.jpg` — Jacana entre la vegetación del humedal. Foto: [SebasFN](https://commons.wikimedia.org/wiki/File:Jacana_1.png), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/rincon-de-franquia-6.jpg` — Lechucita posada en Rincón de Franquía. Foto: [Giannina Pradella](https://commons.wikimedia.org/wiki/File:RINCON_DE_FRANQUIA.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/rincon-de-franquia-7.jpg` — El mangrullo, mirador sobre la triple frontera. Foto: [Gmmv1980](https://commons.wikimedia.org/wiki/File:Mangrullo_de_la_triple_frontera_en_Rinc%C3%B3n_de_Franqu%C3%ADa%2C_Bella_Uni%C3%B3n%2C_Artigas%2C_Uruguay.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/rincon-de-franquia-8.jpg` — El monte de Rincón de Franquía. Foto: [Siliaia3](https://commons.wikimedia.org/wiki/File:Entrando_en_el_Bosque_-_Rinc%C3%B3n_de_Franqu%C3%ADa.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

**Estación de Baltasar Brum**

- `img/baltasar-brum-1.jpg` — La antigua estación de trenes de Baltasar Brum. Foto: [Raul Zapata](https://commons.wikimedia.org/wiki/File:BALTASAR_BRUM_01.JPG), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/baltasar-brum-2.jpg` — Monumento a la esquila de ovinos, en Baltasar Brum. Foto: [Raul Zapata](https://commons.wikimedia.org/wiki/File:BALTASAR_BRUM_02.JPG), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

**Codo del Cuareim**

- `img/codo-del-cuareim-1.jpg` — El río Cuareim en el departamento de Artigas. Foto: [Wilson S. Serra, Alejandro Duarte, Edward D. Burress y Marcelo Loureiro](https://commons.wikimedia.org/wiki/File:Cuareim_River_%2818221%29.png), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). *(foto de referencia)*
- `img/codo-del-cuareim-2.jpg` — El río Cuareim con vista hacia Brasil, en Bella Unión. Foto: [Montecruz Foto](https://commons.wikimedia.org/wiki/File:Cuareim.jpg), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/). *(foto de referencia)*
- `img/codo-del-cuareim-3.jpg` — El río Cuareim en una fotografía de 1888. Foto: [Lorenzo Spátola (Biblioteca Nacional de Uruguay)](https://commons.wikimedia.org/wiki/File:ABN_10881.jpg), Dominio público. *(foto de referencia)*

**Cueva del Indio**

- `img/cueva-del-indio-1.jpg` — La Cueva del Indio, un gran amontonamiento de piedras en medio del monte. Foto: Captura del documental [«La Huella de Sepé», cap. 6](https://www.youtube.com/playlist?list=PLuuHImgA8d0_C9KC72ZmXfp8_vbRcbxFM) (Identidad Antídoto y TNU, 2011).
- `img/cueva-del-indio-2.jpg` — Un jinete entre los Talas del Sacrificio, a orillas del río Cuareim. Foto: Captura del documental [«La Huella de Sepé», cap. 6](https://www.youtube.com/playlist?list=PLuuHImgA8d0_C9KC72ZmXfp8_vbRcbxFM) (Identidad Antídoto y TNU, 2011).
- `img/cueva-del-indio-3.jpg` — El Árbol de los Sacrificios. Foto: Captura del documental [«La Huella de Sepé», cap. 6](https://www.youtube.com/playlist?list=PLuuHImgA8d0_C9KC72ZmXfp8_vbRcbxFM) (Identidad Antídoto y TNU, 2011).
- `img/cueva-del-indio-4.jpg` — Un mapa del departamento con la ubicación de la Cueva del Indio marcada en rojo. Foto: Captura del documental [«La Huella de Sepé», cap. 6](https://www.youtube.com/playlist?list=PLuuHImgA8d0_C9KC72ZmXfp8_vbRcbxFM) (Identidad Antídoto y TNU, 2011).

**CEI Javier de Viana**

- `img/cei-javier-de-viana-1.jpg` — Estudiantes, docentes y funcionarios frente al edificio del CEI. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-2.jpg` — Estudiantes del liceo en el caminito pintado de la entrada. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-3.jpg` — Un acto criollo visto desde el aire: la ronda, los jinetes y la bandera en el pasto. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-4.jpg` — Niñas, niños, estudiantes, docentes y familias vestidos de criollo, junto a la bandera. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-5.jpg` — Una cabalgata con banderas por la ruta. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-6.jpg` — La comunidad del CEI, vestida de criollo, en una calle de tierra. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-7.jpg` — La comunidad del CEI en la foto del saludo por el Día del Trabajador. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-8.jpg` — Estudiantes del liceo en la biblioteca. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-9.jpg` — Lectura en grupo en la biblioteca. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-10.jpg` — Niñas y niños de la escuela y estudiantes del liceo, con docentes y funcionarios. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-11.jpg` — Docentes y funcionarios del CEI, con una muestra por el Año Internacional de la Mujer Agrícola. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-12.jpg` — «Desde nuestra institución, hacemos viral lo que suma»: el lema del CEI. Foto: CEI Javier de Viana.
- `img/cei-javier-de-viana-13.jpg` — La huerta del CEI, su proyecto productivo. Foto: Lámina informativa del CEI Javier de Viana.

**Destacamento Policial N.º 12**

- `img/destacamento-policial-12-1.jpg` — El frente del destacamento, con su viejo cartel «Policía». Foto: CEI Javier de Viana.
- `img/destacamento-policial-12-2.jpg` — El acta inaugural de la Seccional Policial 12.ª, del 10 de mayo de 1973. Foto: CEI Javier de Viana.
- `img/destacamento-policial-12-3.jpg` — El mapa de referencias de la Seccional 12, con su zona entre el arroyo Tres Cruces y el río Cuareim. Foto: CEI Javier de Viana.

**Capilla Santa Margarita**

- `img/capilla-santa-margarita-1.jpg` — La fachada blanca de la capilla, con su campanario y sus cruces. Foto: CEI Javier de Viana.
- `img/capilla-santa-margarita-2.jpg` — Foto histórica de la inauguración de la capilla, el 28 de febrero de 1928. Foto histórica, fotografiada por el CEI Javier de Viana.
- `img/capilla-santa-margarita-3.jpg` — Carteles de las peregrinaciones en el predio de la capilla. Foto: CEI Javier de Viana.

**Museo Ferroviario «Bibiano Gómez» (Javier de Viana)**

- `img/javier-de-viana-1.jpg` — El cartel del museo y el mural del tren en la pared de la estación. Foto: CEI Javier de Viana.
- `img/javier-de-viana-17.jpg` — El viejo cartel de la estación: «Javier de Viana. Distancia de Central K 780.287». Foto: CEI Javier de Viana (mejorada con inteligencia artificial).
- `img/javier-de-viana-2.jpg` — Una de las salas del museo, con paneles, una vitrina y objetos ferroviarios. Foto: CEI Javier de Viana.
- `img/javier-de-viana-3.jpg` — El cartel del Museo Ferroviario «Bibiano Gómez». Foto: CEI Javier de Viana.
- `img/javier-de-viana-4.jpg` — El andén de la vieja estación, con valijas antiguas. Foto: CEI Javier de Viana.
- `img/javier-de-viana-5.jpg` — Niñas, niños, estudiantes y docentes vestidos de época bajo el cartel «Tres Cruces». Foto: CEI Javier de Viana.
- `img/javier-de-viana-6.jpg` — La comunidad vestida de época junto al cartel de la estación. Foto: CEI Javier de Viana.
- `img/javier-de-viana-7.jpg` — Niños vestidos de ferroviarios en el andén. Foto: CEI Javier de Viana.
- `img/javier-de-viana-8.jpg` — Niñas vestidas de época con valijas antiguas en el andén. Foto: CEI Javier de Viana.
- `img/javier-de-viana-9.jpg` — Un niño vestido de jefe de estación, en una sala del museo. Foto: CEI Javier de Viana.
- `img/javier-de-viana-10.jpg` — Niñas vestidas de época en la estación. Foto: CEI Javier de Viana.
- `img/javier-de-viana-11.jpg` — Una niña vestida de época, con abanico. Foto: CEI Javier de Viana.
- `img/javier-de-viana-12.jpg` — Un adulto y dos niños vestidos de ferroviarios junto al cartel «Tres Cruces». Foto: Víctor Hernández.
- `img/javier-de-viana-13.jpg` — Un vagón pintado para sacarse fotos: «Museo Ferroviario Bibiano Gómez». Foto: Víctor Hernández.
- `img/javier-de-viana-14.jpg` — Antigua estación de Cuareim, otra estación del ferrocarril en el departamento. Foto: [Ulises Icardi](https://commons.wikimedia.org/wiki/File:Antigua_estaci%C3%B3n_ferroviaria_de_Cuareim.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). *(foto de referencia)*
- `img/javier-de-viana-15.jpg` — Locomotora a vapor exhibida en la ciudad de Artigas. Foto: [Gerardo c](https://commons.wikimedia.org/wiki/File:Locomotrora_artigas.jpg), Dominio público. *(foto de referencia)*
- `img/javier-de-viana-16.jpg` — La estación de San Eugenio (hoy ciudad de Artigas) hacia 1890. Foto: [John Fitz Patrick](https://commons.wikimedia.org/wiki/File:Uruguay_Northern_Railway_San_Eugenio_station.jpg), CC0. *(foto de referencia)*

**Plaza Artigas e Iglesia San Eugenio**

- `img/centro-artigas-1.jpg` — Fachada de la Iglesia San Eugenio del Cuareim. Foto: [Amurru](https://commons.wikimedia.org/wiki/File:Parroquia_San_Eugenio_del_Cuareim.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/centro-artigas-2.jpg` — La Iglesia San Eugenio, Monumento Histórico Nacional. Foto: [Raul Zapata](https://commons.wikimedia.org/wiki/File:ARTIGAS_03_PATRIMONIO_NACIONAL.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/centro-artigas-3.jpg` — El Ibirapitá frente a la Terminal de Ómnibus. Foto: [Maywiki](https://commons.wikimedia.org/wiki/File:Ibirapit%C3%A1_de_Artigas.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/centro-artigas-4.jpg` — Obelisco a la Gloria de los Héroes de 1825, en la Plaza Batlle. Foto: [Derys Benitez](https://commons.wikimedia.org/wiki/File:Obelisco_a_la_Gloria_de_los_H%C3%A9roes.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/centro-artigas-5.jpg` — Fachada del ex Mercado Municipal. Foto: [Amurru](https://commons.wikimedia.org/wiki/File:Mercado_Municipal_de_Artigas.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/javier-de-viana-16.jpg` — La antigua estación de tren hacia 1890, donde hoy está la Terminal. Foto: [John Fitz Patrick](https://commons.wikimedia.org/wiki/File:Uruguay_Northern_Railway_San_Eugenio_station.jpg), CC0.

**Jefatura de Policía de Artigas**

- `img/jefatura-de-policia-1.jpg` — Fachada sobre la avenida Carlos Lecueder. Foto: [Alejandro Gil Álvarez](https://commons.wikimedia.org/wiki/File:Jefatura_de_Polic%C3%ADa_%28Lecueder%29.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/jefatura-de-policia-2.jpg` — El edificio y sus torres almenadas. Foto: [Nicolas Barriola](https://commons.wikimedia.org/wiki/File:Jefatura_de_Polic%C3%ADa_1.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/jefatura-de-policia-3.jpg` — El reloj y una de las torres almenadas. Foto: [Alejandro Gil Álvarez](https://commons.wikimedia.org/wiki/File:Jefatura_de_Polic%C3%ADa_%28torre_y_reloj%29.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/jefatura-de-policia-4.jpg` — El patio, rodeado de arcos de medio punto. Foto: [Alejandro Gil Álvarez](https://commons.wikimedia.org/wiki/File:Jefatura_de_Polic%C3%ADa_%28patio_y_torre%29.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/jefatura-de-policia-5.jpg` — El patio visto a través de un arco. Foto: [Alejandro Gil Álvarez](https://commons.wikimedia.org/wiki/File:Jefatura_de_Polic%C3%ADa_%28Patio%29.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/jefatura-de-policia-6.jpg` — Una de las torres almenadas. Foto: [Alejandro Gil Álvarez](https://commons.wikimedia.org/wiki/File:Torre_Jefatura_de_Polic%C3%ADa.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/jefatura-de-policia-7.jpg` — La Jefatura Política de San Eugenio en 1907. Foto: [Dornaleche y Reyes Impresores](https://commons.wikimedia.org/wiki/File:Jefatura_Pol%C3%ADtica_de_San_Eugenio_-_Artigas.tif), Dominio público.

**Museo Histórico Departamental**

- `img/museo-historico-1.jpg` — Fachada del Museo Histórico Departamental. Foto: Lámina informativa del museo.
- `img/museo-historico-2.jpg` — Una de las salas del museo. Foto: Lámina informativa del museo.
- `img/museo-historico-3.jpg` — Fósiles de megafauna: Glossotherium y Toxodon. Foto: Lámina informativa del museo.
- `img/museo-historico-4.jpg` — Una maqueta con soldados a caballo, en una de las salas. Foto: Lámina informativa del museo.

**Carnaval de Artigas**

- `img/carnaval-de-artigas-1.jpg` — Carros alegóricos y bailarines en el desfile de 2007. Foto: [Da dinges](https://commons.wikimedia.org/wiki/File:Carnaval_de_Artigas.jpg), Dominio público.
- `img/carnaval-de-artigas-2.jpg` — Una bailarina con su fantasía de plumas. Foto: [Gerardo c](https://commons.wikimedia.org/wiki/File:W_014.jpg), CC0.
- `img/carnaval-de-artigas-3.jpg` — La batería de una escuela de samba. Foto: [Gerardo c](https://commons.wikimedia.org/wiki/File:W_017.jpg), CC0.
- `img/carnaval-de-artigas-4.jpg` — Bailarina de una escuela de samba. Foto: [Gerardo c](https://commons.wikimedia.org/wiki/File:W_008.jpg), CC0.
- `img/carnaval-de-artigas-5.jpg` — Un carro alegórico iluminado en la noche del desfile. Foto: [Gerardo c](https://commons.wikimedia.org/wiki/File:W_002.jpg), CC0.
- `img/carnaval-de-artigas-6.jpg` — Un ala de bailarines con fantasías blancas. Foto: [Gerardo c](https://commons.wikimedia.org/wiki/File:W_004.jpg), CC0.
- `img/carnaval-de-artigas-7.jpg` — Una fantasía con alas negras sobre la avenida. Foto: [Gerardo c](https://commons.wikimedia.org/wiki/File:W_011.jpg), CC0.
- `img/carnaval-de-artigas-8.jpg` — Hinchas de la escuela Académicos en 2007. Foto: [Da dinges](https://commons.wikimedia.org/wiki/File:Los_Academicos_1.JPG), Dominio público.

**Museo de la Piedra Preciosa**

- `img/museo-piedra-preciosa-1.jpg` — Amatista de Artigas cortada y pulida (ejemplar de colección, no pertenece al museo). Foto: [Robert M. Lavinsky](https://commons.wikimedia.org/wiki/File:Quartz-288985.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). *(foto de referencia)*
- `img/museo-piedra-preciosa-2.jpg` — Placa de cristales de amatista de Artigas (ejemplar de colección). Foto: [Robert M. Lavinsky](https://commons.wikimedia.org/wiki/File:Quartz-242682.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). *(foto de referencia)*
- `img/museo-piedra-preciosa-3.jpg` — Cristales de amatista de Artigas (ejemplar de colección). Foto: [Robert M. Lavinsky](https://commons.wikimedia.org/wiki/File:Quartz-136010.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). *(foto de referencia)*

**Paseo 7 de Setiembre y Puente de la Concordia**

- `img/paseo-7-de-setiembre-1.jpg` — Vista aérea del Puente de la Concordia entre Artigas y Quaraí. Foto: [Marcelo Campi](https://commons.wikimedia.org/wiki/File:Quara%C3%AD_-_Artigas_Bridge.jpg), [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/).
- `img/paseo-7-de-setiembre-2.jpg` — El Paseo 7 de Setiembre visto desde el puente. Foto: [Asiria Pacheco](https://commons.wikimedia.org/wiki/File:Parque_7_de_Setiembre_visto_desde_arriba.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/paseo-7-de-setiembre-3.jpg` — El lago del Parque Rodó. Foto: [Gerardo Conti P](https://commons.wikimedia.org/wiki/File:Parque_Rodo_Artigas.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/paseo-7-de-setiembre-4.jpg` — El río Cuareim en el Balneario Municipal. Foto: [Gerardo Conti P](https://commons.wikimedia.org/wiki/File:Balneario_Municipal_Artigas.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- `img/paseo-7-de-setiembre-5.jpg` — El Puente Internacional de la Concordia desde la costa. Foto: [Da dinges](https://commons.wikimedia.org/wiki/File:Puente_Internacional_de_la_Concordia.JPG), Dominio público.
- `img/paseo-7-de-setiembre-6.jpg` — Arboleda del Paseo 7 de Setiembre. Foto: [Asiria Pacheco](https://commons.wikimedia.org/wiki/File:Parque_7_de_Setiembre.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

**Piedra Pintada**

- `img/piedra-pintada-1.jpg` — La Piedra Pintada, con su color verde rojizo. Foto: [Gerardo Conti P](https://commons.wikimedia.org/wiki/File:Piedra_Pintada_3.jpg), CC0.
- `img/piedra-pintada-2.jpg` — Vista aérea de la zona de Piedra Pintada en enero de 1988. Foto: [Starbock1948](https://commons.wikimedia.org/wiki/File:Vista_aerea_Piedra_Pintada.JPG), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

**Minas de amatistas de Los Catalanes**

- `img/los-catalanes-1.jpg` — Amatista extraída en Catalán. Foto: [Gonzalo Devia](https://commons.wikimedia.org/wiki/File:Amatista_Laye.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- `img/los-catalanes-2.jpg` — Una mina de amatistas en la zona. Foto: [Javier Techera](https://commons.wikimedia.org/wiki/File:Mina_amatista.JPG), Dominio público.
- `img/los-catalanes-3.jpg` — Otra cara de la misma amatista de Catalán. Foto: [Gonzalo Devia](https://commons.wikimedia.org/wiki/File:Amatista_Laye_2.jpg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Fuentes de la información

Cada ficha lista sus fuentes: Intendencia de Artigas, Ministerio de Turismo, Ministerio de Ambiente, Ministerio del Interior, Presidencia, IMPO, AFE, Museos del Uruguay, Udelar, prensa local y Wikipedia, además de láminas, fotos y textos aportados por docentes, niñas, niños, estudiantes y el equipo de dirección del CEI. Información reunida entre octubre y noviembre de 2026; horarios, tarifas y accesos pueden cambiar.
