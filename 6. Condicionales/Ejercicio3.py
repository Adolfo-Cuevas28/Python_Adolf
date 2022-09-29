palabra1 = input("Escribe una palabra: ")
palabra2 = input("Escribe otra palabra: ")

if palabra1[-3:] == palabra2[-3:]:
    print("Si riman :D")
elif palabra1[-2:] == palabra2[-2:]:
    print("Bueno, riman un poco :)")
else:
    print("Vete a la verga, esto ni rima")