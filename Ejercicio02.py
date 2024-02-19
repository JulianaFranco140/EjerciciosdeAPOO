#Escribir una función que calcule el área de un círculo dado su radio  

import math
radio = float(input("Ingrese el radio del círculo: "))

area = math.pi * (radio**2)

print ("EL área del círculo con radio ",radio, " es ", area)
