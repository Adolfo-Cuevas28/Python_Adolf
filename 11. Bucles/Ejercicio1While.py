try:
    numero = int(input("Ingresa un número entero y positivo: "))
except:
    print("Número introducido inválido.")
    exit()

i = 0

if numero <= 0:
    print("Número no válido")
    exit()

print("--La tabla del {}--".format(numero))
while i < 10:
    i += 1
    print("   {} * {} = {}".format(numero , i , numero * i))