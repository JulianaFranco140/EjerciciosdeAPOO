#Crear un programa que calcule la suma de los números en una lista dada

cant = int(input("Ingrese la cantidad de números de la lista: "))

suma = 0

for i in range (1,cant+1):
    n = float(input("Ingrese un número: "))
    
    suma = suma + n
    
print("La suma de los números es:", suma)