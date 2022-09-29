'''
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre 
y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un 
mensaje con el resultado de la nota y si ha aprobado o no.
'''

class Estudiante():
    def __init__(self , nombre , nota):
        self._nombre = nombre
        self._nota = nota

    def resultados(self):
        print("El alumno {} ha obtenido {} de calificacion".format(self._nombre , self._nota))
        if(self._nota>5):
            print("¡Aprobado!\n")
        else:
            print("¡Reprobado!\n")


#Bloque principal de ejecución
student1 = Estudiante("Adolfo" , 5)
student2 = Estudiante("Erika" , 6)

student1.resultados()
student2.resultados()