print("-----------------------------EJERCICIOS (while)-------------------------------------------")
# POR FREDERICK GABRIEL AGUILAR PUC 
###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

contador = 10

while contador >= 1:
    print(contador)
    contador -= 1


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

numero = 1
suma = 0

while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print("Suma de pares:", suma)


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.

num = int(input("Introduce un número positivo: "))
factorial = 1

contador = 1
while contador <= num:
    factorial *= contador
    contador += 1

print("Factorial:", factorial)


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while hasta que cumpla con el requisito.

password = input("Introduce una contraseña: ")

while len(password) < 8:
    print("Contraseña muy corta, intenta de nuevo.")
    password = input("Introduce una contraseña: ")

print("Contraseña válida")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime su tabla de multiplicar del 1 al 10 usando while.

num = int(input("Introduce un número: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario un número N.
# Imprime todos los números primos menores o iguales que N.

n = int(input("Introduce un número N: "))
num = 2

while num <= n:
    es_primo = True
    divisor = 2

    while divisor < num:
        if num % divisor == 0:
            es_primo = False
            break
        divisor += 1

    if es_primo:
        print(num)

    num += 1

print("-------------------------------Ejercicios Bucle For-----------------------------------------")

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

for numero in range(2, 21, 2):
    print(numero)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

numeros = [10, 20, 30, 40, 50]
suma = 0

for num in numeros:
    suma += num

media = suma / len(numeros)
print("Media:", media)


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]

for num in numeros:
    if num > maximo:
        maximo = num

print("Máximo:", maximo)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

# Con for
resultado = []
for palabra in palabras:
    if len(palabra) > 5:
        resultado.append(palabra)

print("Palabras con más de 5 letras (for):", resultado)

# Con list comprehension
resultado2 = [p for p in palabras if len(p) > 5]
print("Palabras con más de 5 letras (list comprehension):", resultado2)


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra = input("Introduce una letra: ").lower()

contador = 0

for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1

print("Cantidad de palabras que empiezan con", letra, ":", contador)