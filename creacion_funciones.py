import math


def potencia(valor_abse,valor_exponente=2):
    potencia = math.pow(valor_abse,valor_exponente)
    print(f"La potencia de {valor_abse} elevado a {valor_exponente} es: {potencia}")
    

potencia(2,3)

#Argumentos flexibles
def suma(*args):
    resultado = sum(args)
    print(f"La suma de los números es: {resultado}")

suma(1, 2, 3, 4, 5)

#Crear una funcion que calcule el area de un triangulo dados como argumentos la base y la altura.
#Comprueba que el resultado es correcto para un triangulo de base =5 y altura =3

def area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

help(area_triangulo)  
area_triangulo(5, 3)
