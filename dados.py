# Para este proyecto, tendrás que crear un programa que simule la tirada de dados.
# Cada vez que ejecutamos el programa, éste elegirá dos números aleatorios entre el 1 y el 6. 
# El programa deberá imprimirlos en pantalla, imprimir su suma y preguntarle al usuario si quiere tirar los dados otra vez.

import random

cases = [1,2,3,4,5,6]
flag = 1

while flag:   
   number1 = random.choice(cases)
   number2 = random.choice(cases)

   print("n1: \t", number1, "\nn2: \t", number2)
   print("Suma: \t", number1+number2)

   print("\nDesea continuar?: \n0: \tNo\n1: \tSi")
   flag = int(input())
   print("-----------\n")