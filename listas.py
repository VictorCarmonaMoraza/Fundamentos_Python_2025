
dimensiones = [14,18,22,13,27,"mesa"]
print(len(dimensiones))

#Agregar elementos a la lista
dimensiones.append(30)

# Eliminar un elemento de la lista
dimensiones.remove("mesa")



for i in range(len(dimensiones)):
    print(f"Índice: {i}, Valor: {dimensiones[i]}")
