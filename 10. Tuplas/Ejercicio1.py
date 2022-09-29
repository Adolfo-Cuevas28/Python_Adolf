meses = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
)

try:
    numeroMes = int(input("Ingresa un número de mes: "))
except:
    print("Número introducido inválido.")
    exit()

if numeroMes <= 0:
    print("No existe mes cero o meses negativos")
elif numeroMes <= len(meses):
    print("El mes correspondiente es: {}".format(meses[numeroMes-1]))
else:
    print("Número demasiado grande")