'''
Herencia - Consiste en que una clase hijo obtenga (o herede) los mismos atributos y funciones de una clase padre
'''

class Animales():
    def hablar(self):
        print("Hola humano :v")
    
    def descripcion(self):
        print("Yo soy un {}".format(self._nombre))

class Perro(Animales):
    pass

class Gato(Animales):
    def __init__(self , nombre):
        self._nombre = nombre


#Bloque principal de ejecución
chihuahua = Perro()
chihuahua.hablar() #La clase "Perro" heredo el método "hablar" de la clase "Animales"

miau = Gato("Michi")
miau.descripcion()