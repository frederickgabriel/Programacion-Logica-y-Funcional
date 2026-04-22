from os import system

if system("clear") != 0: system("cls")


print ("n\ range ():")


# genera una secuencia de números del 0 al 9

for num in range (10):
    print(num)


# ragen (inicio, fin) 

for num in range (5, 10):
    print(num)

# range (inicio, fin, paso)

for num in range (0, 100, 5):
    print(num)

for num in range (-5,0):
    print(num)

for num in range (10, 0, -1):
    print(num)

for num in range (0,444):
    print(num)

nums = range (10)
list_of_nums = list (nums)
print (list_of_nums)

# serie para hacerlo cinco veces 

for _ in range(5):
    print("hacer 5 veces algo")

# ejercicios (range)

