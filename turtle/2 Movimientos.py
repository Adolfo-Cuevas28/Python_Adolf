import turtle

s = turtle.Screen() #Pantalla
t = turtle.Turtle() #Flecha

#Mover a la tortuga por el plano cartesiano
t.goto(100,100)
t.goto(-100,100)
t.home()

t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.done()