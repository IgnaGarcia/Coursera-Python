# ZeroDivisionError : se divide por 0
# NameError : no es encontrada la var
# TypeError : tipo no apropiado 

# manejo de excepcion
try: # provoca excepcion
   pass
except Exception as identifier: # si hay excepcion
   pass
finally: # se ejecuta siempre
   pass

# con else
try:
   pass
except Exception:
   pass
else: # si no se causa excepcion
   pass
finally:
   pass

# se pueden encadenar excepciones poniendo multiples except, siguiendo especifico-general

# crear excepciones
class ExcepcionPropia(Exception):
   "Excepcion propia"
   pass

# con raise podemos provocar una excepcion
raise ExcepcionPropia("algo")