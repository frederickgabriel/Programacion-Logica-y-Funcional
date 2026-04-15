from os import system

if system("clear") != 0: system("cls")

print("\n Bucle while")

contador = 0

while contador <=5:
    print(contador)
    contador +=1


# --------------

print("\n bucle while con break")

contador = 0

while True:
    print(contador)
    contador +=1
    if contador == 5:
        break

# --------------


print("\n bucle while con continue")

contador=0
while contador <10:
    contador +=1

    if contador % 2 == 0:
        continue
    print(contador)

# --------------

print("\n bucle while con else")

contador = 0 
while contador <5:
    print(contador)
    contador +=1
else:
    print("El bucle while ha terminado")

# -----------

numero = -1

while numero <0:
    numero = int(input("Ingrese un numero positivo: "))
    if numero <0:
        print("El numero ingresado es negativo, intente de nuevo")
print(f"El numero ingresado es: {numero}")



# -----------

numero = -1
while numero <0:
    try:
        numero = int(input("Ingrese un numero positivo: "))
        if numero <0:
            print("El numero ingresado es negativo, intente de nuevo")
    except :
        print("lo que introduces debe ser un numero , que si no peta")
print(f"El numero ingresado es: {numero}")


# ejercicio while

