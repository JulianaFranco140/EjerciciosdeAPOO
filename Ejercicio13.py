#Crear un programa que pida al usuario ingresar dos números y calcul su suma, resta, multiplicación y división.

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))

def suma (num1,num2):
    Suma = num1 + num2
    return Suma

def resta (num1, num2):
    Resta = num1 - num2
        
    return Resta

def multiplicacion (num1,num2):
    multi = num1 * num2
    return multi

def division (num1,num2):
    
    div = num1/num2
        
    return div

Division = division(num1,num2)
Multiplicacion = multiplicacion(num1,num2)
Sum = suma(num1,num2)
Resta = resta(num1,num2)
print ("Los números son ", num1, num2)
print ("Su suma es ", Sum, " su resta es", Resta, " su multiplicación es ", Multiplicacion, " y su división es ", Division)
