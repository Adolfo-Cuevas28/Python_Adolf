import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10)             # 1 - 10 , Aumenta la velocidad
t.circle(60)            # Realiza un circulo con diametro de 60
t.dot(60, "red")        # Realiza un punto de tamaño de 60 rojo
t.hideturtle()          #Oculta la tortuga
t.circle(70)    
t.dot(30, "green")
t.showturtle()          #Muestra de nuevo la tortuga
t.circle(100)
t.setx(-200)            #Mueve la tortuga solo en el eje x
t.sety(150)             #Mueve la tortuga solo en el eje y

turtle.done()