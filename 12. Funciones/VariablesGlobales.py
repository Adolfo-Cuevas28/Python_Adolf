num1 = 110 #Variables globales
num2 = 40

def suma():
    global num1 , num2 #Le digo a la función que utilice las variables globales num1 y num2
    num1 -= 10
    num2 -= 10
    return num1 + num2

print(suma())
print(num1 - num2)