for i in range(1 , 11):
    print (i)

print("\nAy perro, ya sé usar ciclos! \nAhora vas tú \n")

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
    print(i)