#tuplas
my_other_tupla = ()
my_tupla = tuple()

my_tupla = (35,1.8,"anderson","molina","molina")
my_other_tupla = (32,65,70)

print(my_tupla)
print(type(my_tupla))

print(my_tupla[0])
print(my_tupla[-1])

print(my_tupla.count("molina"))
print(my_tupla.index("molina"))

# las tuplas no se pueden modificar
# my_tupla[1] = 1.85
# print(my_tupla)

my_sum_tuples = my_other_tupla + my_tupla
print(my_sum_tuples)

print(my_sum_tuples[3 : 5])


my_tupla = list(my_tupla)
print(type(my_tupla)) 

my_tupla[4]= "bardo"

print(my_tupla)
print(type(my_tupla)) 

del my_tupla
# print(my_tupla)