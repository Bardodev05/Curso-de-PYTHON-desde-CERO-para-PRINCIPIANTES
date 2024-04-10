# restos 

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

# def fizzbuzz():
#     for index in range(1,101):
#         print(index)
#         if index % 3 == 0 and index % 5 ==0 :
#             print("fizzbuzz")
#         elif index % 3 == 0:
#             print("fizz")
#         elif index % 5 == 0:
#             print("buzz")
#         else:
#             print(index)
# fizzbuzz()

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

# fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagrama(word_one, word_two):
    # Convertir las palabras a minúsculas
    word_one = word_one.lower()
    word_two = word_two.lower()
    
    # Verificar si las palabras son idénticas
    if word_one == word_two:
        return False
    
    # Verificar si las palabras tienen la misma longitud
    if len(word_one) != len(word_two):
        return False
    
    # Comparar las listas ordenadas de letras de las palabras
    return sorted(word_one) == sorted(word_two)

# print(is_anagrama("amor", "roma"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    
    prev = 0
    next = 1
    
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
# fibonacci() 

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)
# is_prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def revese(texto):
    texto_len = len(texto)
    reversed_text = " "
    for i in range(0,texto_len):
        reversed_text += texto[texto_len - i -1]
    return reversed_text

print(revese("hola mundo"))