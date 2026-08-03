# Levantamiento 2: entidades que desarrollan vivienda social DS19 y DS49

- **Excel:** [`inmobiliarias_ds19_ds49.xlsx`](./inmobiliarias_ds19_ds49.xlsx) — hojas `DS19`, `DS49` y `Resumen`
- **Datos planos:** [`inmobiliarias_ds19_ds49.csv`](./inmobiliarias_ds19_ds49.csv)
- **Entidades:** 44 (27 con DS19, 26 con DS49; varias operan en ambos)
- **Con presencia en la RM:** 34
- **Con correo directo:** 11
- **Fecha:** agosto 2026

## Estado de la nómina oficial de entidades patrocinantes

**No se pudo descargar.** La política de red de este entorno rechaza la conexión a los dominios de MINVU en el gateway de salida (403 al CONNECT, tanto `proveedorestecnicos.minvu.gob.cl` como `proveedores-tecnicos.minvu.gob.cl` y `minvu.gob.cl`). No es una caída del sitio ni un bloqueo del servidor: es la política de egreso del entorno.

Lo que sí se recuperó, vía índices de búsqueda sobre el PDF de la **nómina de junio 2026**, son 8 entidades patrocinantes de la RM que antes no estaban: Evolutiva, Kutralwe, Jessica Sandoval Quiroga E.I.R.L., Manuel Medina E.I.R.L., Gestora Mashogar, Inmobiliaria D&M, Nahuen Ingenieros Constructores Asociados, y Ávalos y Ibacache Arquitectos Sociales. **Solo el nombre** — el PDF trae además RUT, contacto, dirección, comuna, teléfono y correo de cada una, y eso sigue pendiente.

**Para obtenerla, descarga directa desde:**

- Página índice: `proveedorestecnicos.minvu.gob.cl/entidades-patrocinantes/`
- PDF de junio 2026: `proveedores-tecnicos.minvu.gob.cl/wp-content/uploads/2017/04/Nomina-de-entidades-habilitadas-a-operar-por-region-Junio-2026_compressed.pdf`

Con ese archivo en el repositorio, las columnas de correo y teléfono de la hoja DS49 se completan de una pasada.

## Lo primero: DS19 y DS49 no se contactan igual

Esta es la diferencia que cambia toda la estrategia, y conviene tenerla clara antes de mirar la lista.

**DS19 (Integración Social y Territorial)** funciona como el mercado libre. Una **entidad desarrolladora** —inmobiliaria o constructora— compra el terreno, postula el proyecto a concurso MINVU, construye y vende. El subsidio viene incorporado al proyecto y la familia postula en la sala de ventas. Para vender terreno, el interlocutor es directo: la inmobiliaria.

**DS49 (Fondo Solidario de Elección de Vivienda)** no funciona así. La familia postula —individual o colectivamente, vía comité— acompañada por una **Entidad Patrocinante (EP)**, que intermedia ante el SERVIU, formula el proyecto y contrata a la constructora. Aquí **quien decide la compra del terreno suele ser la EP o el comité, no una inmobiliaria.** Si el objetivo es ofrecer paños, en DS49 el interlocutor es la EP, no una constructora.

Por eso el archivo tiene dos hojas y no una sola lista.

## Quién es quién

**Especialistas puros en vivienda social** — su negocio principal es DS19/DS49:
iSiete, ICuadra, Koyam, Noval, Vive Tu Barrio, Nexos, Comosa, IVL, CISS, Urbani.

**Inmobiliarias de mercado libre con línea de subsidio** — desarrollan ambos mundos, y ya están en el levantamiento 1:
Socovesa, Pilares, Besalco, PY, Los Silos, Maestra, Ecomac, Siena, Convet.

**Fundaciones y entidades patrocinantes** — el mundo DS49:
TECHO-Chile (Inmobiliaria Social), Urbanismo Social / Fundación Gestión Vivienda, DOMUM, INSOC, Consultora e Inmobiliaria Hogar, Miraflores, Consultora V y S, Emile Straub, I. Municipalidad de Huechuraba, Constructora OVAL.

## Los 11 correos directos

| Entidad | Correo | Programas |
|---|---|---|
| iSiete Grupo Inmobiliario | contacto@isiete.cl | DS19 / DS1 |
| Inmobiliaria ICuadra | contacto@icuadra.cl | DS19 |
| Inmobiliaria Koyam | contacto@koyam.cl | DS19 / DS1 |
| Comosa Gestión Inmobiliaria | contacto@comosa.cl | DS19 |
| Socovesa | contacto@socovesa.cl | DS19 / DS1 / DS15 |
| Pilares | servicioalcliente@pilares.cl | DS19 / DS1 |
| Besalco Inmobiliaria | ventas@besalco.cl | DS19 / DS49 / DS1 |
| Siena Inmobiliaria | informes@sienainmobiliaria.com | DS19 / DS1 |
| Urbani | contacto@urbani.cl | DS19 / DS1 |
| IVL | contacto@ivl.cl | DS19 |
| Inmobiliaria Noval | postventainoval@inoval.cl | DS19 / DS1 / DS49 |

El de Noval es de postventa, no comercial — úsalo solo como puerta de entrada para pedir el correo del área de nuevos negocios.

## Gremios de referencia

- **ADVS** (Asociación de Desarrolladores de Viviendas Sociales, fundada 2021) — 43 miembros entre inmobiliarias, constructoras, entidades patrocinantes, fundaciones e industrializadores. Es el gremio específico del rubro. `advschile.cl`
- **ADI** (Asociación de Desarrolladores Inmobiliarios) — 52 socios; varios tienen línea DS19.

## Limitaciones

Las mismas dos del levantamiento 1, y pesan más aquí porque las fuentes oficiales son justamente las bloqueadas:

1. **Sin acceso directo a sitios web** (bloqueo de red, HTTP 403). No se pudo descargar el **listado oficial de proyectos DS19 vigentes del MINVU**, la **nómina de entidades patrocinantes de la RM** (`proveedorestecnicos.minvu.gob.cl`, se actualiza mensualmente) ni el **padrón de socios de la ADVS**. Los tres son listados públicos y completos: con navegación habilitada, esta lista pasa de 36 a probablemente más de 100 entidades.
2. **La cuota de BigQuery de Data Inmobiliaria está agotada.**

**Sobre la calidad de las filas:** las 7 marcadas `Por confirmar` (Albores, Consolida, Urbanitas, Grupo Vías, Ciclos, Identidades, Fundación Deportistas por un Sueño) son socias de la ADVS identificadas por nombre en fuentes secundarias — existen, pero no tengo sitio web ni contacto verificado. Y la nómina de entidades patrocinantes DS49 de la RM es **parcial**: son las que aparecieron nombradas en documentos MINVU citados en resultados de búsqueda, no el listado oficial.

## Para completar

1. **`proveedorestecnicos.minvu.gob.cl/entidades-patrocinantes/`** — nómina oficial de EP por región, mensual. Es la fuente que convierte la hoja DS49 en un censo real.
2. **Portal de oferta inmobiliaria del MINVU** — proyectos DS19 vigentes con sala de ventas y entidad desarrolladora por proyecto.
3. **`advschile.cl`** — los 43 socios, que cubren buena parte del rubro.
4. **SERVIU Metropolitano** — nómina regional y proyectos DS49 en ejecución.
