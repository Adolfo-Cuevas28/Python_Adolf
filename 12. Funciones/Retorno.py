def entero():
    print("numero..")
    return 10

def asignacion():
    return 1 , 3 , 4 , 6 

print(entero())

a , b , c , d = asignacion()

print(" {} - {} - {} - {}".format(a , b , c , d))