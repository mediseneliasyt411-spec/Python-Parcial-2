"""
TEMA: Listas y operaciones con listas
OBJETIVO: Crear, consultar, modificar, ordenar y recorrer listas.
EXPLICACIÓN:
Las listas son colecciones ordenadas y modificables. Los índices empiezan
en cero. append agrega al final, insert agrega en una posición, remove
elimina por valor, pop elimina por índice y len cuenta elementos.
"""

alumnos = ["Ana", "Luis", "Paty"]
calificaciones = [8.5, 7.0, 9.2, 6.5, 8.0]

print("Primer alumno:", alumnos[0])
print("Último alumno:", alumnos[-1])

alumnos.append("Carlos")
alumnos.insert(1, "Sofía")
alumnos.remove("Luis")
print("Alumnos:", alumnos)
print("Cantidad:", len(alumnos))

print("Máxima:", max(calificaciones))
print("Mínima:", min(calificaciones))
print("Suma:", sum(calificaciones))
promedio = sum(calificaciones) / len(calificaciones)
print("Promedio:", round(promedio, 2))

calificaciones.sort()
print("Ascendente:", calificaciones)
calificaciones.sort(reverse=True)
print("Descendente:", calificaciones)
print("Primeras tres:", calificaciones[:3])

aprobados = [c for c in calificaciones if c >= 6]
print("Aprobados:", aprobados)

# RESULTADO ESPERADO:
# Se muestran accesos, modificaciones, operaciones y filtros de listas.
