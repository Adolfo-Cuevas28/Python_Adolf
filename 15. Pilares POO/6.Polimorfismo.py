'''
Polimorfismo - Modificación de un método en una clase hijo que está siendo heredado de una clase padre
'''

class Animales():
    def __init__(self , sonido):
        self._sonido = sonido

    def habla(self):
        print(self._sonido)

class Perro(Animales):
    def habla(self):
        print("Guau conchetumare")

class Gato(Animales):
    def habla(self):
        print("Miaaaau xdxd")


#Bloque principal de ejecución
a = Animales("Grrr")
b = Perro("Guau")
c = Gato("Miau")

a.habla()
b.habla()
c.habla()