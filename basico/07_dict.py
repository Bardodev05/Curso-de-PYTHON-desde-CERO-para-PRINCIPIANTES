#diccionario
my_dict = dict()
my_other_dict = {}

print(type(my_other_dict))
print(type(my_dict))

my_other_dict = {
    "Nombre": "anderson",
    "apellido": "molina",
    "edad": 10,
    1:"python"
}
my_dict = {
    "Nombre": "ander",
    "apellido": "molina",
    "edad": 10,
    "lenguajes": {"python","js"},
    1:1.81
}
print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["apellido"])

my_dict["edad"] = 45
print(my_dict["edad"])

print(my_dict[1])

my_dict["calle"] = "calle de ander"
print(my_dict)

del my_dict["calle"]
print(my_dict)


print("Nombre" in my_dict)
print("anders" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_list = ["nombre",1, "piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("nombre",1,"piso"))
print((my_new_dict))

my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,"molinas")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))