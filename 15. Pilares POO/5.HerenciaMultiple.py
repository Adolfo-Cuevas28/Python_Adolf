# Una clase hijo hereda de 2 o más clases

class A():
    def primera(self):
        return ("Holi, esta es la clase A")

class B():
    def segunda(self):
        return ("Holo, esta es la clase B")

class C(A , B):
    pass


#Bloque principal de ejecución
c = C()
print(c.primera())
print(c.segunda())