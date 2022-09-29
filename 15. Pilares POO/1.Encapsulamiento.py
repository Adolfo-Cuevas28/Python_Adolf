'''
Encapsulamiento, que las variables de un objeto solo puedan ser modificados por métodos del propio objeto
No se debería poder acceder, eliminar o alterar una variable de un objeto desde fuera de él
'''

class A():
    def __init__(self):
        self.contador = 0

    def aumentar(self):
        self.contador += 1

    def contar(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0 #Usando el doble guion bajo indicamos que la variable solo podrá ser usada dentro de la clase

    def aumentar(self):
        self.__contador += 1

    def contar(self):
        return self.__contador


#Bloque principal de ejecución
print("Objeto 1")
a = A()
print(a.contar())
a.aumentar()
print(a.contar())
print(a.contador) #De la primera forma, podemos acceder al contador del objeto a, lo cual es incorrecto

print("\nObjeto 2")
b = B()
print(b.contar())
b.aumentar()
print(b.contar())
print(b.__contador) #Al intentar acceder a la variable del objeto, nos marcara un error
                    #Solo podemos modificar la variable dentro del mismo objeto

'''
Algunos programadores de python utilizan solo un guion bajo "self._contador"
En este caso python no marcará error si se intenta acceder a un valor de un objeto, pero servirá para alertar a otros
programadores de no realizar esa práctica
'''