"""
TEMA: Condicionales
OBJETIVO: Ejecutar instrucciones diferentes según una condición.
EXPLICACIÓN:
if evalúa una condición; elif permite probar otra y else se ejecuta
cuando ninguna condición anterior se cumple.
"""

calificacion = float(input("Escribe tu calificación (0 a 10): "))

if calificacion < 0 or calificacion > 10:
    print("La calificación debe estar entre 0 y 10.")
elif calificacion >= 6:
    print("Aprobaste.")
else:
    print("Reprobaste.")

# RESULTADO ESPERADO:
# El mensaje depende de la calificación ingresada.
