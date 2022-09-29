'''
Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...".
Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo".
Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje 
y que muestre ese mesjae como parametro
'''
class Marino():
    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo xd")

class Foca(Marino):
    def hablar(self , mensaje):
        print(mensaje)


#Bloque principal de ejecución
obj1 = Marino()
obj2 = Pulpo()
obj3 = Foca()

obj1.hablar()
obj2.hablar()
obj3.hablar("Hola soy un foco")