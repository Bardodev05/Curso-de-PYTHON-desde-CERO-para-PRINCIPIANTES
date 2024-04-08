#variables
my_variable = "my string variables"
print(my_variable)

my_int = 5
print(my_int)

my_bool = False
print(my_bool)

my_int_str = str(my_int)
print(my_int_str)
print(type(my_int_str))

# concatenacion de variables
print(my_variable, my_int, my_bool)
print(f"este es el valor de: {my_int}")

# funciones del sistema
print(len("my string variables"))

# varibles en una sola linea 
name, surname, alias, ege = "ander", "molina", "bardo", 19
print(f"mi nombres es {name},y mi apellido es {surname},me dicen {alias},y tengo {ege} años ")

nombre = input("cuan es tu nombre: ")
edad = input("cual es tu edad: ")

print(f"tu nombre es: {nombre},y tienes {edad} años.")

#¿Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(address)
