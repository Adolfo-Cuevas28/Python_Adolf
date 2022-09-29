'''
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
'''

class Calculadora():
    def __init__(self , num1 , num2):
        self._num1 = num1
        self._num2 = num2

    def suma(self):
        return self._num1 + self._num2
    
    def resta(self):
        return self._num1 - self._num2

    def multiplicacion(self):
        return self._num1 * self._num2

    def division(self):
        return self._num1 / self._num2

    def imprimirResultados(self):
        print("\nSuma: {}\nResta: {}\nMultiplicación: {}\nDivisión: {}\n".format(self.suma() , self.resta() , self.multiplicacion() , self.division()))


#Bloque principal de ejecución
while True:
    try:
        num1 = int(input("Ingresa un número entero: "))
        num2 = int(input("Ingresa otro número entero: "))
        break
    except:
        print("\nNúmeros inválidos, intentalo de nuevo\n")

calc = Calculadora(num1 , num2)
calc.imprimirResultados()