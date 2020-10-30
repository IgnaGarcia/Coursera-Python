# abrir archivo 
# r(lectura), 
# w(sobreescritura), 
# x(nuevo archivo, escritura), 
# a(escribir desde el final), 
# b(binario), 
# t(texto),
# +(lectura escritura) 
arch = open('ruta', '+')

# leer todo el archivo
arch.read()
# leer linea a linea
arch.readline()
# leer lineas como listas
arch.readlines()

# escribir
arch.write("cadena")
# escribir lineas
arch.writelines("1","2","3")

# posicion actual
arch.tell()

# cambiar posicion actual
arch.seek(0)

# cerrar
arch.close()

# manejar csv
import csv

# abrir archivo
with open('mi.csv', newline = '') as f:
   reader = csv.reader(f) # puede tener parametros
# delimiter= 'delimitador de cols'
# quoting= csv.QUOUTE_(ALL | MINIMAL | NONNUMERIC | NONE)
# quoutechar= 'define entrecomillaro'
# lineterminator= 'separador de lineas' 

# escribir con writer, se pueden definir parametros en el writer
with open('mi.csv', 'w', newline = '') as f:
   writer = csv.writer(f)
   writer = writerow([['row1','nacho'], ['row2','juan']])


# estructurar con DictWriter
   writer = csv.DictWritter(f, ['campo1',"campo2"])
   writer.writeheader() # nombre de campo
   writer.writerow({"campo1":'valor1', "campo2":'valor2'})

# manejo de json
import json

# parsear a object
json.dumps(json) 
# se le puede agregar un file como parametro para escribirlo

# parsear json
json.loads(objeto)
# se le puede pasar un archivo para que lo lea 