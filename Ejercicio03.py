#Crear un programa que genere una lista de números aleatorios y los imrpima en pantalla

import random

print ("La lista de números es: ")
for i in range (10):
    lista = random.randint(1,1000)
    print(lista)