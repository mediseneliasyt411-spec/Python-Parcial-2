"""
TEMA: Variables y tipos de datos
OBJETIVO: Reconocer cómo se almacenan distintos tipos de información en Python.
EXPLICACIÓN:
Una variable es un nombre asociado a un valor. Algunos tipos básicos son:
str (texto), int (entero), float (decimal) y bool (verdadero/falso).
"""

nombre = "Carlos"       # str: cadena de texto
edad = 18               # int: número entero
estatura = 1.72         # float: número decimal
tiene_identificacion = True  # bool: valor lógico
es_estudiante = False

print("Nombre:", nombre, "| tipo:", type(nombre).__name__)
print("Edad:", edad, "| tipo:", type(edad).__name__)
print("Estatura:", estatura, "| tipo:", type(estatura).__name__)
print("Tiene identificación:", tiene_identificacion,
      "| tipo:", type(tiene_identificacion).__name__)
print("Es estudiante:", es_estudiante)

# RESULTADO:
# Se muestran los valores y los tipos str, int, float y bool.
