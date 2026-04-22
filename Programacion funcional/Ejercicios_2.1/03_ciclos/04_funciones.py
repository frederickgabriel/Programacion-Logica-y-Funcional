from os import system

if system("clear") != 0: system("cls")

# definicion de funciones


def saludo():
    print("Hola")

def saludo_a(nombre):
    print(f"Hola {nombre}")

saludo_a("estudiante")
saludo_a("jefa")
saludo_a("profesor")

# funciones con mas parametros

def suma (a, b):
    suma = a + b
    return suma

resultado = suma(5, 10)
print(resultado)

# documentar las funciones con docstrings

def resta (a, b):
    """Esta funcion resta dos numeros y devuelve el resultado"""
    return a - b

# parametros por defecto

def multiplicar (a,b=2):
    return a*b

print (multiplicar(2))
print(multiplicar(2,3))


# argumentos por posicion 

def describir_persona(nombre: str, edad: int,sexo: str):
    print(f"soy {nombre} y tengo {edad} años y me identifico como {sexo}")


# parametros son pocisionales

describir_persona(1, 20, "femenino")
describir_persona("carlos", 25, "masculino")
describir_persona("persona", "ingeniero", 30)

# argumentos por clave
# parametros nombrados

describir_persona(sexo="perro", nombre="reyes", edad=30)
describir_persona(sexo="mujer", nombre="alejandra", edad=21)

# argumentos de longitud variable
