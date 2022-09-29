class A():
    def __init__(self):
        self._contador = 10 #Colocamos el guion bajo como buena práctica
        self._cuenta = 15

    @property #Esta frase le indica a python que el método es un método get
    def contador(self): #Es una buena práctica colocar el mismo nombre que la variable
        return self._contador

    @contador.setter #De esta forma le indicamos a python que es un método set
    def contador(self , contador):
        self._contador = contador

    @property
    def cuenta(self):
        return self._cuenta

    @cuenta.setter
    def cuenta(self , cuenta):
        self._cuenta = cuenta


#Bloque principal de ejecución
a = A()

print(a.contador) #Así podemos acceder a los valores del objeto por medio del método get
a.contador = 20
print(a.contador) #Ahora podemos modificar un atributo por medio del método set

print(a.cuenta)
a.cuenta = 30
print(a.cuenta)