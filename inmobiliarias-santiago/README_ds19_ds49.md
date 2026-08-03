# Levantamiento 2: entidades que desarrollan vivienda social DS19 y DS49

- **Excel:** [`inmobiliarias_ds19_ds49.xlsx`](./inmobiliarias_ds19_ds49.xlsx) — hojas `DS19`, `DS49` y `Resumen`
- **Datos planos:** [`inmobiliarias_ds19_ds49.csv`](./inmobiliarias_ds19_ds49.csv)
- **Entidades:** 39 (27 con DS19, 21 con DS49; varias operan en ambos)
- **Con presencia en la RM:** 31
- **Con correo directo:** 25
- **Fecha:** agosto 2026

## Nómina oficial de entidades patrocinantes — incorporada

El PDF oficial de la **nómina MINVU/DITEC de junio 2026** (47 páginas, 1.256 entidades en todo el país) se procesó y se filtró por Región Metropolitana:

- **[`entidades_patrocinantes_rm.csv`](./entidades_patrocinantes_rm.csv) / [`.xlsx`](./entidades_patrocinantes_rm.xlsx) — 270 entidades patrocinantes de la RM, todas con correo y teléfono**, más RUT, contacto, dirección, comuna, categoría MINVU y número de resolución.

Con esa fuente se corrigieron y completaron las filas de la hoja DS49:

**Corrección.** Cinco entidades que se habían agregado a partir de índices de búsqueda resultaron **no ser de la Región Metropolitana** y se eliminaron: Jessica Sandoval Quiroga E.I.R.L. y Manuel Medina E.I.R.L. (Tarapacá), Inmobiliaria D&M (Tarapacá), Nahuen Ingenieros Constructores Asociados y Ávalos y Ibacache Arquitectos Sociales (Antofagasta). Los índices de búsqueda no conservan la columna de región, y esa fue la causa del error.

**Verificadas y completadas con correo oficial** — INSOC, Consultora e Inmobiliaria Hogar, Miraflores, Consultora V y S, Emile Straub, Municipalidad de Huechuraba, Urbanismo Social (opera como *Asesorías Gestión Vivienda Ltda*), TECHO (*Fundación Un Techo para Chile*), OVAL (tiene una EP propia, *OVAL Entidad Patrocinante Ltda*), Evolutiva, Kutralwe y Gestora Mas Hogar.

**Dos socias de ADVS aparecieron en la nómina** y quedaron confirmadas como RM: **Consolida SpA** (`contacto@consolida.cl`) e **Identidades** (`fmella@consultoraidentidades.com`).

**DOMUM** figuraba en un documento MINVU antiguo pero **no aparece en la nómina de junio 2026** — probablemente ya no está habilitada. Queda marcada así en el archivo.

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

1. **Sin acceso directo a sitios web** (bloqueo de red, HTTP 403). La nómina de entidades patrocinantes ya se resolvió con el PDF aportado manualmente, pero siguen pendientes el **listado oficial de proyectos DS19 vigentes del MINVU** y el **padrón de socios de la ADVS** (43 miembros). Ambos son públicos.
2. **La cuota de BigQuery de Data Inmobiliaria está agotada.**
3. **La nómina es de junio 2026 y se actualiza mensualmente.** Antes de una campaña conviene bajar la versión vigente.

**Sobre la calidad de las filas:** las 7 marcadas `Por confirmar` (Albores, Consolida, Urbanitas, Grupo Vías, Ciclos, Identidades, Fundación Deportistas por un Sueño) son socias de la ADVS identificadas por nombre en fuentes secundarias — existen, pero no tengo sitio web ni contacto verificado. Y la nómina de entidades patrocinantes DS49 de la RM es **parcial**: son las que aparecieron nombradas en documentos MINVU citados en resultados de búsqueda, no el listado oficial.

## Para completar

1. ~~Nómina oficial de entidades patrocinantes~~ — **hecho**, 270 entidades de la RM en `entidades_patrocinantes_rm.csv`.
2. **Portal de oferta inmobiliaria del MINVU** — proyectos DS19 vigentes con sala de ventas y entidad desarrolladora por proyecto. Es lo que falta para cerrar el lado DS19.
3. **`advschile.cl`** — los 43 socios del gremio; 7 siguen sin contacto verificado.
4. **SERVIU Metropolitano** — proyectos DS49 en ejecución, para saber qué EP están activas hoy y no solo habilitadas.
