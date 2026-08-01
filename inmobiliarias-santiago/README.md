# Levantamiento: inmobiliarias que desarrollan edificios en Santiago

Base de contactos de inmobiliarias con **desarrollo de edificios (departamentos) en la Región Metropolitana**, con oferta vigente o histórico reciente de proyectos.

- **Excel:** [`inmobiliarias_santiago.xlsx`](./inmobiliarias_santiago.xlsx) — hoja `Contactos` (filtros, semáforo de confianza, correos y webs clicleables) + hoja `Resumen`
- **Datos planos:** [`inmobiliarias_santiago.csv`](./inmobiliarias_santiago.csv)
- **Empresas en esta versión:** 38
- **Fecha de levantamiento:** agosto 2026

## Columnas

| Columna | Contenido |
|---|---|
| `inmobiliaria` | Nombre comercial |
| `sitio_web` | Dominio oficial |
| `email_contacto_general` | Correo general publicado, o el hallazgo real si no hay uno |
| `tipo_email` | `general`, `comercial`, `ventas`, `servicio al cliente`, `corporativo`, `nominal`, `por proyecto` |
| `telefono` | Teléfono de casa matriz o contact center |
| `direccion_casa_matriz` | Dirección corporativa |
| `comunas_santiago` | Comunas RM donde tienen o han tenido proyectos |
| `segmento` | Tipo de producto |
| `confianza_email` | `alta` / `media` / `baja` / `sin dato` |
| `fuente` | De dónde salió el dato |

## Cómo leer `confianza_email`

- **alta** — correo corporativo publicado por la propia empresa (contacto, ventas o servicio al cliente).
- **media** — correo corporativo real pero de alcance parcial: dominio a verificar, correo de un proyecto puntual, o casilla del holding y no de la inmobiliaria.
- **baja** — solo existe una casilla de propósito acotado (denuncias, postventa) o un contacto nominal de un ejecutivo; sirve como puerta de entrada, no como correo institucional.
- **sin dato** — la empresa no publica correo; el canal es formulario web o teléfono.

**21 de las 38** empresas tienen correo utilizable: 16 con confianza alta y 5 con media. De las 17 restantes, 4 tienen solo una casilla acotada (confianza baja) y 13 no publican correo alguno — para esas el camino es el formulario web o una llamada pidiendo el correo del área comercial.

## Metodología y límites

**Fuentes usadas:** búsqueda web sobre sitios corporativos, páginas de contacto y servicio al cliente, fichas de directorios sectoriales (Pabellón, Portal PM, Mercantil), prensa sectorial (La Tercera/Pulso, CChC, CCS) y listados de eventos del rubro (Black Inmobiliario 2026, organizado por CCS + ADI + ABIF + CChC).

**Dos limitaciones del entorno condicionaron el trabajo, y conviene tenerlas presentes al evaluar la cobertura:**

1. **No hubo acceso directo a sitios web.** La política de red de esta sesión bloquea la navegación (todo intento devuelve HTTP 403), incluidos `adi-ag.cl/empresas-asociadas` (los 52 socios de la Asociación de Desarrolladores Inmobiliarios), el directorio de `pabellon.cl/vendedor/inmobiliarias` y las páginas de contacto de cada empresa. Los datos se obtuvieron mediante búsqueda web, no leyendo la fuente. Por eso cada fila lleva `confianza_email`.
2. **La cuota de BigQuery de Data Inmobiliaria está agotada** (plan demo, cupo de por vida consumido). Eso impidió el cruce más potente disponible: filtrar la tabla `publicaciones` por `es_proyecto = TRUE` en comunas de la RM para obtener el universo real de proyectos en venta hoy y desde ahí derivar los desarrolladores activos con evidencia de mercado, en vez de partir de nombres conocidos.

**Alcance:** la lista cubre a los principales desarrolladores de edificios de la RM, no es un censo exhaustivo. Faltan actores chicos y de nicho, y desarrolladores que operan por SPA por proyecto sin marca comercial visible.

## Cómo completar el censo

En orden de rendimiento:

1. **Reactivar la cuota de Data Inmobiliaria** ([plan de pago](https://datainmobiliaria.cl/organizations/select_plan)). Con `publicaciones` filtrada por `es_proyecto = TRUE` + comunas RM se obtiene el universo de proyectos en venta vigentes, y con `contenido_publicacion` sobre cada aviso se extrae el desarrollador. Eso convierte esta lista curada en un censo con respaldo de datos y actualizable.
2. **Habilitar navegación web en el entorno** para leer `adi-ag.cl/empresas-asociadas` (52 socios ADI) y las páginas de contacto una a una, cerrando los 17 correos faltantes.
3. **Padrón CChC** — el registro de socios de la Cámara Chilena de la Construcción suma constructoras-inmobiliarias que no están en ADI.

## Anexo: operadores de renta residencial (no desarrolladores puros)

Actores relevantes en edificios de Santiago que operan o financian, más que desarrollar de punta a punta. Van aparte porque el criterio del levantamiento es *desarrollar edificios*:

| Empresa | Rol | Web |
|---|---|---|
| Assetplan | Mayor administradora de edificios de renta residencial del país | assetplan.cl |
| Greystar | Operador global de multifamily; desarrolla con socios locales | greystar.com |
| Cimenta | AGF con más de 30 años en desarrollo y gestión de activos de renta | cimenta.cl |

El mercado multifamily de Santiago cerró 2025 con 183 edificios en operación y 44.020 departamentos; la comuna de Santiago concentra el 29,2%, seguida de Estación Central (13%) y La Florida (9,1%).
