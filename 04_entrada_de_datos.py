"""
TEMA: Entrada de datos
OBJETIVO: Capturar información escrita por el usuario.
EXPLICACIÓN:
input() pausa el programa y devuelve lo escrito como texto (str).
Si se necesita operar con números, hay que convertir la respuesta.
"""

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))

print("Hola,", nombre)
print(f"En 5 años tendrás {edad + 5}")

# RESULTADO ESPERADO:
# El programa saluda al usuario y calcula su edad dentro de cinco años.
