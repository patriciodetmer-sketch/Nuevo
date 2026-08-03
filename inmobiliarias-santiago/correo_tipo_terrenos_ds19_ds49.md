# Correo tipo — oferta de terrenos para vivienda social (DS19 y DS49)

Adaptación de [`correo_tipo_terrenos.md`](./correo_tipo_terrenos.md) para la base de [`inmobiliarias_ds19_ds49.csv`](./inmobiliarias_ds19_ds49.csv).

**Son dos correos distintos, no uno con variantes de saludo.** Van a interlocutores con lógicas de compra diferentes, y mandar el correo equivocado se nota de inmediato.

## Por qué cambia el pitch

| | DS19 | DS49 |
|---|---|---|
| **A quién le escribes** | La inmobiliaria desarrolladora | La Entidad Patrocinante (EP) |
| **Quién decide el terreno** | La inmobiliaria, como cualquier compra | La EP junto al comité de vivienda |
| **Cuándo compra** | Necesita el paño **antes** de postular al llamado MINVU | No puede comprar hasta tener el subsidio asignado |
| **Qué le importa del paño** | Localización (puntúa en el concurso), densidad permitida, cabida | Precio por vivienda, factibilidad, tamaño acorde al comité |
| **Instrumento comercial** | Compra o promesa | **Opción de compra condicionada a la asignación del subsidio** |

Ese último punto es el que decide si te responden o no en DS49: una EP no tiene cómo comprarte un terreno hoy. Si tu correo no ofrece esperar la asignación, el correo muere ahí. Y es también tu palanca de negociación: estás ofreciendo algo que el vendedor común no ofrece.

## Campos de personalización

Del CSV: `[ENTIDAD]` (columna `entidad`), `[CORREO]`, `[PROGRAMAS]`.
Fijos tuyos: `[CARGO]` · `[EMPRESA]` · `[TELÉFONO]` · `[CORREO_TUYO]` · `[SITIO_WEB]`

---

## Correo DS19 — a inmobiliarias desarrolladoras

**Asunto:** Paño en [COMUNA] para proyecto DS19 — [SUPERFICIE] m²

> Estimados [ENTIDAD]:
>
> Mi nombre es Patricio Detmer, [CARGO] de [EMPRESA]. Trabajo en la búsqueda y gestión de terrenos para desarrollo inmobiliario en la Región Metropolitana.
>
> Los contacto porque sé que desarrollan proyectos con subsidio DS19 y tengo un paño que calza con ese perfil:
>
> - **Comuna:** [COMUNA]
> - **Superficie:** [SUPERFICIE] m²
> - **Uso de suelo y normativa:** [ZONIFICACIÓN], altura máxima [ALTURA], constructibilidad [COEFICIENTE]
> - **Localización:** a [N] cuadras de [METRO / paradero / servicios], [establecimientos educacionales y salud en el radio]
> - **Cabida preliminar:** [N] viviendas
> - **Valor pedido:** UF [VALOR] ([UF/m²] UF/m² de terreno)
>
> Incluí la localización con detalle porque sé que es lo que pesa en la evaluación del concurso, no solo la cabida.
>
> Si les interesa evaluarlo para el próximo llamado, les envío la ficha con rol, certificado de informes previos y factibilidad sanitaria. Tengo disponibilidad para estructurar la operación con los plazos del concurso, si eso les acomoda.
>
> ¿Con quién debería coordinar en el área de nuevos negocios?
>
> Saludos cordiales,
>
> **Patricio Detmer**
> [CARGO] · [EMPRESA]
> [TELÉFONO] · [CORREO_TUYO]
> [SITIO_WEB]

### Variante DS19 sin paño definido (prospección)

**Asunto:** Búsqueda de paños para DS19 — ¿qué perfil están necesitando?

> Estimados [ENTIDAD]:
>
> Mi nombre es Patricio Detmer, [CARGO] de [EMPRESA]. Me dedico a la búsqueda y gestión de terrenos en la Región Metropolitana.
>
> Sé que desarrollan proyectos DS19 y quiero enfocar bien la búsqueda antes de mandarles cosas que no les sirven. Concretamente:
>
> - ¿En qué comunas están buscando para los próximos llamados?
> - ¿Qué rango de superficie y de viviendas por proyecto manejan?
> - ¿Hasta qué UF/m² de terreno les cierra el negocio con los topes de precio del programa?
> - ¿Necesitan el paño con factibilidad sanitaria resuelta o lo toman en bruto?
>
> Con eso les llega solo lo que calza. Si prefieren, coordinamos 15 minutos por teléfono.
>
> Saludos cordiales,
>
> **Patricio Detmer**
> [CARGO] · [EMPRESA] · [TELÉFONO] · [CORREO_TUYO]

---

## Correo DS49 — a entidades patrocinantes

Más colaborativo y menos comercial. La EP no es un comprador con caja: es un intermediario que trabaja con familias y con plazos del SERVIU. El correo tiene que reconocer eso desde la primera línea.

**Asunto:** Terreno disponible en [COMUNA] para proyecto DS49 — con opción de compra

