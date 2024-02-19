#Escribir una función que calcule la media aritmética de una lista de números

cantidad = int(input("Ingrese la cantidad de números de la lista: "))
suma = 0
for i in range (1, cantidad+1):
    numero = float(input("Ingrese un número: "))
    print(numero)
    suma = suma + numero
def media (numero, cantidad, suma):
    Media = suma / cantidad
    
    return Media

Med = media(numero, cantidad, suma)
print ("La media de los número es: ", Med )
