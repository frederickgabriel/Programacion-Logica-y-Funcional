# =============================================================================
#  ACTIVIDAD PRÁCTICA INTEGRADORA
#  Sistema de pedidos: Comedor Escolar
# =============================================================================
#  Programación Funcional en Python — Nivel Básico
#  Temas integrados:
#    ✅ Funciones simples y de primera clase  
#    ✅ Comprensión de listas                 
#    ✅ Funciones de orden superior           
#    ✅ Callbacks                             
#    ✅ Funciones lambda + map()              
#    ✅ Lógica condicional dentro de funcs.   
#    ✅ Entrada del usuario                   
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
#  Sección 1 — INVESTIGA
# ─────────────────────────────────────────────────────────────────────────────
# Antes de comenzar a codificar, investiga y responde en comentarios:
#
# 1. ¿Qué es una función de primera clase en Python?
#    R: Una función que puede tratarse como cualquier otro objeto
#
# 2. ¿Cuál es la diferencia entre una función de orden superior y un callback?
#    R: La de orden superior es la que recibe a otra función.
#       El callback es la función que le pasas a esa función para que la use.
#
# 3. ¿Cuándo conviene usar comprensión de listas en lugar de un ciclo for?
#    R: Cuando solo quieres crear una lista nueva en una sola línea simple.
#       Si la lógica es más complicada, mejor usa un for normal.
#
# 4. ¿Qué hace map() y cómo se relaciona con lambda?
#    R: aplica la misma operación a todos los elementos de una lista.
#       Lambda es la instrucción rápida que le dices que use, sin crear
#       una función aparte con def.
#
# 5. ¿Qué ventaja ofrece pasar una función como argumento a otra función?
#    R: Que no repites código una sola función tomar_orden() sirve para
#       pizza, agua y tamal, solo cambiando el argumento que le pasas.

# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Sección 2 — PLANEA
# ─────────────────────────────────────────────────────────────────────────────
# Lee el siguiente escenario y diseña tu solución ANTES de codificar.
#
# ESCENARIO
# La cooperativa escolar ofrece tres productos en su menú:
#   🍕 Pizza  |  🥤 Agua fresca  |  🫔 Tamal
#
# El sistema debe:
#   A) Preparar cualquier producto usando una función dedicada por producto.
#   B) Tomar la orden de un grupo: recibir la FUNCIÓN del producto y la
#      CANTIDAD solicitada, y devolver una lista con todas las porciones.
#   C) Calcular el precio total aplicando el precio unitario a cada porción  
#      usando map() y una función lambda.
#   D) Aplicar una PROMOCIÓN: si el pedido es de 3 o más porciones,
#      agregar "🎁 postre gratis" a la orden.
#   E) Solicitar al usuario cuántas porciones desea de cada producto y
#      mostrar el resumen completo del pedido.
#
# Antes de codificar respone o describe:
#      - ¿Qué funciones necesitas definir?
#        Cuatro funciones:
#       - preparar_pizza(), preparar_agua(), preparar_tamal() para cada producto.
#       - calcular_promocion() para revisar si aplica el postre gratis.
#       - tomar_orden() para juntar todo: porciones, precios y promoción.

#      - ¿Cuál de ellas es de orden superior? ¿Por qué?
#        tomar_orden() porque recibe como argumento la función del producto
#       (preparar_pizza, preparar_agua o preparar_tamal) y la llama adentro.

#      - ¿Dónde usarás comprensión de listas?
#        Dentro de tomar_orden() para generar la lista de porciones.
#      - ¿Dónde usarás lambda + map()?
#       Dentro de tomar_orden() para generar la lista de precios.
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Sección 3 — CODIFICA
# ─────────────────────────────────────────────────────────────────────────────
# Completa cada paso en el orden indicado.
# Puedes apoyarte en los archivos del carpeta para recordar la sintaxis.


# ── PASO 1 ──────────────────────────────────────────────────────────────────
# Define tres funciones simples, sin parámetros, que devuelvan el nombre
# (y emoji) del producto correspondiente. Son funciones de primera clase.
#
# Referencia: ejercicio1_cafe.py → preparar_cafe()
#             desafio2_alimentos.py → preparar_pizza(), preparar_hamburguesa()

def preparar_pizza():
    return "🍕 Pizza"

def preparar_agua():
    return "🥤 Agua fresca"

def preparar_tamal(): 
    return "🫔 Tamal"


# ── PASO 2 ──────────────────────────────────────────────────────────────────
# Define la función calcular_promocion(cantidad).
# Si cantidad >= 3, devuelve el string "🎁 postre gratis".
# En caso contrario, devuelve un string vacío "".
#
# Referencia: desafio2_alimentos.py → calcular_bonus()

def calcular_promocion(cantidad):
    if cantidad >= 3:
        return "🎁 postre gratis"
    else:
        return ""


