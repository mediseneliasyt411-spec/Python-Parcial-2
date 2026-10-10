"""
TEMA: Conversión de tipos (casting)
OBJETIVO: Convertir valores de un tipo a otro.
EXPLICACIÓN:
int() convierte a entero, float() a decimal, str() a texto y round()
redondea un número decimal a la cantidad de posiciones indicada.
"""

numero_texto = "42"
numero_entero = int(numero_texto)
numero_decimal = float(numero_texto)

print(numero_entero)   # 42
print(numero_decimal)  # 42.0

edad = 25
texto = str(edad)
print(texto, type(texto).__name__)  # 25 str

pi = 3.14159
print(round(pi, 2))  # 3.14

# RESULTADO ESPERADO:
# Se muestran conversiones y el número pi redondeado a dos decimales.
