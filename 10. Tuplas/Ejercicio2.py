abecedario = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
)

try:
    numeroLetra = int(input("Ingresa un número: "))
except:
    print("Número introducido inválido.")
    exit()

if numeroLetra <= 0:
    print("No existe letras cero o letras negativos")
elif numeroLetra <= len(abecedario):
    print("La letra correspondiente es: {}".format(abecedario[numeroLetra-1]))
else:
    print("Número demasiado grande")