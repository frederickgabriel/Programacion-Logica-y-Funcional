# desafio 1 : ordenar hotcake para la familia
# FREDERICK GABRIEL AGUILAR PUC
# objetivo : crear un programa que simule la preparación de piezas de hotcake y ordenar de acuerdo al numero de integrantes en tu familia

""""

1- definir una funcion que no recibe parametros y que devuelva el emoji de hotcake
2- crea una segunda funcion que reciba un argumento numero_piezas, representando la cantidad de piezas de hotcake a preparar, dentro de la funcion: 

-- almacenar el resultado en una lista llamada piezas_hotcake
-- usa una comprension de listas para llamar a la funcion preparar_hotcake tantas veces como el numero indicado en numero_piezas
-- devuelve la lista piezas_hotcake

4- llama a la segunda funcion solicitado al usuario ingresar el numero de integrantes en su familia y almacena el resultado en una variable hotcakes_familia

5- muestra en pantalla el contenido de la variable hotcakes_familia, que sera una lista con varios emojis "🥞"

"""

def preparar_hotcake():
    return "🥞"

def ordenar_hotcake(numero_piezas):
    piezas_hotcake = [preparar_hotcake() for _ in range(numero_piezas)]
    return piezas_hotcake

hotcakes_familia = ordenar_hotcake(int(input("Ingrese el número de integrantes en su familia: ")))
print(hotcakes_familia)

