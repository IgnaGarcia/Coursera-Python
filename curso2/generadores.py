# iteradores perezosos
def generador():
   for n in range(10):
      yield n # yield reemplaza return

# instanciamos y utilizamos generador
iterador= generador()
iterador.__next__()
# devuelve StopIteration cuando alcanza el max

# si el generador tiene un return este corta y envia StopIteration

# generador por comprension
(p for p in range(10) if p%2==0)

# se usan para infinitudes, estructuras muy grandes