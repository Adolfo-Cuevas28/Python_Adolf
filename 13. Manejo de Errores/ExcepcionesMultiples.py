while True:
    try:
        num = int(input("Ingresa un número: "))
        print(100/num)
        break
    except ZeroDivisionError:
        print("No seas boludo, no se puede dividir entre cero")
    except KeyboardInterrupt:
        print("Cancelaste la ejecución")
        break
    except TypeError:
        print("No se puede dividir el número entre una cadena")
    except ValueError:
        print("Debes introducir una cadena que sea un número")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__ )
        print("Error: {}".format(e))