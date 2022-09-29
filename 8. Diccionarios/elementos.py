usuario = {
    "Nombre" : "Adolfo" ,
    "Apellido" : "Cuevas" ,
    "Estatura" : 1.80
}

print(usuario)
print(usuario.keys()) #Regresa el nombre de las llaves
print(usuario.values()) #Regresa los valores

print(usuario["Nombre"]) #Regresa el valor de la llave especificada

usuario["Correo"] = "adolfo_cwas@hotmail.com" #Agregamos un nuevo valor
print(usuario)

usuario["Apellido"] = "Cuevas Colorado" #Modificamos el valor
print(usuario)