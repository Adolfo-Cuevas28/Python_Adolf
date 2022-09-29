cadena="Te quiero solo como amigo"

print(cadena[:3],"- Dos primeros caracteres")
print(cadena[-3:],"- Últimos tres caracteres")

for i in range(0,len(cadena),2):
    print(f"{cadena[i]}",end="")

print(" - Cada dos caracteres") #print(cadena[::2])

for i in range(len(cadena)-1,-1,-1):
    print(f"{cadena[i]}",end="")

print(" - Palabra a la inversa") #print(cadena[::-1])

for i in range(0,len(cadena)):
    print(f"{cadena[i]}",end="")
for i in range(len(cadena)-1,-1,-1):
    print(f"{cadena[i]}",end="")

print(" - Normal y a la inversa")