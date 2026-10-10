"""
TEMA: break y continue
OBJETIVO: Controlar el comportamiento de un ciclo.
EXPLICACIÓN:
break termina el ciclo inmediatamente. continue omite el resto de la
iteración actual y pasa a la siguiente.
"""

print("Ejemplo de break:")
for numero in range(1, 8):
    if numero == 5:
        break
    print(numero)

print("Ejemplo de continue (omite el 3):")
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

# RESULTADO ESPERADO:
# break imprime del 1 al 4; continue imprime 1, 2, 4 y 5.
