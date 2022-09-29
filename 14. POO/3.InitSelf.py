class FabricaAutos():
    def __init__(self , marca , color , ram , almacenamiento):
        self.marca = marca
        self.color = color
        self.ram = ram
        self.almacenamiento = almacenamiento

#Bloque principal
MotoG = FabricaAutos("Motorola","Azul",3,32)
print(MotoG.marca,MotoG.color)