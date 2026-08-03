import re, csv, unicodedata

REGIONES = ["ARICA Y PARINACOTA","TARAPACÁ","ANTOFAGASTA","ATACAMA","COQUIMBO","VALPARAÍSO",
            "METROPOLITANA","O'HIGGINS","LIBERTADOR","MAULE","ÑUBLE","BIOBÍO","ARAUCANÍA",
            "LOS RÍOS","LOS LAGOS","AYSEN","AYSÉN","MAGALLANES"]
RUT = re.compile(r'\b\d{1,2}\.\d{3}\.\d{3}-[\dkK]\b')
MAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
CAT  = re.compile(r'\b(PRIMERA|SEGUNDA|TERCERA|ÚNICA|UNICA)\b')
RES  = re.compile(r'\b(\d{1,4})\s+(\d{2}-\d{2}-\d{4})\s*$')
SKIP = ("DEPARTAMENTO DE GESTIÓN","DITEC","NÓMINA DE ENTIDADES","REGIÓN NOMBRE","ACTUALIZADO",
        "PROGRAMAS HABITACIONALES","Página")

text = open("nomina_raw.txt", encoding="utf-8").read()
lines = [l.strip() for l in text.replace("\f","\n").split("\n")]
lines = [l for l in lines if l and not any(l.startswith(s) for s in SKIP)]

def empieza_region(l):
    for r in REGIONES:
        if l.startswith(r + " "):
            return r
    return None

registros, actual = [], None
for l in lines:
    r = empieza_region(l)
    if r:
        if actual: registros.append(actual)
        actual = {"region": r, "texto": l[len(r):].strip()}
    elif actual:
        actual["texto"] += " " + l
if actual: registros.append(actual)

def limpiar(s):
    return re.sub(r'\s{2,}', ' ', s).strip(" -,;")

filas = []
for reg in registros:
    t = reg["texto"]
    m = RUT.search(t)
    if not m:
        continue
    razon = limpiar(t[:m.start()])
    rut = m.group(0)
    resto = t[m.end():]

    correos = MAIL.findall(resto)
    resto_sin_mail = MAIL.sub(" ", resto)

    cat, categoria = CAT.search(resto_sin_mail), ""
    if cat:
        categoria = cat.group(1)
        cuerpo = resto_sin_mail[:cat.start()]
        cola = resto_sin_mail[cat.end():]
    else:
        cuerpo, cola = resto_sin_mail, ""

    res = RES.search(limpiar(cola))
    resolucion = f"{res.group(1)} / {res.group(2)}" if res else limpiar(cola)

    # teléfonos: grupos de 7+ dígitos, admitiendo (56)2, guiones y espacios
    tels = re.findall(r'(?:\(\d{2,3}\)\s*)?\d[\d\s\-]{6,}\d', cuerpo)
    tels = [limpiar(x) for x in tels if len(re.sub(r'\D','',x)) >= 7]
    cuerpo_sin_tel = cuerpo
    for x in tels:
        cuerpo_sin_tel = cuerpo_sin_tel.replace(x, " ")

    filas.append({
        "region": reg["region"],
        "razon_social": razon,
        "rut": rut,
        "contacto_y_direccion": limpiar(cuerpo_sin_tel),
        "telefonos": " / ".join(dict.fromkeys(tels)),
        "correos": " / ".join(dict.fromkeys(correos)),
        "categoria": categoria,
        "resolucion": resolucion,
    })

with open("nomina_ep_completa.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
    w.writeheader(); w.writerows(filas)

rm = [r for r in filas if r["region"] == "METROPOLITANA"]
with open("nomina_ep_rm.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
    w.writeheader(); w.writerows(rm)

print("registros totales:", len(filas), "| RM:", len(rm))
print("RM con correo:", sum(1 for r in rm if r["correos"]), "| con teléfono:", sum(1 for r in rm if r["telefonos"]))
print("\n--- muestra RM ---")
for r in rm[:6]:
    print(f"* {r['razon_social']} | {r['rut']} | tel: {r['telefonos']} | mail: {r['correos']} | cat: {r['categoria']}")
    print(f"    dir: {r['contacto_y_direccion'][:110]}")
