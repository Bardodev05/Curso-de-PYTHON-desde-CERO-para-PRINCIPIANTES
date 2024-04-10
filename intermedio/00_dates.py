# Importar el módulo datetime de la biblioteca estándar de Python
from datetime import datetime, time, date, timedelta

# Obtener la fecha y hora actuales
now = datetime.now()

# Definir una función para imprimir diferentes componentes de una fecha y hora
def print_date(date):
    # Imprimir el día actual
    print(f"el dia es: {now.day}")
    # Imprimir la hora de la fecha proporcionada
    print(date.hour)
    # Imprimir los minutos de la fecha proporcionada
    print(date.minute)
    # Imprimir los segundos de la fecha proporcionada
    print(date.second)
    # Imprimir el año de la fecha proporcionada
    print(date.year)
    # Imprimir el mes de la fecha proporcionada
    print(date.month)

# Llamar a la función print_date() con la fecha y hora actuales
print_date(now)

# Imprimir los diferentes componentes de la fecha y hora actuales directamente
print(f"el dia es: {now.day}")
print(now.hour)
print(now.minute)
print(now.second)
print(now.year)
print(now.month)

# Obtener el timestamp (marca de tiempo) de la fecha y hora actuales
timestamp = now.timestamp()
print(timestamp)

# Crear un objeto datetime para el 1 de enero de 2024
year_2024 = datetime(2024, 1, 1)

# Llamar a la función print_date() con la fecha y hora del 1 de enero de 2024
print_date(year_2024)

# Crear un objeto de tiempo con hora, minuto y segundo especificados
current_time = time(7,6,0)

# Imprimir los diferentes componentes de la hora actual
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Obtener la fecha actual
current_date = date.today()

# Imprimir el año, mes y día de la fecha actual
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date)

# Crear un objeto de fecha con año, mes y día especificados
current_date = date(2024,10,6)

# Imprimir el año, mes y día del objeto de fecha creado
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Incrementar el mes de la fecha actual en 1 mes
current_date = date(current_date.year, current_date.month + 1, current_date.day)

# Imprimir el mes después de incrementar
print(current_date.month)

# Calcular la diferencia entre dos fechas
diff = year_2024 - now
print(diff)

# Calcular la diferencia en días entre dos fechas
diff = year_2024.date() - current_date
print(diff)

# Imprimir solo el componente de tiempo de la fecha 1 de enero de 2024
print(year_2024.time())

# Crear objetos timedelta para representar diferencias de tiempo
start_timedelta = timedelta(200, 100, 110, weeks= 10)
end_timedelta = timedelta(300, 100, 110, weeks= 13)

# Realizar operaciones de suma y resta entre objetos timedelta
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