# ── PASO 3 ──────────────────────────────────────────────────────────────────
# Define la función tomar_orden(preparar_alimento, cantidad, precio_unitario).
#
# Esta función es de ORDEN SUPERIOR porque recibe otra función como argumento.
# preparar_alimento → función que se usará como callback (pizza, agua o tamal)
# cantidad          → número de porciones
# precio_unitario   → costo por porción (número)
#
# Dentro de la función debes:
#   a) Usar COMPRENSIÓN DE LISTAS para generar la lista de porciones,
#      llamando a preparar_alimento() en cada iteración.
#   b) Usar map() con una función LAMBDA para calcular el precio de cada
#      porción: cada elemento de la lista recibe el precio_unitario.
#      Convierte el resultado en lista con list().
#   c) Llamar a calcular_promocion(cantidad) y guardar el resultado.
#   d) Devolver una tupla: (porciones, precios, promocion)
#
# Referencia: ejercicio2_tipoCafe.py → ordenar_cafe()
#             desafio2_alimentos.py  → ordenar_alimento()
#             compresionListas.py    → map + lambda
#             funciones.py           → callbacks y orden superior

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    # a) Comprensión de listas
    porciones = [preparar_alimento() for _ in range(cantidad)]          # ← reemplaza con list comprehension

    # b) map() + lambda para precios
    precios = list(map(lambda p: precio_unitario, porciones))            # ← reemplaza con list(map(lambda ..., porciones))

    # c) Promoción
    promocion = calcular_promocion(cantidad)          # ← llama a calcular_promocion(cantidad)

    # d) Devuelve los tres valores
    return porciones, precios, promocion





# # ── DESAFÍO EXTRA 2 — Función de orden superior que devuelve funciones ───────

# def elegir_producto(nombre):
#     if nombre == "pizza":
#         return preparar_pizza       # devuelve la función, sin ejecutarla
#     elif nombre == "agua":
#         return preparar_agua
#     elif nombre == "tamal":
#         return preparar_tamal
#     else:
#         return None







# ── PASO 4 ──────────────────────────────────────────────────────────────────
# Solicita al usuario la cantidad de cada producto y toma las órdenes.
# Almacena cada resultado en una variable distinta.
#
# Referencia: desafio1_hotcake.py → input() + int()

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))

# Llama a tomar_orden para cada producto.
# Precios sugeridos: pizza=25, agua=10, tamal=15
orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)


# ── PASO 5 ──────────────────────────────────────────────────────────────────
# Muestra el resumen del pedido.
# Para cada orden imprime: porciones, precios y promoción (si aplica).
#
# Ejemplo de salida esperada:
#   🍕 PIZZAS   → ['🍕 pizza', '🍕 pizza', '🍕 pizza']
#   💲 Precios  → [25, 25, 25]
#   🎁 Promo    → 🎁 postre gratis
#
# Referencia: solucionAlimentos.py → print de tupla

print("\n========== RESUMEN DEL PEDIDO ==========")
# Desempaqueta cada tupla en sus tres partes y muéstralas
porciones_pizza,  precios_pizza,  promo_pizza  = orden_pizza
porciones_agua,   precios_agua,   promo_agua   = orden_agua
porciones_tamal,  precios_tamal,  promo_tamal  = orden_tamal

print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")

print("\n========================================")


# ─────────────────────────────────────────────────────────────────────────────
# Sección 4 — PRUEBA
# ─────────────────────────────────────────────────────────────────────────────
# Ejecuta el programa con los siguientes casos y verifica los resultados.
#
# CASO 1 — Sin promoción (cantidades menores a 3):
#   Pizzas: 2  | Aguas: 1  | Tamales: 2
#   Esperado: ninguna orden muestra "🎁 postre gratis"
#
# CASO 2 — Con promoción en todas las órdenes:
#   Pizzas: 3  | Aguas: 5  | Tamales: 4
#   Esperado: las tres órdenes muestran "🎁 postre gratis"
#
# CASO 3 — Promoción mixta:
#   Pizzas: 1  | Aguas: 3  | Tamales: 2
#   Esperado: solo la orden de aguas muestra "🎁 postre gratis"
#
# CASO 4 — Verificación de precios con map() + lambda:
#   Pide 3 pizzas a $25 c/u → la lista de precios debe ser [25, 25, 25]
#   Pide 4 tamales a $15 c/u → la lista de precios debe ser [15, 15, 15, 15]
#
# Registra:
#   - ¿El resultado coincide con lo esperado? ✅ / ❌
#    R: si los resultados coinciden con cada uno de los casos
#   - Si no coincide, ¿en qué función está el error?
#    R: en tomar_orden()
#   - ¿Qué cambiarías para corregirlo?
#   R: revisar la lógica de cada paso dentro de tomar_orden() y verificar
# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Desafío extra (opcional)
# ─────────────────────────────────────────────────────────────────────────────
# Si terminaste antes y quieres ir más allá:
#
# 1. Usa sum() y map() + lambda para calcular el TOTAL a pagar de cada orden.
# 2. Crea una función elegir_producto(nombre) que sea de ORDEN SUPERIOR:
#    recibe un string ("pizza", "agua" o "tamal") y DEVUELVE la función
#    de preparación correspondiente (sin ejecutarla).
#    Referencia: funciones.py → elegir_operacion()
# 3. Usa la función del punto 2 para reemplazar los argumentos directos en
#    las llamadas a tomar_orden().
# ─────────────────────────────────────────────────────────────────────────────


total_pizza  = sum(map(lambda p: p, precios_pizza))
total_agua   = sum(map(lambda p: p, precios_agua))
total_tamal  = sum(map(lambda p: p, precios_tamal))
gran_total   = total_pizza + total_agua + total_tamal

print(f"\n💰 Total pizzas  → ${total_pizza}")
print(f"💰 Total aguas   → ${total_agua}")
print(f"💰 Total tamales → ${total_tamal}")
print(f"\n🧾 TOTAL A PAGAR → ${gran_total}")

print("\n========================================")