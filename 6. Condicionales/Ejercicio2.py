num = int(input("Ingrese un número entero: "))

#print(abs(num))

if num >= 0:
    print("El absoluto de {} es: {}".format(num,num))
else:
    print("El absoluto de {} es: {}".format(num,num * -1))