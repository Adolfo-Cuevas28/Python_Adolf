def calcularIVA(importe , iva = 0.21):
    return importe * (1+iva)

def solicitarNumero():
    try:
        total = float(input("Ingresa el importe a pagar: "))
        iva = float(input("Ingresa el pocentaje de IVA (21%): "))
        return total , iva
    except:
        print("Número introducido inválido.")
        return False , False

#Bloque principal de ejecución
tot , iva = solicitarNumero()

while tot == False and iva == False:
    tot , iva = solicitarNumero()

if iva >= 1:
    print("El total a pagar es: ${}".format(calcularIVA(tot , iva / 100)))
elif iva == 0:
    print("El total a pagar es: ${}".format(calcularIVA(tot)))
else:
    print("Error, el iva no puede ser negativo")