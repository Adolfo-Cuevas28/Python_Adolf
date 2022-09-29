while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Ah, tas viejo, tienes {}".format(edad))
        break
    except:
        print("No seas boludo, coloca un número")
    finally:
        #Esto se ejecuta haya o no haya error
        print("OwO\n")