# ejercicio 1 : ordenar cafe para el grupo isc


"""
1-crear una funcion que no tome ningun argumento y devuelva un texto que diga "cafe"
para simular que se esta ordenando un cafe


2-crear una funcion para tomar la orden del cafe que tome un argumento numero_tazas que indica 
cuantas tazas de cafe se quieren ordenar

dentro de las funciones :

-almecena los resultados en una lista llamada  tazas cafe.
-utiliza una lista por comprension para llamar a la funcion preparar_cafe segun el numero_tazas proporcionado.
-finalmente devuelve la lista tazas_cafe

3- llama a la 2da funcion con el numero de tazas que requiere y almacenar en una variable llamada cafe_para_grupo

4- imprime el contenido de cafe_para_grupo es decir la lista de la cadena "cafe"

"""

def ordenar_cafe():
    return "cafe"   

def tomar_orden(numero_tazas):
    tazas_cafe = [ordenar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupo = tomar_orden(10)
print(cafe_para_grupo)


