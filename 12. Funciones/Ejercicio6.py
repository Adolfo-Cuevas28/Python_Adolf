def media(lista):
    return sum(lista)/len(lista)

#Bloque principal
lista = [4 , 20 , 10 , 7 , 8 , 9 , 12 , 15]
print("Lista:",lista)
print("El promedio de la lista es: {}".format(media(lista)))