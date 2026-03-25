# Por frederick gabriel aguilar puc 
# 02 booleanos 
# valores logicos : true (verdadero) y false (falso)
# Fundamentales para el control de flujo y la logica en programacion 

from os import system

if system("clear") != 0: system("cls")

# Los booleanos representan valores de verdad : true o false 

print("\n valores booleanos basicos")

print(True)
print(False)

# operadores de comparacion : devuelve un valor booleano 

print("\n operadores de comparacion")

print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

print("\nComparación de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera")  # True
print("'Hola' == 'hola':", "Hola" == "hola")      # False


# Operadores lógicos: and, or, not
print("\n Operadores lógicos:")
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("True or False:", True or False)     # True
print("False or False:", False or False)   # False
print("not True:", not True)               # False
print("not False:", not False)             # True


# Tablas de verdad (para referencia):
print("\n Tablas de verdad:")

print("\n and:")
print("A     B     A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

print("\n not:")
print("A     not A")
print("True  ", not True)
print("False ", not False)

