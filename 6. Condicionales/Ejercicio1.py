letra = input("Ingrese una vocal: ")

if letra.lower() == "a":
    print("Esta vocal es la A")
elif letra.lower() == "e":
    print("Esra vocal es la E")
elif letra.lower() == "i":
    print("Esra vocal es la I")
elif letra.lower() == "o":
    print("Esra vocal es la O")
elif letra.lower() == "u":
    print("Esra vocal es la U")
else:
    print("¿Eres imbécil? TE DIJE UNA VOCAL!!!")

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("No es un vocal")
