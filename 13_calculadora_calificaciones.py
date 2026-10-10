"""
PRÁCTICA FINAL: Calculadora simple de calificaciones
OBJETIVO:
Pedir el nombre de un estudiante y tres calificaciones, convertir cada
calificación a float, guardarlas en una colección, calcular el promedio,
mostrar los datos e indicar si aprobó (promedio >= 6.0) o reprobó.
"""

nombre = input("Nombre del estudiante: ")

# Se usa una lista porque permite guardar las tres calificaciones en orden.
calificaciones = [
    float(input("Primera calificación: ")),
    float(input("Segunda calificación: ")),
    float(input("Tercera calificación: "))
]

promedio = sum(calificaciones) / len(calificaciones)

print("\n--- REPORTE DE CALIFICACIONES ---")
print("Estudiante:", nombre)
print("Calificaciones:", calificaciones)
print(f"Promedio: {promedio:.2f}")

if promedio >= 6.0:
    print("Resultado: APROBÓ")
else:
    print("Resultado: REPROBÓ")

# RESULTADO ESPERADO:
# Se presenta un reporte con el nombre, las tres calificaciones,
# el promedio y el resultado académico.
