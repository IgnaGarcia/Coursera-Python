class Divisa(object):
   def __init__(self, nombre, simbolo, valorBase):
      self.nombre = nombre
      self.simbolo = simbolo
      self.base = valorBase

   # Parsear a moneda base
   def convertToBase(self, valor):
      return valor * self.base
   def convertFromBase(self, valor):
      return valor / self.base

   def __repr__(self):
      return self.name

class Dinero:
   def __init__(self, valor, divisa):
      self.valor = valor
      self.divisa = divisa
   
   def valorEnBase(self):
      return self.divisa.convertToBase(self.valor)

   def __add__(self, valor):
      aux = self.valorEnBase() + valor.valorEnBase()
      aux = self.divisa.convertFromBase(aux)
      return Dinero(aux, self.divisa)

   def __sub__(self, valor):
      aux = self.valorEnBase() - valor.valorEnBase()
      aux = self.divisa.convertFromBase(aux)
      return Dinero(aux, self.divisa)

   def __mul__(self, valor):
      return Dinero(self.valor * valor, self.divisa)

   def __truediv__(self, valor):
      return Dinero(self.valor / valor, self.divisa)

   del __repr__(self):
      return "{} {}".format(self.divisa.simbolo, self.valor)



dolar = Divisa("Dolar", "U$S", 160)
pesoArg = Divisa("Peso Arg", "$", 1)

dolar1 = Dinero(1, dolar)
peso10 = Dinero(10, pesoArg)

