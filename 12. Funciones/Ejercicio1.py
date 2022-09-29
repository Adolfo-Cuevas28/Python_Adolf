def solicitarNumero():
    try:
        num = int(input("Ingresa un número: "))
        return num
    except:
        print("Número introducido inválido.")
        return False

def ordenarLista(lis):
    pares = []
    impares = []

    for i in lis:
        if i % 2 == 0:
            pares.append(i)
        else: 
            impares.append(i)

    pares.sort()
    impares.sort()

    return pares, impares


#Bloque principal de ejecución
lista = [9 , 3 , 14 , 16 , 1 , 90 , 28] #Lista base
print("Lista original: {}\n".format(lista))

for i in range (1,6): #Solicitamos al usuario 5 número para agregar a la lista
    numero = solicitarNumero()
    if numero != False:
        lista.append(numero)
print("Lista con números agregados: {}\n".format(lista))

listaPar , listaImpar = ordenarLista(lista)

print("Lista con números pares: {}\nLista con números impares: {}".format(listaPar , listaImpar)) #Ordenamos los números pares en una lista