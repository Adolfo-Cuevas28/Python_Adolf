def argumentos(*num): #Se agrega un asterisco para indicar que serán varios argumentos, pero se desconoce el número exacto
    for i in num:
        print(i)
    return type(num) #Se guardará el parámetro como una tupla

print(argumentos( 10 , 20 , 30 , 40 , 50 ))