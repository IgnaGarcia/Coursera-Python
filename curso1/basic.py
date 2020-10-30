print("Hola Mundo")

#IF
if a == b:
   print("same")
elif a < b:
   print("menor")
else:
   print("mayor")

#Funcion
def saludo(name):
   print("Hola ", name)

saludo("Nacho")

#Funcion anonima
potencia = lambda a, b: a**b

def fib(x):
   return fib(x-1) + fib(x-2)
print(fib(5))
#For
s=0
for x in range(10):
   s+=x
print(s)

for x in range(0,10,1):
   print("for tradicional ", x)

for x in "Hola Nacho":
   print(x)

#While
i= 0
while i<+10:
   print(i)
   i+=1

#Suma de 50 primeros pares, desde 2 hasta 100
result = 0
for x in range(2,101,2):
   print(x)
   result += x
print(result)

#El break rompe el ciclo

#El continue termina la iteracion actual y 
# sigue con la siguiente

#El else luego del ciclo se ejecutara siempre 
# a menos que se haya roto el ciclo con break

#El pass es una linea vacia, para usarlas en 
# sectores del if donde no se debe actuar

def es_primo(numero):
   resultado = True
   for divisor in range(2, numero):
      print(divisor)
      if (numero % divisor) == 0:
         resultado = False
         break
   return resultado
es_primo(13)

s = 0
for n in range(1, 10):
   if n % 7 == 0:
      break
   s += n
print(s)

s = 0
for n in range(1, 10):
   if n % 2 != 0:
      continue
s += n
else:
   s += 5
print(s)


class SumaDos:
   def __init__(self, datos):
      self.datos = datos
      self.indice = 0
   def __iter__(self):
      return self
   def __next__(self):
      if self.indice == len(self.datos):
         raise StopIteration()
      elemento = self.datos[self.indice] + 2
      self.indice += 1
      return elemento

list(SumaDos([1,2,3,4,5]))
SumaDos.__iter__()

#Para importar modulos se hace
# import MODULO y luego se accede a 
# sus funciones con los .

#Sino se hace
# from MODULO import FUNCION

#Para convertir una carpeta en un paquete se crea
# __init__.py en dicha carpeta y luego se importa dicha carpeta