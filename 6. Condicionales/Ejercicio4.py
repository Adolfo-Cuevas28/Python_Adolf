print("-----Elecciones 2022------")
print("A. Partido Rojo\nB. Partido Verde\nC. Partido Azul")
voto = input("¿Qué partido escoge (A, B o C)?: ")

if voto.upper() == "A":
    print("Usted ha votado por el partido Rojo")
elif voto.upper() == "B":
    print("Usted ha votado por el partido Verde")
elif voto.upper() == "C":
    print("Usted ha votado por el partido Azul")
else:
    print("Vete a la verga, opción errónea")