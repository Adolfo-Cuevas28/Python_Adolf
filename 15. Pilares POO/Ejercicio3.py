'''
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
'''
class Fabrica():
    def __init__(self , llantas , color , precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    def caracteristicas(self):
        print("Tiene {} llantas, es de color {} y tiene un precio de ${}".format(self._llantas , self._color , self._precio))

class Moto(Fabrica):
    pass

class Carro(Fabrica):
    pass


#Bloque principal de ejecución
moto = Moto(2 , "Negro" , 18000)
carro = Carro(4 , "Rojo" , 500000)

moto.caracteristicas()
carro.caracteristicas()