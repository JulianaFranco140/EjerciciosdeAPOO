#Escribir un programa que determine si un número dado es par o impar

numero = int(input("Ingrese un número: "))

if (numero > 0):
    if (numero%2 == 0):
        print ("El número", numero, "es par")
    
    elif (numero%2 != 0):
        print ("El número ",numero , " no es par")
    
else:
    print ("El número ingresado es 0, no es válido")