#Escribir una función que calcule el factorial de un número dado

import math

num = int(input("Ingrese un número: "))

def factorial (num):
    if (num < 0):
        print ("El número dado es negativo, su factorial no existe")
    elif (num == 0):
        return 1
    
    else: 
        for i in range (num):
            fac = math.factorial(num)
            
        return fac 
        
facto = factorial(num)
print ("El factorial del número: ",facto)
        