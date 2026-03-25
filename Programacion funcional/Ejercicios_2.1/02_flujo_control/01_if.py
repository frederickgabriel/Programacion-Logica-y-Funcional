# Por frederick gabriel aguilar puc 
# 01-senticias (if, else, elif)
# permite ejecutar un bloque de código si se cumple una condición

from os import system

if system("clear") != 0: system("cls")

print("\n sentecia simple condicional")


# podemos usar palabras claves "if" para ejecutar un bloque de código
# solo si se cumple una condición

edad=18

if edad >= 18:
    print("Eres mayor de edad")
    print("felicidades")

# si no cumple la condición no se ejecuta el bloque de código

edad=15 
if edad >= 18 :
    print("Eres mayor de edad")
    print("felicidades")

# podemos usar "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del "if"

print("\n sentencia compuesta condicional")

edad=15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


print("\n sentencia condicional con elif")
# ademas de usar "If" y "else" podemos usar "elif" para determinar multiples condiciones
# ten en cuenta que solo se ejecuta el primer bloque de código que cumpla la condición

nota = 5

if nota >= 9:
    print("sobresaliente")
elif nota >=7 :
    print("notable")
elif nota >= 5:
    print("aprobado")
else :
    print("no esta calificado")



print("\n condiciones multiples ")

edad =16
tiene_carnet = True

# los operadores logicos en python son:
# and : true si ambos operandos son verdaderos
# en javaScript:
# && seria and
# || seria or

# en el caso que sea mayor de edad y tenga carnet
# entonces podras conducir

if edad >= 18 and tiene_carnet:
    print("puedes conducir")
else:
    print("policia!!")

# en un publo de isla de holbox son mas relajados y
# te dejan conducir si eres mayor de edad o tienes carnet

if edad >= 18 or tiene_carnet:
    print("puedes conducir en la isla de holbox")
else:
    print("paga al policia y te dejan pasar!!")


# tambien tenemos el operador logico "not"
# que nos permite negar una condicion

es_fin_de_semana = False

# javaScript -> !
if not es_fin_de_semana:
    print("isc, anda que hay que ir al tec")

# podemos anidar codiciones uno dentro de otro
# para determinar multiples condiciones aunque
# siempre intentaremos evitar esto para simplificar

print("\n anidar condiciones")

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("puedes ir a la discoteca")
    else:
        print("quedate en casa")
else:
    print("no puedes entrar a la discoteca")

# mas facil seria:
# if edad < 18 :
#     print("no puedes entrar a la discoteca")
# elif tiene_dinero:
#     print("puedes ir a la discoteca")
# else:
#     print("quedate en casa")

# ten en cuenta que hay valores que al usarlos como condiciones
# en python son evaluados como vedaderos o falsos
# por ejemplo, el numero 5, es true

numero = 5
if numero:
    print("el numero no es cero")

# pero el numero 0 se evalua como falso
numero = 0
if numero:
    print("aqui no entrara nunca")

# tambien el valor vacio "" se evalua como falso

nombre =""
if nombre:
    print("el nombre no esta vacio")

# ten cuidado con no confundir las asignaciones = con las comparaciones ==!

numero =  3 #asignacion
es_el_tres = numero == 3 #comparacion 

if es_el_tres:
    print("el numero es 3")

# a veces podemos crear condiciones en una sola linea usando
# las ternarias, es una forma concisa de un if-else en una linea de código

print("\n la condicion ternaria:")
#  [codigo si cumple la condicion] if [condicion] else [codigo si no cumple la condicion]

edad=17
mensaje = "es mayor de edad" if edad >= 18 else "es menor de edad"

print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: determiar el mayor de dos numeros 
# pide al usuario que introduzca dos numeros y muestre un mensaje
# indicando cual es mayor o si son iguales

num1= int(input("Introduce el primer numero: "))
num2= int(input("Introduce el segundo numero: "))

if num1 > num2 :
    print(f"el numero {num1} es mayor que {num2}")
elif num2 == num1:
    print("los numeros son iguales")
elif num2 > num1:
    print(f"el numero{num2} es mayor que {num1}")
else:
    print("numero invalido")


#Ejercicio 2: calculo simple 
# Pide al usuario dos numero y una operacion operacion (+,-,*,/)
# Realiza la operacion y muestra el resultado el resultado (maneja la divicion entre zero)

n1=int(input("ingrese el primer numero: "))
n2=int(input("ingrese el segundo numero: "))

operacion=input("ingrese la operacion (+,-,*,/): ")

if operacion == "+":
    print("\n la suma de los numero son :", n1+n2)

elif operacion == "-":
    print("\n la resta de los numero son :", n1-n2)

elif operacion == "*":
    print("\n la multiplicacion de los numero son :", n1*n2)

elif operacion == "/":
    if n2 == 0 or n1 == 0:
        print("\n no se puede dividir entre cero")
    else:
        print("\n la division de los numero son :", n1/n2)
else:
    print("\n operacion invalida")

# Ejercicio 3: año bisiesto 
# pide al usuario que introduzca un año y determina si es bisiesto 
# un año es bisiesto si es divisible por 4 exepto  si se es divisible por 100 pero no por 400

año = int(input("ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")

# Ejercicio 4: categorizar edades
# Pide al usuario que introduzca una edad y clasifique en:

# -Bebe (0-2 años)
# -Niño (3-12 años)
# -Adolescente (13-17 años)
# -Adulto (18-64 años)
# -Adulto mayor (65 años o mas)

Edad = int (input("ingrese su edad: "))

if Edad >= 0 and Edad <= 2:
    print("eres un bebe")
elif Edad >= 3 and Edad <= 12 :
    print("eres un niño")
elif Edad >= 13 and Edad <= 17 :
    print("eres un adolescente")
elif Edad >=18 and Edad <= 64 :
    print("eres un adulto")
elif Edad >= 65 :
    print("eres un adulto mayor")
else:
    print("edad invalida")

