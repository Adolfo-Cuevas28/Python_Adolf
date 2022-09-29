import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("green")      #Color de la pantalla
s.title("Prueba 1")     #Titulo de la pantalla

t.shapesize(2,2,2)      #Tamaño de la tortuga
t.fillcolor("orange")   #Color de la flecha
# t.color("blue","orange") - cambia de color (tinta , tortuga)
t.pensize(2)

t.forward(100)

turtle.done()