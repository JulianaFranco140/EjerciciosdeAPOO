#Crear una función que invierta el orden de los números de una lista dada
def invertir_lista(lista):
    
    return lista[::-1]

mi_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_invertida = invertir_lista(mi_lista)
print("Lista original:", mi_lista)
print("Lista invertida:", lista_invertida)
