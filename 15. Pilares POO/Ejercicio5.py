'''
Crear un programa con tres clases. 
Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante).
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
'''
class Universidad():
    def __init__(self , nombreUni):
        self._nombreUni = nombreUni

class Carrera():
    def __init__(self , especialidad):
        self._especialidad = especialidad

class Estudiante():
    def __init__(self , nombreUni , especialidad , nombreEstudiante , edad):
        Universidad.__init__(self , nombreUni)
        Carrera.__init__(self , especialidad)
        self._nombreEstudiante = nombreEstudiante
        self._edad = edad

    def informacion(self):
        print("Estudiante: {}\nEdad: {}\nUniversidad: {}\nCarrera: {}\n".format(self._nombreEstudiante , self._edad , self._nombreUni , self._especialidad))


#Bloque principal de ejecución
persona = Estudiante("Universidad Veracruzana","LSCA","Adolfo Cuevas",21)
persona.informacion()

persona2 = Estudiante("Universidad Veracruzana","LSCA","Erika Miranda",21)
persona2.informacion()