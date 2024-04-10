### File Handling ###

import csv
import json
import os

# .txt file
print("---------------- .txt file ----------------")

# Leer, escribir y sobrescribir si ya existe
with open("my_file.txt", "w+") as txt_file:
    txt_file.write(
        "Mi nombre es anderson\nMi apellido es Molina\n19 años\nY mi lenguaje preferido es Python\n")

    txt_file.seek(0)  # Mover el puntero al inicio del archivo
    print(txt_file.read(10))  # Leer los primeros 10 caracteres
    print(txt_file.readline())  # Leer la primera línea
    print(txt_file.readline())  # Leer la segunda línea
    for line in txt_file.readlines():  # Leer las líneas restantes
        print(line)

    txt_file.write("\nAunque también me gusta Kotlin\n")

# Usando 'with', no es necesario cerrar explícitamente el archivo

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("Y Swift\n")

# os.remove("Intermediate/my_file.txt")

# Clase en vídeo (03/11/22): https://www.twitch.tv/videos/1642512950

# .json file
print("---------------- .json file ----------------")

json_test = {
    "name": "ander",
    "surname": "Molina",
    "age": 19,
    "languages": ["Python", "Swift", "Kotlin"]
}

with open("my_file.json", "w+") as json_file:
    json.dump(json_test, json_file, indent=2)

with open("my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file
print("---------------- .csv file ----------------")

with open("my_file.csv", "w+") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["name", "surname", "age", "language", "website"])
    csv_writer.writerow(["ander", "Molina", 19, "Python", "https://moure.dev"])
    csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

with open("my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file
print("---------------- .xml file ----------------")
