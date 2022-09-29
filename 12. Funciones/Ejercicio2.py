from math import factorial

def solicitarNumero():
    try:
        num = int(input("Ingresa un número positivo: "))
        if num > 0:
            return num
        else:
            print("Error, el número debe ser positivo")
            return False
    except:
        print("Número introducido inválido.")
        return False

def calcularFactorial(n):
    return factorial(n)

#Bloque principal de ejercución
num = False
while num == False: #Hasta que no se introduzca un número válido
    num = solicitarNumero()

print("El factorial de {} es: {}".format(num , calcularFactorial(num)))