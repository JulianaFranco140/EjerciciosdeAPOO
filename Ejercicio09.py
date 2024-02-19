#Crear un programa que genere una matriz de números y la imprima en pantalla
import random 

def generar_matriz (filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = random.randint(1,100)
            fila.append(numero)
        matriz.append(fila)
    return matriz

def imprimir_matriz (matriz):
    for fila in matriz:
        for numero in fila:
            print(f"{numero:3}",end = "")
        print()
        
filas = 4
columnas = 4

matr = generar_matriz(filas,columnas)
imprimir_matriz(matr)