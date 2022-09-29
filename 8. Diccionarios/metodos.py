diccionario = {
    1:2,
    2:3,
    3:4
}

print(diccionario.get(2)) #Obtenemos el valor de la llave especificada

'''
diccionario.pop(3) #Elimina el valor de la llave especificada
print(diccionario)

diccionario.clear() #Elimina todo el diccionario
print(diccionario)
'''

diccionario.setdefault(4,5) #Agrega un nuevo valor - (llave,valor)
print(diccionario)

#Se pueden juntar dos diccionarios por medio del metodo update
diccionario2 = {
    5:6,
    6:7,
    7:8
}
diccionario.update(diccionario2)
print(diccionario)

#Crear copia del diccionario
diccionario3 = diccionario.copy()
print(diccionario3)