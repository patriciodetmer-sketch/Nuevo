# Correo tipo — oferta de terrenos a inmobiliarias

Plantillas para envío masivo personalizado a la base de [`inmobiliarias_santiago.csv`](./inmobiliarias_santiago.csv).
Objetivo: detectar cuáles inmobiliarias están comprando terreno para desarrollo en la RM.

**Antes de enviar, reemplaza todos los campos entre `[corchetes]`.**

## Campos de personalización

Los que salen directo del CSV (merge automático):

| Campo | Columna del CSV |
|---|---|
| `[INMOBILIARIA]` | `inmobiliaria` |
| `[CORREO]` | `email_contacto_general` |
| `[COMUNAS]` | `comunas_santiago` — donde ya desarrollan; úsalo para que el correo no suene genérico |

Los que tienes que definir una vez y quedan fijos:

`[CARGO]` · `[EMPRESA]` · `[TELÉFONO]` · `[CORREO_TUYO]` · `[SITIO_WEB]`

---

## Variante A — tienes paños concretos

Úsala si ya tienes terrenos disponibles para ofrecer. Es la que mejor convierte: llega con algo específico.

**Asunto:** Terreno en [COMUNA] para desarrollo en altura — [SUPERFICIE] m²

> Estimados [INMOBILIARIA]:
>
> Mi nombre es Patricio Detmer, [CARGO] de [EMPRESA]. Trabajo en la búsqueda y gestión de paños para desarrollo inmobiliario en la Región Metropolitana.
>
> Los contacto porque tengo disponible un terreno que calza con el perfil de proyectos que ustedes desarrollan en [COMUNAS]:
>
> - **Comuna:** [COMUNA]
> - **Superficie:** [SUPERFICIE] m²
> - **Normativa:** [ZONIFICACIÓN], altura máxima [ALTURA], constructibilidad [COEFICIENTE]
> - **Potencial estimado:** [N] m² vendibles / [N] unidades
> - **Valor pedido:** UF [VALOR] ([UF/m²] UF/m² de terreno)
>
> Si les hace sentido, les envío la ficha completa con rol, certificado de informes previos y estudio de cabida preliminar.
>
> ¿Con quién debería coordinar en el área de nuevos negocios o estudios?
>
> Quedo atento a su respuesta.
>
> Saludos cordiales,
>
> **Patricio Detmer**
> [CARGO] · [EMPRESA]
> [TELÉFONO] · [CORREO_TUYO]
> [SITIO_WEB]

---

## Variante B — prospección, sin paños definidos aún

Úsala para levantar los criterios de búsqueda de cada inmobiliaria y armar una lista de requerimientos. Pide poco, así que responde más gente.

**Asunto:** ¿Están buscando terrenos en Santiago? — [EMPRESA]

> Estimados [INMOBILIARIA]:
>
> Mi nombre es Patricio Detmer, [CARGO] de [EMPRESA]. Me dedico a la búsqueda y gestión de terrenos para desarrollo inmobiliario en la Región Metropolitana.
>
> Vi que tienen proyectos en [COMUNAS], así que los contacto para saber si están comprando terreno actualmente y con qué criterios. Concretamente:
>
> - ¿En qué comunas están buscando hoy?
> - ¿Qué superficie mínima les sirve?
> - ¿Qué rango de UF/m² de terreno manejan?
> - ¿Trabajan con opción de compra o compran directo?
>
> Con eso les hago llegar solo lo que efectivamente calce con su búsqueda, sin llenarlos de correos.
>
> Si prefieren, coordinamos una llamada de 15 minutos.
>
> Saludos cordiales,
>
> **Patricio Detmer**
> [CARGO] · [EMPRESA]
> [TELÉFONO] · [CORREO_TUYO]
> [SITIO_WEB]

---

## Seguimiento (enviar a los 5–7 días hábiles, solo a quien no respondió)

**Asunto:** Re: [asunto original]

> Estimados [INMOBILIARIA]:
>
> Insisto brevemente por si el correo anterior no llegó a la persona indicada.
>
> Si hoy no están comprando terreno, me sirve igual saberlo y no los molesto más. Y si el tema lo ve otra persona del equipo, agradezco que me la deriven.
>
> Saludos cordiales,
>
> **Patricio Detmer**
> [TELÉFONO] · [CORREO_TUYO]

---

## Cómo enviarlo

**No uses copia oculta con los 21 correos en un solo envío.** Un correo a 21 destinatarios en CCO tiene mucha más probabilidad de caer en spam y no permite personalizar. Usa envío uno a uno con merge (Gmail + extensión de mail merge, Mailchimp, Brevo, o similar).

**Buenas prácticas que sí mueven la tasa de respuesta:**

1. **Envía desde tu dominio propio**, no desde Gmail personal. Con SPF y DKIM configurados.
2. **Personaliza al menos el campo `[COMUNAS]`.** Es la diferencia entre un correo masivo evidente y uno que parece escrito para ellos.
3. **Tandas de 20–30 por día**, no todo de una vez.
4. **Martes a jueves, 9:00–11:00.** Lunes y viernes rinden peor.
5. **Asunto corto y concreto.** Sin "oportunidad única" ni signos de exclamación: los filtros de spam los castigan y el rubro los lee como venta agresiva.

**Cumplimiento legal (Chile):** la Ley 19.496 (art. 28 B) exige que toda comunicación promocional por correo identifique al remitente e incluya una vía para pedir que no te escriban más. Agrega al pie:

> Si no desea recibir más correos de nuestra parte, responda con "Baja" y lo retiraremos de nuestra lista.

## A quién enviar

| Grupo | Cuántas | Acción |
|---|---|---|
| Confianza alta | 16 | Envío directo |
| Confianza media | 5 | Envío directo, pero verifica rebotes |
| Confianza baja | 4 | La casilla es de denuncias o postventa. Mejor llamar y pedir el correo de nuevos negocios |
| Sin correo | 13 | Formulario web del sitio, o llamada al teléfono de la planilla |

Para los 17 de los dos últimos grupos, el guion telefónico es una línea: *"Buenas, soy Patricio Detmer de [EMPRESA], trabajo con terrenos para desarrollo. ¿Me puede dar el correo del área de nuevos negocios o estudios para enviarles información?"*

## Qué esperar

En prospección en frío al rubro inmobiliario, una tasa de respuesta razonable va del 10% al 20% con seguimiento incluido. Sobre 21 correos son 2 a 4 respuestas. Por eso conviene trabajar en paralelo los 17 sin correo: el teléfono convierte mucho mejor que el correo frío, y ahí está la mitad de la base.
