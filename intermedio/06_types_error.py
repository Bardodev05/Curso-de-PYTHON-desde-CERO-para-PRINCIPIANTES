# types error

# sytaxError
# print "¡hola gente!"
print("¡hola gente!")
print("------------------")

# NameError
name = "anderson" #comentar para el error
print(name)
print("------------------")

# IndexError
my_list = ["Python","c#","HTML","CSS","JS"]
print(my_list[0])
print(my_list[3])
print(my_list[-1])
# print(my_list[5]) aca de muestra el IndexError 
print("------------------")

# MoludeNotFoundError
# import maths 
import math
print("------------------")

# AttributeError
# print(math.PI)
print(math.pi)

# KeyError
my_dict = {
    "Nombre": "anderson",
    "apellido": "molina",
    "edad": 10,
    1:"python"
}
print(my_dict["Nombre"])
# print(my_dict["apelldo"])
print(my_dict["apellido"])
print("------------------")

# TypeError
# print(my_list["0"])
print(my_list[0])
print("------------------")

# ImportError
# from math import PI
from math import pi
print(pi)
print("------------------")

# ValueError
my_int = int("10")
# my_int = int("10 años")
print(type(my_dict))
print("------------------")

# ZeroDivisionError
print(4/2)
# print(4/0)
print("------------------")