> Estimados [ENTIDAD]:
>
> Mi nombre es Patricio Detmer, [CARGO] de [EMPRESA]. Trabajo en la búsqueda y gestión de terrenos en la Región Metropolitana.
>
> Los contacto porque sé que patrocinan comités de vivienda en postulaciones DS49, y una de las trabas habituales es encontrar paño disponible que aguante los tiempos de la postulación.
>
> Tengo un terreno que podría servir:
>
> - **Comuna:** [COMUNA]
> - **Superficie:** [SUPERFICIE] m²
> - **Uso de suelo:** habitacional, [ZONIFICACIÓN]
> - **Factibilidad:** [estado de factibilidad de agua, alcantarillado y electricidad]
> - **Capacidad estimada:** [N] viviendas
> - **Valor pedido:** UF [VALOR]
>
> **Lo importante: estoy disponible para estructurarlo como opción de compra o promesa condicionada a la asignación del subsidio**, de modo que el comité no tenga que comprometer recursos antes de tener certeza. Sé que sin eso la operación no es viable para ustedes.
>
> Si tienen un comité buscando terreno en el sector, les envío la ficha con rol, certificado de informes previos y estado de factibilidad.
>
> ¿Con quién puedo revisarlo?
>
> Saludos cordiales,
>
> **Patricio Detmer**
> [CARGO] · [EMPRESA]
> [TELÉFONO] · [CORREO_TUYO]
> [SITIO_WEB]

### Variante DS49 de prospección

**Asunto:** ¿Tienen comités buscando terreno en la RM?

> Estimados [ENTIDAD]:
>
> Mi nombre es Patricio Detmer, [CARGO] de [EMPRESA]. Busco y gestiono terrenos en la Región Metropolitana.
>
> Trabajo con paños que pueden estructurarse con opción de compra condicionada a la asignación del subsidio, que entiendo es la forma en que ustedes pueden operar sin arriesgar recursos del comité antes de tiempo.
>
> Para enfocar la búsqueda:
>
> - ¿Tienen comités actualmente en busca de terreno? ¿En qué comunas?
> - ¿De qué tamaño son los grupos, en número de familias?
> - ¿Qué valor de terreno por vivienda les permite cerrar el proyecto dentro del marco del subsidio?
> - ¿Necesitan factibilidad resuelta o los acompañan ustedes en esa gestión?
>
> Quedo atento, y con gusto coordinamos una llamada.
>
> Saludos cordiales,
>
> **Patricio Detmer**
> [CARGO] · [EMPRESA] · [TELÉFONO] · [CORREO_TUYO]

---

## Seguimiento (5–7 días hábiles, solo a quien no respondió)

> Estimados [ENTIDAD]:
>
> Insisto brevemente por si el correo no llegó a la persona indicada.
>
> Si hoy no están buscando terreno, me sirve saberlo y no los molesto más. Y si el tema lo ve otra persona del equipo, agradezco que me la deriven.
>
> Saludos cordiales,
>
> **Patricio Detmer** · [TELÉFONO] · [CORREO_TUYO]

---

## A quién enviar

De las 36 entidades del levantamiento, **11 tienen correo directo**:

| Correo DS19 | Correo DS49 |
|---|---|
| contacto@isiete.cl | ventas@besalco.cl |
| contacto@icuadra.cl | postventainoval@inoval.cl |
| contacto@koyam.cl | |
| contacto@comosa.cl | |
| contacto@socovesa.cl | |
| servicioalcliente@pilares.cl | |
| ventas@besalco.cl | |
| informes@sienainmobiliaria.com | |
| contacto@urbani.cl | |
| contacto@ivl.cl | |
| postventainoval@inoval.cl | |

Besalco y Noval reciben ambos programas: mándales el de DS19, que es donde tienen más volumen, y menciona DS49 en una línea.

El correo de Noval es de postventa. No le mandes la oferta completa: pide primero el correo del área de nuevos negocios.

**Las otras 25 entidades no tienen correo publicado.** Ahí el canal es teléfono o formulario, con este guion:

> *"Buenas, soy Patricio Detmer de [EMPRESA], trabajo con terrenos para desarrollo. ¿Me puede dar el correo del área de nuevos negocios? Tengo paños que podrían servirles para proyectos DS19."*

Para las entidades patrocinantes de la hoja DS49, casi ninguna tiene web propia identificada. La vía real es la **nómina oficial de EP del MINVU** (`proveedorestecnicos.minvu.gob.cl/entidades-patrocinantes/`), que **incluye teléfono y correo de cada entidad por región** — es exactamente el dato que falta, y se actualiza mensualmente. Descargarla debería ser el paso previo a cualquier envío masivo a DS49.

## Dos advertencias

**Verifica los topes del programa antes de citar cifras.** No puse montos de subsidio ni topes de precio de venta en las plantillas a propósito: cambian por llamado y por zona. Si vas a mencionar que un paño "calza con el tope del programa", revisa las bases del llamado vigente en minvu.gob.cl — equivocarte en eso frente a un desarrollador especializado te quema la credibilidad en el primer correo.

**El resto de las buenas prácticas de envío** (dominio propio con SPF y DKIM, tandas de 20–30, martes a jueves, pie de baja por Ley 19.496 art. 28 B) están en [`correo_tipo_terrenos.md`](./correo_tipo_terrenos.md) y aplican igual acá.
