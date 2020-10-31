from os import system, name

### FUNCION PARA PINTAR MATRIZ:
def printTable(matriz):
   print('-  0 1 2 ')
   for i in range(3):
      print('{}  {}|{}|{}'.format(i,matriz[i][0],matriz[i][1],matriz[i][2]))
###

### FUNCION PARA ELEGIR CAMPO:
def choiceField(player):
   print("Jugador {}".format(player))
   row = int(input("\nEn que fila colocara su figura? : "))
   column = int(input("En que columna colocara su figura? : ")) 
   return [row,column]
###

### FUNCION PARA CHEQUEAR QUE NO HALLA EXCEPTION
def checkInvalidField(table, move):
   if move[0]>2 or move[0]<0 or move[0]>2 or move[1]<0 or table[move[0]][move[1]]=="O" or table[move[0]][move[1]]=="X":
      return True
   return False
###

### FUNCION PARA CAMBIAR DE JUGADOR
def togglePlayer(flag):
   if flag:
      return "X", not flag
   return "O", not flag
###

### FUNCION PARA CHEQUEAR SI TERMINO EL JUEGO
def checkEnd(table):
   if table[0][0] == table[1][1] == table[2][2] != " " or table[0][2] == table[1][1] == table [2][0] != " " :
      return True
   else:
      for x in range(3):
         if table[0][x] == table[1][x] == table[2][x] != " " or table[x][0] == table[x][1] == table[x][2] != " ":
            return True
   return False
###

### FUNCION PARA CHEQUEAR QUIEN GANO
def checkWinner(x):
   if x % 2 == 0:
      return "X"
   return "O"
###

### FUNCION CLEARSCREEN
def clear(): 
   if name == 'nt': 
      _ = system('cls') 
   else: 
      _ = system('clear') 
###

### FUNCION MAIN:
def main():
   table = [
      [" "," "," "],
      [" "," "," "],
      [" "," "," "]  
   ]
   printTable(table)

   input("\nSeleccione su figura: \n0- O\n1- X\n: ")

   flag= True
   end= 0

   for x in range(9):
      print("\nQuedan {} movimientos posibles!!!".format(9-x))
      player, flag= togglePlayer(flag)

      move = choiceField(player)

      notValid = checkInvalidField(table, move)
      while notValid:
         print("El campo [{}] [{}] no existe o se encuentra ocupado".format(move[0],move[1]))
         move = choiceField(player)
         notValid = checkInvalidField(table, move)


      table[move[0]][move[1]]= player
      
      clear()
      printTable(table)

      end= checkEnd(table)
      if end:
         print("Hay un ganador!")
         winner = checkWinner(x)
         break

   if end:
      print("Quien ha ganado es {}".format(winner))
   else:
      print("El juego termino en empate")
###

play = True
while play:
   clear()
   main()
   play= int(input("\nDesea seguir jugando? \n0: NO\n1: SI\n:"))