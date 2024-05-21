#!/usr/bin/env python3

def leer_archivos(credenciales):

    with open(credencial, 'r') as archivo:
        
        lineas = archivo.readlines()
        credenciales = tuple(str(linea.strip() for linea in lineas))
        
    return credenciales

def contraseña_fuerte(contraseñas):

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    tiene_especial = False

    for contraseña in contraseñas:
        if contraseña.isupper():
            tiene_mayuscula = True
        if contraseña.islower():
            tiene_minuscula = True
        if contraseña.isdigit():
            tiene_digito = True
        if contraseña in "!@#%&*":
            tiene_especial = True

    return tiene_mayuscula and tiene_especial and tiene_digito and tiene_minuscula

    
credencial = "credenciales.txt"
contraseña = leer_archivos(credencial)
contraseña_fuerte_verificar = contraseña_fuerte(contraseña)

verificar_credenciales(credencial)