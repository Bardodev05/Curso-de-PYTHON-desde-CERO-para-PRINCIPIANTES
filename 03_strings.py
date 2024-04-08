# strings

my_string = "mi string"
my_other_string ='mi strings'
print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_string = "este es un string  \n con salto de linea" 
print(my_new_string)

my_tab_string = "\teste es un string con tabulacion" 
print(my_tab_string)

my_scape_string = "\teste es un string \n escapado" 
print(my_scape_string)

# formateo
name, last_name, ege = "anderson", "molina",19

print("Mi nombre es %s %s y mi edad es %d" %(name,last_name,ege))
print(f"Mi nombre es {name},{last_name} y mi edad es {ege}")

# desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# reverse

reversed_language = language [ ::-1]
print(reversed_language)

reversed_language = language [ ::-2]
print(reversed_language)

#funciones

# Definimos una cadena de ejemplo
mensaje = "   Hola Mundo   "

# Método upper(): convierte la cadena a mayúsculas
print("1. Método upper():", mensaje.upper())  # Salida: "   HOLA MUNDO   "

# Método lower(): convierte la cadena a minúsculas
print("2. Método lower():", mensaje.lower())  # Salida: "   hola mundo   "

# Método capitalize(): convierte la primera letra de la cadena a mayúscula y el resto a minúsculas
print("3. Método capitalize():", mensaje.capitalize())  # Salida: "   hola mundo   "

# Método title(): convierte la primera letra de cada palabra en la cadena a mayúscula
mensaje_title = "bienvenidos al mundo de python"
print("4. Método title():", mensaje_title.title())  # Salida: "Bienvenidos Al Mundo De Python"

# Método strip(): elimina los espacios en blanco al inicio y final de la cadena
print("5. Método strip():", mensaje.strip())  # Salida: "Hola Mundo"

# Método lstrip(): elimina los espacios en blanco del lado izquierdo de la cadena
print("6. Método lstrip():", mensaje.lstrip())  # Salida: "Hola Mundo   "

# Método rstrip(): elimina los espacios en blanco del lado derecho de la cadena
print("7. Método rstrip():", mensaje.rstrip())  # Salida: "   Hola Mundo"

# Método split(): divide la cadena en una lista de subcadenas utilizando un separador (espacio en blanco por defecto)
mensaje_split = "Python es un lenguaje de programación"
palabras = mensaje_split.split()  # Dividir por espacio en blanco
print("8. Método split():", palabras)  # Salida: ['Python', 'es', 'un', 'lenguaje', 'de', 'programación']

# Método join(): une una lista de cadenas en una sola cadena utilizando un separador específico
palabras_join = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación']
mensaje_join = ' '.join(palabras_join)
print("9. Método join():", mensaje_join)  # Salida: "Python es un lenguaje de programación"

