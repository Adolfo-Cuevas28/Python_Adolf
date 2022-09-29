def solicitarNumero():
    try:
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa otro número: "))
        return num1 , num2
    except:
        print("Número introducido inválido.")
        return False , False

def calcularMayor(n1 , n2):
    if n1 > n2:
        return 1
    elif n2 > n1:
        return -1
    else:
        return 0

#Bloque principal de ejecución
num1 , num2 = solicitarNumero()

while num1 == False:
    num1 , num2 = solicitarNumero()

print("El resultado es: {}".format(calcularMayor(num1 , num2)))