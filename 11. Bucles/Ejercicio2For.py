print("Hagamos una iteración! \n")

try:
    num1 = int(input("Ingresa un número: "))
    num2 = int(input("Ingresa un número mayor al anterior: "))
except:
    print("Números introducidos inválidos.")
    exit()

if num1 >= num2:
    print("Error, eres un pelotudo, te dije que fuera mayor!")
    exit()

for i in range(num1 , num2+1):
    if (i%2) != 0:
        print(i)