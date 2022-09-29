class FabricaEXplosivos():
    def __init__(self , nombre , precio , peso): #Constructor
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        print("El explosivo {} ha sido creado".format(self.nombre))

    def __str__(self): #Modifica la descripción general del objeto
        return "Este es el explosivo {} con un precio de ${}".format(self.nombre , self.precio)

    def __del__(self): #Destructor - Los objetos se destruyen al final de la ejecución del programa
        print("El explosivo {} ha sido destruido".format(self.nombre))

#Bloque Principal
dinamita = FabricaEXplosivos("TNT" , 2000 , 4.5)
print(dinamita.nombre)
print(dinamita) #Descripción general del objeto

#Finaliza el programa, se activa el destructor