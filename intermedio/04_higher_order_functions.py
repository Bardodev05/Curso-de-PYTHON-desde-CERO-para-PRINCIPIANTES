#funciones de orden mayor

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

print("------------------")
# closures

def sum_ten(origin_value):
    def add(value):
        return value + 10 + origin_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))
print("------------------")

# built-in funciones de orden superior

numbers = [2,1,3,10,21,3,70]

# map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two,numbers)))
print(list(map(lambda number: number * 2,numbers)))
print("------------------")


# filter

def filter_greater_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_ten, numbers)))
print(list(filter(lambda number: number >10, numbers)))
print("------------------")

# reduce

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values,numbers))