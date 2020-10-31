# crear
a = {"clave": "valor",...}
b = dict(clave="valor",...)

# se puede acceder por indices
a["clave"]

# agregar elemento
a["nuevaclave"]= "valornuevo"

# pisar elemento
a["clave"]= "nuevovalor"

# borrar elemento
del a["clave"]

# tamaño
len(a)

# obtener elemento
a.get("clave")

# devuelve el valor o la crea
a.setdefault("clave")
a.setdefault("clave", "default")

# actualiza
a.update({"clave2": "valor2"})

# claves del dict
a.keys()
# valores del dict
a.values()
# key-values
a.items()
## se pueden asignar a variables y se quedan linkeados

# quitar del dict
a.pop("clave")

# quitar el ultimo ingresado LIFO
a.popitem()