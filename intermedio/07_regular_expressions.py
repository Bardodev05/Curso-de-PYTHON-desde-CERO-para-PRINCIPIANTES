### Regular Expressions ###

import re

# match
print("---------------- MATCH ----------------")
my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# Busca un patrón al principio de la cadena
match = re.match("Esta es la lección", my_string, re.I)
print(match)
if match is not None:
    start, end = match.span()
    print(my_string[start:end])

# No hay coincidencia al principio de la cadena
match = re.match("Esta no es la lección", my_other_string)
if match is not None:
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search
print("---------------- SEARCH ----------------")
# Busca un patrón en toda la cadena
search = re.search("lección", my_string, re.I)
print(search)
if search is not None:
    start, end = search.span()
    print(my_string[start:end])

# findall
print("---------------- FINDALL ----------------")
# Encuentra todas las ocurrencias de un patrón en la cadena
findall = re.findall("lección", my_string, re.I)
print(findall)

# split
print("---------------- SPLIT ----------------")
# Divide la cadena en función de un patrón y devuelve una lista
print(re.split(":", my_string))

# sub
print("---------------- SUB ----------------")
# Reemplaza un patrón en la cadena con otro texto
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))


### Regular Expressions Patterns ###

print("---------------- EXPRESSIONS PATTERNS ----------------")
# Para aprender y validar expresiones regulares:

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "andersondev0526@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "andersondev0526@anderosn.com"
print(re.findall(pattern, email))