# =============================================================================
# Ejercicio 2: Ordenar tipo de café
# Objetivo : Ordenar distintos tipos de café
#
# Los grupos de VIII de ISC tienen cambios de humor y ahora cada grupo quiere 
# un tipo de café:
# —café americano y
# —café de olla.
#
# ****Dato curioso: Los cambios de humor de mis alumnos son bastante frecuentes.
#
# Con esta información, tendremos que revisar la función ordenar café del 
# ejercicio anterior para agregar la variedad de café.
#
# Debemos modificar ordenar_cafe para que acepte una función como parámetro 
# y así poder cambiar el tipo de café que se va a preparar.
#
# Esto hace que obtener_cafe sea más flexible y ofrece al programador mayor 
# control cuando cambian las solicitudes del cliente.
#
# 1.- Crea una función preparar_cafe que no recibe parámetros y devuelve una 
#     cadena que representa una taza de café americano.
# 2.- Crea otra esta función devuelve una cadena que representa una taza de 
#     café olla.
# 3.- Crea otra función ordenar_cafe que acepta dos parámetros: una función 
#     que prepara café y numero de tazas.
# 4.- Dentro de la función ordenar crea una lista que guarde las tazas de café.
# 5.- Dentro de la función ordenar, aplica la iteración a través de la lista 
#     por comprensión para llamar a la función preparar_cafe según el 
#     numero_tazas proporcionado.
# 6.- Finalmente en la función ordenar, devuelve la lista tazas_cafe.
# 5.- Crear una variable cafe para el grupo A que recibe el numero de tazas 
#     que prefieren el sabor americano.
# 6.- Crear una variable cafe para el grupo B que recibe el numero de tazas 
#     que prefieren el sabor de olla.
# 7.- Imprimir en una sola línea ambas ordenes
# 
# =============================================================================


def preparar_americano():
    return "café_americano"

def preparar_olla():
    return "café_olla"

def ordenar_cafe(preparar, numero_tazas):
    tazas_tazas = [preparar() for _ in range(numero_tazas)]
    return tazas_tazas

cafe_grupo_a=ordenar_cafe(preparar_americano, 10)
cafe_grupo_b=ordenar_cafe(preparar_olla, 12)

print(cafe_grupo_a,cafe_grupo_b)

