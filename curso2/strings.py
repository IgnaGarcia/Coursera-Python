# pueden ser con comilla doble "", 
# comilla simple ''
# triple comilla doble """ """ a partir de este se acepta multilinea
# triple comilla simple ''' '''

saludo = "Hola Nacho"

# se puede acceder a los caracteres con []
saludo[2]

# se puede acceder a una cadena con [n:N]
saludo[1:4]
saludo[:3]

# la longitud se puede obtener con len()
len(saludo)

# se concatena con +
saludo2= saludo + " qcyo"

# para embeber una variable en una cadena
# "%s" % cadena
# "%d" % numero
# "%f" % flotante
# "%.2f" % flotanteRedondear

# PARSEAR A UTF8
saludoUTF8 = saludo.encode('utf-8')

# parsear utf8
saludoTransformado = saludoUTF8.decode('utf-8')

# funciones utiles
saludo.isalpha()
saludo.isalnum()
saludo.isnumeric()
saludo.strip()
saludo.replace('Hola', 'Chau')
saludo.split('divisor')

# importar string library
import string

# importar time library
import datetime

# date
fecha = datetime.date('') # constructor
fecha.weekday() # dia de la semana con lunes 0
fecha.isoweekday() # dia de la semana con lunes 1
fecha.isocalendar() # año, numero de semana y dia de semana en iso
fecha.isoformat() # YY-MM-DD
fecha.srtftime() #parse to string con especifico formato
fecha.today() # date actual

# time
hora = datetime.time('') # constructor
hora.isoformat() #HH:MM:SS.ffffff

# datetime
fechaHora = datetime.datetime('') # constructor
# metodos de date y time tambien
fechaHora.date() # fecha
fechaHora.time() # hora
datetime.strptime('string','formato') # convierte a date

# timedelta es para diferencias de tiempos
datetime.timedelta()

date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)
date_time.strftime('%Y/%m/%d %H:%M:%S')