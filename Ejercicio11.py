#Crear un programa que genere una lista de números  pares entre 1 y 100

import random 
print ("La lista de números es: ")
for i in range (20):
    n = random.randint(1,100)
    if (n % 2 == 0):
        print (n)