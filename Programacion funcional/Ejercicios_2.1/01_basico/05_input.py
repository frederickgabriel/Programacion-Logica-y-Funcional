from os import system
if system('clear') != 0: system('cls')

#################
nombre = input("hola ¿como llamas?\n")
print(f"hola {nombre}, encantado de conocerte")

################

age = input("¿cuantos años tines? : \n")

age= int(age)

print(f"Tines {age} años")

################

print("obtener multiples valores a la vez")

country, city = input("¿en que pais y ciudad vives?\n").split()

print(f"vives en {country}, {city}")

################

