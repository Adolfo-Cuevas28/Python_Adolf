class FabricaCelulares():
    def __init__(this , marca , *colores , **modelosPrecios): #*colores es una tupla - **modelosPrecios es un diccionario
        this.marca = marca
        this.colores = colores
        this.modelosPrecios = modelosPrecios

#Bloque principal
Marca1 = FabricaCelulares("Motorola" , "Azul" , "Negro" , "Gris" , "Morado" , MotoG=4500 , MotoE=2500 , MotoX=7500)
print(Marca1.marca)
print(Marca1.colores)
print(Marca1.modelosPrecios)

Marca1.Disponibilidad = True #Este es un atributo temporal único para el objeto "Marca1", no se aplica si se crea un nuevo objeto
print(Marca1.Disponibilidad)