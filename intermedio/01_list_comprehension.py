# Lista original
my_list_origin = [0,1,2,3,4,5,6,7,8,9]
print(my_list_origin)

# Crear un rango y convertirlo a lista
my_range = range(8)
print(list(my_range))

# Crear una lista usando comprensión de lista que agrega 1 a cada elemento del rango
my_list = [i + 1 for i in range(7)]
print(my_list)

# Crear una lista usando comprensión de lista que multiplica cada elemento del rango por 2
my_list = [i * 2 for i in range(7)]
print(my_list)

# Crear una lista usando comprensión de lista que eleva al cuadrado cada elemento del rango
my_list = [i * i for i in range(7)]
print(my_list)

# Definir una función que suma 5 al número dado
def sum_five(number):
    return number + 5

# Crear una lista usando comprensión de lista que aplica la función sum_five a cada elemento del rango
my_list = [sum_five(i) for i in range(8)]
print(my_list)
