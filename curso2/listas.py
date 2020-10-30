# guardan cualquier cosa
lista = [3, 7.5, "holam undo"]

# se acceden como vector
lista[0]
lista[-2]

# slicing
lista[1:]
lista[2:3]
lista[:2]

# cantidad de elementos
len(lista)

# agregar elemento
lista.append("value")

# agrega elementos de una lista
lista.extend(["Otra lista", 12])

# insertar elementos en un indice, no reemplaza
lista.insert(2, "value")

# eliminar elemento y guardarlo
lista.pop()
lista.pop(2)

# limpiar lista
lista.clear()

# lista como cola
from collections import deque
queue = deque[1,2,3]
queue.append[4]
queue.popleft()

# lista por comprension
cuadrados = [x ** 2 for x in range(10)]
cuadra2 = list(map(lambda x: x**2, range(10)))
pares = [x for x in cuadra2 if (x%2==0)]
paresCuadra2 = [(x, x**2)] for x in pares

# buscar elementos
lista.index("value")

# ordenar elementos
lista.sort()
lista.sort(reverse=True)
lista.sort(key=lambda x: x[1]) # funcion ordenadora
sorted(lista)
sorted(lista, key=lambda x: x[1])

# conjuntos/set
algo = {1,2,3,4,1}

1 in algo

set() # conjunto vacio
algo2 = set('abracadabra')
algo3 = set('alacazan')
set(1)

# operadores
a . b # diferencia
a | b # union
a & b # interseccion
a ^ b # diferencia de la interseccion

# matrices como listas
matriz = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
matriz[0][2]

# matrices con numpy mas eficiente

# tuplas
t = (1, 2.5, "hola")
t[2]
t[:2]
tupla= ()
tupla= tuple()
unicoElemento= (5, )
len(t)