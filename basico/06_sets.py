# sets
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"ander","molina",19}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("bardo")
print(my_other_set)

my_other_set.add("andy")
print(my_other_set)

print("ander" in my_other_set)
print("anderson" in my_other_set)

my_other_set.remove("ander")
print(my_other_set)

my_other_set.clear() #vacio
print(len(my_other_set))

del my_other_set #elimina todo
print(my_other_set)

my_set = {"ander", "Molina", 15}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))