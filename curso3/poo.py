# todo es un objeto
# los objetos colaboran entre si enviandose mensajes

# clase
class MiClase(object):
   # constructor
   def __init__(self, var):
      self.var = var

   def m1(self):
      return "Hola {}".format(self.var)

   # metodo de clase
   @classmethod
   def m2(self):
      return self

# instancia
objeto1 = MiClase(4)
objeto1.m1()

#-------------------
# clase: objeto que representa una entidad del dominio del problema
# subclasificacion/herencia: relacion estatica entre clases
   # si se envia un mensaje a un metodo el recorrido de busqueda es especifico -> general
# metodo:  resultado de la recepcion de un mensaje de un objeto
   # de instancia: implementan mensajes a enviar a instancias
   # de clase: implementan mensajes a enviar a la clase
# polimorfismo: 


# KISS: Keep It Short and Simple
# YAGNI: You Arent Gonna Need It (anticipar cambios futuros)
# SRP: Single Responsibility Principle (realiza una unica cosa)
# DRY: Dont Repeat Yourself (redundancia y repeticion de codigo)