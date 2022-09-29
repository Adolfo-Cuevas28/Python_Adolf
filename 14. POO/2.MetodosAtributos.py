class FabricaCelulares():
    marca = "Motorola"
    color = "Azul"
    ram = 8
    memoria = 128

    def llamar(self , mensaje):
        print(mensaje)

    def Encendido(self):
        print("Hello Moto!")

#Bloque principal
Iphone = FabricaCelulares()
print(Iphone.color)
print(Iphone.marca)
print(Iphone.ram)
print(Iphone.memoria)

Iphone.Encendido()
Iphone.llamar("Ayudaaa! Me están matandoooo!")
