"""
TEMA: Diccionarios: pares clave-valor
OBJETIVO: Organizar datos mediante claves que apuntan a valores.
EXPLICACIÓN:
Los diccionarios guardan pares clave-valor. Se consulta un valor mediante
su clave y se puede agregar, modificar o eliminar información.
"""

alumno = {
    "nombre": "Mariana",
    "edad": 20,
    "calificacion": 8.7
}

print("Nombre:", alumno["nombre"])
print("Edad:", alumno["edad"])

alumno["grupo"] = "A"                 # Agregar una clave nueva
alumno["calificacion"] = 9.0          # Modificar un valor
print("Datos completos:", alumno)

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

alumno.pop("edad")
print("Después de eliminar edad:", alumno)

# RESULTADO ESPERADO:
# Se muestran los datos del diccionario antes y después de modificarlo.
