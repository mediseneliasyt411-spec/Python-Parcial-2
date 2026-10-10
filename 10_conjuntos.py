"""
TEMA: Conjuntos (set)
OBJETIVO: Almacenar elementos únicos y practicar operaciones de conjuntos.
EXPLICACIÓN:
Un conjunto elimina duplicados y no utiliza índices. Puede servir para
unión, intersección y diferencia entre grupos de elementos.
"""

grupo_a = {"Ana", "Luis", "Sofía", "Ana"}
grupo_b = {"Luis", "Carlos", "Paty"}

print("Grupo A sin duplicados:", grupo_a)
print("Unión:", grupo_a | grupo_b)
print("Intersección:", grupo_a & grupo_b)
print("Diferencia A - B:", grupo_a - grupo_b)

grupo_a.add("Elena")
grupo_a.discard("Ana")
print("Grupo A actualizado:", grupo_a)

# RESULTADO ESPERADO:
# Se muestran los elementos únicos y las operaciones entre conjuntos.
