def areaCuadrado(lado):
    return lado*lado

def areaCircuclo(radio):
    return radio*radio*3.14159265359

def solicitarNumero():
    try:
        num = int(input("Ingresa una opción: "))
        return num
    except:
        print("Número introducido inválido.")
        return False

def opcion():
    print("\n1. Calcular el área de un cuadrado \n2.Calcular el área de un circulo \n3. Salir del programa")
    num = solicitarNumero() 
    return num

#Bloque principal de ejecución
num = opcion()

while num == 1 or num == 2:
    if num == 1:
        lado = float(input("Ingresa la longitud de un lado: "))
        print("El área del cuadrado es: {}".format(areaCuadrado(lado)))
    else:
        radio = float(input("Ingresa el radio del circulo: "))
        print("El área del circulo es: {}".format(areaCircuclo(radio)))
    num = opcion()

print("\n¡Gracias!")