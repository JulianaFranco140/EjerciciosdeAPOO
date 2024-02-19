#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo ono.

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
cadena = input("Por favor, ingresa una cadena de texto: ")

if es_palindromo(cadena):
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")