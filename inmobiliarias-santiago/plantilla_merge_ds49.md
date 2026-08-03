# Plantilla de merge — DS49, entidades patrocinantes

Sirve igual para las dos tandas generadas:

| Categoría | Archivo | Destinatarios únicos |
|---|---|---|
| Primera | [`merge_ds49_categoria_primera.csv`](./merge_ds49_categoria_primera.csv) / [`.xlsx`](./merge_ds49_categoria_primera.xlsx) | 73 (de 75 en la nómina) |
| Segunda | [`merge_ds49_categoria_segunda.csv`](./merge_ds49_categoria_segunda.csv) / [`.xlsx`](./merge_ds49_categoria_segunda.xlsx) | 21 |

**94 destinatarios en total** entre ambas. Para generar otra categoría: `python3 fuentes/build_merge.py TERCERA`.

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

## Las categorías, y cómo secuenciar el envío

De las 270 entidades patrocinantes habilitadas en la RM: **134 Tercera, 75 Primera, 40 Única, 21 Segunda.** Es la clasificación que asigna el MINVU en su nómina. **Conviene verificar el criterio exacto en la normativa antes de sacar conclusiones**, pero como filtro para acotar una campaña funciona.

Orden sugerido:

1. **Primera (73)** — la tanda principal. Tres o cuatro días de envío.
2. **Segunda (21)** — una sola tanda. Ninguna comparte correo, así que son 21 limpios.
3. **Tercera (134) y Única (40)** — solo si las dos primeras rinden. Ahí conviene cortar por comuna antes que mandar 174 correos de una.

Un contraste útil entre las dos primeras tandas: en Primera, 40 de 73 tienen dominio propio; en Segunda, solo 9 de 21. La categoría Segunda es notoriamente más chica y artesanal, así que ahí el teléfono pesa aún más que el correo.

## Antes de lanzar

1. Reemplaza los `[CORCHETES]` — datos del terreno y tu firma.
2. Envía desde tu dominio, con SPF y DKIM configurados.
3. Tandas de 20–25 al día: Primera son tres o cuatro días, Segunda cabe en uno.
4. Martes a jueves, 9:00–11:00.
5. En Primera, dos filas comparten casilla con otra entidad (marcadas en la columna `nota`): ya están deduplicadas, pero si alguien responde, ten presente que puede hablar por dos entidades. En Segunda no hay casillas compartidas.
6. **Casi la mitad de los correos son de casilla gratuita** — 33 de 73 en Primera, 12 de 21 en Segunda. Son entidades chicas, muchas unipersonales. Ahí el teléfono convierte bastante mejor que el correo, y la planilla trae todos los números.
