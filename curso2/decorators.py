import time
# funcion que recibe una funcion, y devuelve otra funcion
def deco_timer(f):
   def wrap(*args, **kwargs):
      tinicial= time.time()
      result= f(*args, **kwargs)
      tfinal= time.time()
      difftime= tfinal - tinicial
      print("La funcion", f.__name__,"tardo: ",difftime,"segs")
      return result
   return wrap

@deco_timer
def suma(a,b):
   return a+b

suma(10,9)