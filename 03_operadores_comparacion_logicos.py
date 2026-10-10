"""
TEMA: Operadores de comparación y lógicos
OBJETIVO: Comparar valores y combinar condiciones.
EXPLICACIÓN:
Las comparaciones devuelven True o False. Los operadores lógicos son
and (ambas condiciones), or (al menos una) y not (niega la condición).
"""

edad = 18
tiene_identificacion = True
es_estudiante = False

print("¿Es mayor o igual a 18?", edad >= 18)
print("¿Es exactamente 18?", edad == 18)
print("¿Es distinto de 20?", edad != 20)

if edad >= 18 and tiene_identificacion:
    print("Cumple ambas condiciones")

if edad >= 18 or es_estudiante:
    print("Cumple al menos una condición")

if not es_estudiante:
    print("No es estudiante")

# RESULTADO ESPERADO:
# Se muestran resultados booleanos y mensajes según las condiciones.
