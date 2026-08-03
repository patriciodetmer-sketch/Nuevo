import csv, re, collections

SRC="/home/user/Nuevo/inmobiliarias-santiago/entidades_patrocinantes_rm.csv"
OUT="/home/user/Nuevo/inmobiliarias-santiago/merge_ds49_categoria_primera.csv"

CALLE = {"CALLE","AV","AV.","AVDA","AVDA.","AVENIDA","PASAJE","PSJE","PSJE.","CAMINO","DIAGONAL",
         "GENERAL","GRAL","GRAL.","LOS","LAS","EL","LA","SAN","SANTA","PRESIDENTE","PDTE","PDTE.",
         "PADRE","DR","DR.","DOCTOR","NUEVA","NUEVO","RUTA","AUTOPISTA","ALAMEDA","COSTANERA",
         "MANUEL","JOSE","JOSÉ","VICUÑA","ISIDORA","ROSARIO","CERRO","PARQUE","PLAZA","MONSEÑOR",
         "ALONSO","ANDRES","ANDRÉS","APOQUINDO","AMERICO","AMÉRICO","LIBERTADOR","BERNARDO"}

def partir(blob):
    """Separa nombre de contacto y dirección. Heurística: la dirección empieza en la
    primera palabra tipo-calle o, si no hay, después de las primeras 3 palabras."""
    tok = blob.split()
    if not tok:
        return "", ""
    for i, t in enumerate(tok[:7]):
        if i >= 1 and t.upper().strip(".,") in CALLE:
            return " ".join(tok[:i]), " ".join(tok[i:])
    corte = min(3, len(tok))
    return " ".join(tok[:corte]), " ".join(tok[corte:])

filas = [r for r in csv.DictReader(open(SRC, encoding="utf-8")) if r["categoria"] == "PRIMERA"]

por_correo = collections.defaultdict(list)
for r in filas:
    por_correo[r["correo_principal"].lower()].append(r)

out = []
for correo, grupo in por_correo.items():
    r = grupo[0]
    nombre, direccion = partir(r["contacto_y_direccion"])
    tels = r["telefonos"].split(" / ")
    entidad = r["razon_social"].strip()
    corta = r["nombre_corto"].strip() or entidad
    out.append({
        "correo": correo,
        "entidad": entidad,
        "entidad_corta": corta,
        "saludo": f"Estimados {corta}",
        "nombre_contacto_aprox": nombre,
        "rut": r["rut"],
        "direccion_aprox": direccion,
        "comuna": r["comuna"],
        "telefono_1": tels[0] if tels else "",
        "telefonos_todos": r["telefonos"],
        "correos_adicionales": r["correos_adicionales"],
        "categoria": r["categoria"],
        "nota": ("Este correo lo comparten también: " + "; ".join(x["razon_social"] for x in grupo[1:])) if len(grupo) > 1 else "",
    })

out.sort(key=lambda r: r["entidad"])
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

print("destinatarios únicos:", len(out))
print("con nombre de contacto:", sum(1 for r in out if r["nombre_contacto_aprox"]))
print("con comuna:", sum(1 for r in out if r["comuna"]))
print("correos compartidos por 2+ entidades:", sum(1 for r in out if r["nota"]))
print("\n--- muestra ---")
for r in out[:8]:
    print(f"{r['correo']:40} | {r['entidad_corta'][:34]:36} | {r['nombre_contacto_aprox'][:26]:28} | {r['comuna']}")
