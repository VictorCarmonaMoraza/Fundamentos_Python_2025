
##creacion de un diccionario
diccionario = {"raul": 25, "maria": 30, "jose": 28}

# Acceder a un valor por su clave
print(diccionario["maria"])

# Agregar un nuevo par clave-valor
diccionario["ana"] = 22

# Eliminar un par clave-valor
del diccionario["jose"]

# Recorrer el diccionario
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")