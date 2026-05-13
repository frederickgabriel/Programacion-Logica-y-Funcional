"""
FREDERICK GABRIEL AGUILAR PUC 
#Desafio 2
'''
Usando la lógica del ejercicio 2, realiza lo siguiente:
1.- Define funciones para preparar cada tipo de alimento: pizza, hamburguesa y hotdog.
2.- Crea una función ordenar_alimento que reciba como argumentos a la función preparar_alimento y número de porciones.
3.- Dentro de la función ordenar crea una lista que guarde las porciones de alimentos.
4.- Dentro de la función ordenar, aplica la iteración a través de la lista por comprensión para llamar a la función preparar_alimento según el número de porciones proporcionado.
5.- Finalmente en la función ordenar, devuelve la lista porciones_alimentos.
6.- Cada grupo debe utilizar esta función para ordenar su selección de alimento y mostrar el resultado.
7.- Prueba imprimir las órdenes
8.- Crea una función que permita calcular bonus para los grupos que recibe el número de porciones.
9.- Compara si el número de porciones es mayor a 2, si es así, retorna "coca gratis", sino retorna vacío.
Muestra el bonus en la orden de cada grupo.
10.- Modifica la función ordenar_alimento para usar la función calcular_bonus y guardar el resultado en una variable bonus.
11.- Agregar en la devolución el resultado de las órdenes con el bonus.
'''



"""

def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"


def ordenar_alimento(preparar_alimento, porciones):
    porciones_alimentos = [preparar_alimento() for _ in range(porciones)]
    bonus = calcular_bonus(porciones)
    return porciones_alimentos , bonus


def calcular_bonus(porciones):
    return "Coca-Cola Gratis" if porciones > 2 else ""


ham = ordenar_alimento(preparar_hamburguesa, 2)
piz = ordenar_alimento(preparar_pizza, 1)
hot = ordenar_alimento(preparar_hotdog, 3)

print(ham,piz,hot)
