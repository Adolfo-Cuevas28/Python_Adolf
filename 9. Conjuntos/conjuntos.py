conjunto = {1 , 1 , 2 , 3 , 4 , 4 , 5}
lista = [1 , 1 , 2 , 3 , 4 , 4 , 5]

print(conjunto)
#print(lista)

conjunto.add(20) #Agrega un nuevo valor
print(conjunto)

conjunto.remove(2) #Remove y discard eliminan el elemento
conjunto.discard(3)
print(conjunto)

conjunto.pop() #Elimina un valor al azar
print(conjunto)

conjunto.update([5,6,7,8]) #Adjunta más datos al conjunto
print(conjunto)

conjunto.clear() #Elimina todo el conjunto
print(conjunto)