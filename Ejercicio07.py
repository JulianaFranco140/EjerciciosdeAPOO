#Escribir un programa que encuentre el número más grande en una lista dada
cant = int(input("Ingrese la cantidad de números de la lista: "))
n_mayor= 0

for i in range (1,cant+1):
    n = float(input("Ingrese un número: "))
    if (n > n_mayor):
        n_mayor = n
    
    else: 
        n_mayor = n_mayor
        
print ("El número mayor es: ", n_mayor)