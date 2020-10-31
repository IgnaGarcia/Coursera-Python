# Se va corroborando si hay un ganador
# El juego termina con empate cuando se llena el tablero


#### MIS EXCEPCIONES:
class OutOfTable(Exception):
   message = "El campo {field} no es valido"
   def __init__(self, field: str) -> None:
      self.field = field
      super().__init__(self.message.format(field=field))

class InvalidField(Exception):
   message = "El campo {field} ya se encuentra ocupado"
   def __init__(self, field: str) -> None:
      self.field = field
      super().__init__(self.message.format(field=field))
###

### FUNCION PARA PINTAR MATRIZ:
def printTable(matriz):
   print('-  0 1 2 ')
   for i in range(3):
      print('{} |{}|{}|{}|'.format(i,matriz[i][0],matriz[i][1],matriz[i][2]))
###

### FUNCION PARA ELEGIR CAMPO:
def choiceField(player):
   print("Jugador {}".format(player))
   row = int(input("En que fila colocara su figura? : "))
   column = int(input("En que columna colocara su figura? : ")) 
   return [row,column]
###

### FUNCION PARA CHEQUEAR QUE NO HALLA EXCEPTION OutOfTable
def checkOutOfTable(move):
   if move[0] > 2 or move[0] < 0 or move[0] > 2 or move[1] < 0:
      raise OutOfTable("[{}][{}]".format(move[0],move[1]))
###

### FUNCION PARA CHEQUEAR QUE NO HALLA EXCEPTION InvalidField
def checkInvalidField(move, table):
   if table[move[0]][move[1]]=="O" or table[move[0]][move[1]]=="X":
      raise OutOfTable("[{}][{}]".format(move[0],move[1]))
###

### FUNCION PARA CHEQUEAR SI TERMINO EL JUEGO
def checkEnd(table):
   if table[0][0] == table[1][1] == table[2][2] != "_" or table[0][2] == table[1][1] == table [2][0] != "_" :
      return True
   else:
      for x in range(3):
         if table[0][x] == table[1][x] == table[2][x] != "_" or table[x][0] == table[x][1] == table[x][2] != "_":
            return True
   return False
###

### MAIN:
table = [
   ["_","_","_"],
   ["_","_","_"],
   ["_","_","_"]
]
printTable(table)

choice= bool(input("Seleccione su figura: \n0- O\n1- X\n: "))
if choice:
   player1= "X"
   player2= "O"
else:
   player1= "O"
   player2= "X"

try:
   flag= choice
   end= 0
   for x in range(9):
      if flag:
         move = choiceField(1)

         checkOutOfTable(move)
         checkInvalidField(move, table)

         table[move[0]][move[1]]= player1
         printTable(table)
         flag= not flag

      else:
         move = choiceField(2)

         checkOutOfTable(move)
         checkInvalidField(move, table)

         table[move[0]][move[1]]= player2
         printTable(table)
         flag= not flag

      end= checkEnd(table)
      if end:
         print("Hay un ganador!")
         break
   pass

except (InvalidField, OutOfTable) as err:
   print(err)
   pass

finally:
   if end:
      print("Quien ha ganado es ...")
      ###CALCULAR GANADOR
   else:
      print("El juego termino en empate")
   pass

###