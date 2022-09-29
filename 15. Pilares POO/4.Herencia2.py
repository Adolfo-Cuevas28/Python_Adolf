class Animales():
    def __init__(self , nombre):
        self._nombre = nombre
    
class Perro(Animales):
    def __init__(self , nombre , sonido):
        super().__init__(nombre) #Con "super()" heredamos un método, después de super() colocamos el nombre del método y sus argumentos
        self._sonido = sonido


#Bloque principal de ejecución
dalmata = Perro("Dalmata" , "Miau")
print(dalmata._nombre,'di',dalmata._sonido)