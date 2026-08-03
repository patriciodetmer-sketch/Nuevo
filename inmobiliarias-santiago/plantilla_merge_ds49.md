# Plantilla de merge — DS49, entidades patrocinantes categoría Primera

Archivo de destinatarios: [`merge_ds49_categoria_primera.csv`](./merge_ds49_categoria_primera.csv) / [`.xlsx`](./merge_ds49_categoria_primera.xlsx) — **73 destinatarios únicos**.

Los campos entre `{{llaves}}` los reemplaza la herramienta de merge desde las columnas del CSV. Los campos entre `[CORCHETES]` los reemplazas tú **una sola vez** antes de lanzar la campaña: son constantes, no varían por destinatario.

## Asunto

```
Terreno en [COMUNA_TERRENO] para proyecto DS49 — con opción de compra
```

## Cuerpo

```
{{saludo}}:

Mi nombre es Patricio Detmer, [CARGO] de [EMPRESA]. Trabajo en la búsqueda y
gestión de terrenos en la Región Metropolitana.

Los contacto porque están habilitados como entidad patrocinante en la región, y
sé que una de las trabas habituales para levantar un proyecto DS49 es encontrar
paño disponible que aguante los tiempos de la postulación.

Tengo un terreno que podría servir:

- Comuna: [COMUNA_TERRENO]
- Superficie: [SUPERFICIE] m²
- Uso de suelo: habitacional, [ZONIFICACIÓN]
- Factibilidad: [estado de agua, alcantarillado y electricidad]
- Capacidad estimada: [N] viviendas
- Valor pedido: UF [VALOR]

Lo importante: estoy disponible para estructurarlo como opción de compra o
promesa condicionada a la asignación del subsidio, de modo que el comité no
tenga que comprometer recursos antes de tener certeza. Sé que sin eso la
operación no es viable para ustedes.

Si tienen un comité buscando terreno en el sector, les envío la ficha con rol,
certificado de informes previos y estado de factibilidad.

¿Con quién puedo revisarlo?

Saludos cordiales,

Patricio Detmer
[CARGO] · [EMPRESA]
[TELÉFONO] · [CORREO_TUYO]
[SITIO_WEB]

—
Si no desea recibir más correos de nuestra parte, responda con "Baja" y lo
retiraremos de nuestra lista.
```

## Seguimiento (5–7 días hábiles, solo a quien no respondió)

**Asunto:** `Re: Terreno en [COMUNA_TERRENO] para proyecto DS49 — con opción de compra`

```
{{saludo}}:

Insisto brevemente por si el correo no llegó a la persona indicada.

Si hoy no tienen comités buscando terreno, me sirve saberlo y no los molesto
más. Y si el tema lo ve otra persona del equipo, agradezco que me la deriven.

Saludos cordiales,

Patricio Detmer
[TELÉFONO] · [CORREO_TUYO]
```

## Campos disponibles

| Campo | Contenido | Úsalo para |
|---|---|---|
| `{{saludo}}` | "Estimados <nombre corto de la entidad>" | Abrir el correo |
| `{{entidad}}` | Razón social completa | Referencia interna |
| `{{entidad_corta}}` | Nombre de fantasía | Alternativa al saludo |
| `{{comuna}}` | Comuna de la casa matriz de la EP | **Registro interno, no el correo** |
| `{{telefono_1}}` | Teléfono principal | Seguimiento telefónico |
| `{{rut}}` | RUT de la entidad | Registro interno |

**`{{comuna}}` es la comuna de la oficina de la entidad, no la del terreno.** No la uses en el cuerpo: decir "sé que operan desde Providencia" no aporta nada y suena a base de datos.

**No uses el campo de contacto como saludo.** En el PDF de MINVU el nombre de la persona y la dirección vienen fusionados en una sola celda, y la separación que hice es heurística: hay nombres cortados a la mitad y filas donde quedó texto de la dirección. Sirve para saber por quién preguntar al llamar, confirmándolo en la llamada. En un correo, un nombre mal puesto hace más daño que no poner ninguno.

## Por qué categoría Primera

De las 270 entidades patrocinantes habilitadas en la RM, 75 son categoría Primera (y 73 buzones únicos). Es la clasificación que asigna el MINVU en su nómina. **Conviene verificar el criterio exacto en la normativa antes de sacar conclusiones**, pero como primer filtro para una campaña acotada funciona: reduce 270 a 73 sin quedarse con las entidades más pequeñas.

Si esta tanda responde bien, la siguiente natural es categoría Segunda (21 entidades). Tercera son 134 y Única 40 — ahí conviene otro criterio de corte, probablemente por comuna.

## Antes de lanzar

1. Reemplaza los `[CORCHETES]` — datos del terreno y tu firma.
2. Envía desde tu dominio, con SPF y DKIM configurados.
3. Tandas de 20–25 al día: son 73, o sea tres o cuatro días.
4. Martes a jueves, 9:00–11:00.
5. Dos filas comparten casilla con otra entidad (marcadas en la columna `nota`): ya están deduplicadas, pero si alguien responde, ten presente que puede hablar por dos entidades.
6. **Buena parte de los correos son Gmail personal.** Son entidades chicas, muchas unipersonales. Ahí el teléfono convierte bastante mejor que el correo, y la planilla trae todos los números.
