# 03 casting de types
# transformar un tipo de un valor a otro

from os import system
if system('clear') != 0: system('cls')

print("conversion de tipos")

# convertir una cadena que contiene un numero a un entero y sumarlo con otro entero 
print(int("100")+2) #convertir "100" a entero y suma 2, resultado 102

# convertir un entero a cadena para concatenarlo con otra cadena

print("100" + str(2)) #convertir el numero 2 a cadena y concatena, resultado 1002

# convertir una cadena con un numero decimal a tipo float
print(type(float("3.1416"))) #convierte 3.1416 a float y muestar su tipo , resultado <class

# convertir un numero decimal a entero (se trunca la parte decimal)
print(int(3.1416))

# Evaluar valores numericos como booleanos
print(bool(3)) #cualquier numero distinto de 0 es true resultado true
print(bool(0)) #0 es false 
print(bool(-1)) #cualquier numero negativo -1 es true resultado


# Evaluar cadenas como booleanos

print(bool("")) # una cadena vacia es false 
print(bool(" ")) # una cadena con espacio es true 
print(bool("False")) # una cadena con texto aun que sea false es true


# Redondear un numero unico
print(round(2.51)) #redondea 2.51 al entero mas cercano resulatdo:3

# este genera un error y se comenta para evitar conflicto en la ejecucion 
# print(int("hola mundo")) esto generaria un ValueError porque "hola mundo" no es num



