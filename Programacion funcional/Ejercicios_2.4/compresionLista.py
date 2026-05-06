numeros = [1, 2, 3, 4,5,6,7,8,9,10]

doble = []

for n in numeros:
    doble.append(n * 2)

print(doble)

# genera otra lista de los cuadrados de los numeros

cuadrados = [num ** 2 for num in numeros]

lista_cuadruple= list(map(lambda x: x * 4, numeros))
print(lista_cuadruple)

# genera otra lista de los cubos de los numeros
cubos = [elemento ** 3 for elemento in numeros]

cadena = ["hola" + "que hace" for _ in range(3)]

# genera una lista de cadenas para cada elemento del rango de 5

saludos = ["hola" for _ in range(5)]
saludos2=["que hace" for _ in range(5)]