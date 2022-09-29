try:
    edad = int(input("Ingresa tu edad: "))
except:
    print("Edad no válida.")
    exit()

i = 0
while i < edad:
    i += 1
    print("{}° año".format(i))