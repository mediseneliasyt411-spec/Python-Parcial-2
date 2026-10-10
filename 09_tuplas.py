"""
TEMA: Tuplas
OBJETIVO: Guardar varios elementos en una colección ordenada e inmutable.
EXPLICACIÓN:
Las tuplas permiten índices y valores duplicados, pero no se modifican
directamente. Una tupla de un elemento necesita una coma.
"""

tecnologias = ("Python", "JavaScript", "Go")
print(tecnologias)
print(type(tecnologias).__name__)
print("Segundo elemento:", tecnologias[1])

una_tupla = ("manzana",)
print("Tupla de un elemento:", type(una_tupla).__name__)

periodo = ("Agosto", "Diciembre", 2026)
inicio, fin, anio = periodo
print(inicio)
print(fin)
print(anio)

# Para cambiar elementos se puede convertir temporalmente a lista.
lista_temporal = list(tecnologias)
lista_temporal.append("ReactJS")
tecnologias = tuple(lista_temporal)
print("Tupla actualizada:", tecnologias)

# RESULTADO ESPERADO:
# Se imprimen los elementos y se demuestra el desempaquetado.
