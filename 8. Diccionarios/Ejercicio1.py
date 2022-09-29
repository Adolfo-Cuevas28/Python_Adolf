paises = {
    "Guatemala" : "Ciudad de Guatemala",
    "El Salvador" : "San Salvador",
    "Honduras" : "Honduras",
    "Nicaragua" : "Managua",
    "Costa Rica" : "San Jose",
    "Panama" : "Panama",
    "Argentina" : "Buenos Aires",
    "Colombia" : "Bogota",
    "Venezuela" : "Caracas",
    "España" : "Madrid"
}

contador = 0 #Si no se encuentra el país, permanecerá en 0
busqueda = input("Ingresa un país: ")

for x in paises:
    if x.lower() == busqueda.lower():
        contador += 1
        print("La capital de {} es: {}".format(x,paises.get(x)))

if contador == 0:
    print("País no encontrado.")