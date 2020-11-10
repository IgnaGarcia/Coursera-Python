class Romanos(object):
   valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
   simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

   def toRoman(self, value):
      resto = value
      resultado = ""

      for i in range(len(self.valores)):
         resultado, resto= self.appendRoman(resto, self.valores[i], self.simbolos[i], resultado)
      
      return resultado


   def appendRoman(self, value, intValue, romanValue, resultado):
      resto = value
      
      while resto >= intValue:
         resultado = resultado + romanValue
         resto -= intValue

      return resultado, resto