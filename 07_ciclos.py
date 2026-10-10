"""
TEMA: Ciclos for y while
OBJETIVO: Repetir instrucciones.
EXPLICACIÓN:
for recorre elementos de una colección o rango. while repite mientras
su condición sea verdadera.
"""

print("Conteo con for:")
for numero in range(1, 6):
    print(numero)

print("Conteo con while:")
contador = 1
while contador <= 3:
    print(contador)
    contador += 1

# RESULTADO ESPERADO:
# El primer ciclo imprime del 1 al 5 y el segundo del 1 al 3.
