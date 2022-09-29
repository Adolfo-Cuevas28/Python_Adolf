jugadores = {
    1 : "Casillas",
    15 : "Ramos",
    3 : "Pique",
    5 : "Puyol",
    11 : "Capdevila",
    14 : "Xabi Alonso",
    16 : "Busquets",
    8 : "Xavi Hernandez",
    18 : "Pedrito",
    6 : "Iniesta",
    7 : "Villa"
}

try:
    busqueda = int(input("Ingresa el número de tu jugador: "))
except:
    print("Número introducido inválido.")
    exit()

if busqueda in jugadores:
    print("El jugador con el número {} es: {}".format(busqueda,jugadores.get(busqueda)))
else:
    print("Jugador no encontrado.")