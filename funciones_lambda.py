
lista = [4,5,2]
lista_al_cuadrado = map(lambda x: x**2, lista)
print(list(lista_al_cuadrado))

##Crear un funcion lambda que convierta de $ a euros una lista de precios
## Asumir que 1 euro = 1.1 dolares
precio_dol = [10.82, 11.95, 14.49, 24.95]
precio_euro = list(map(lambda x: x / 1.1, precio_dol))
print(precio_euro)