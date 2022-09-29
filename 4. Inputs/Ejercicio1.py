import math

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

try:
    xN=((-(b) - math.sqrt( (b**2) - (4*a*c)))/(2*a))
    xP=((-(b) + math.sqrt( (b**2) - (4*a*c)))/(2*a))
    print("Las soluciones son {"+str(xP)+","+str(xN)+"}")
except:
    print("No existen solución")