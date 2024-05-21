#!/usr/bin/env python3


with open('credenciales.txt', 'r') as archivo:
        
    lineas = archivo.readlines()
    credenciales = tuple(linea.strip() for linea in lineas)

for credencial in credenciales:

    if credencial.islower() == False:

        credencial_no_mayuscula = True

    elif credencial.islower() == True:

        credencial_no_minuscula = True

for credencial_2 in credenciales:

    if credencial_no_mayuscula and credencial_no_minuscula == True:
        
        print("Contraseña debil")
    
    else:
        print("Contraseña fuerte")


minuscula = "hoLa"
tiene_mayuscula = minuscula.islower()
print(tiene_mayuscula)

if tiene_mayuscula == True:
    print("Tiene mayúscula")
else:
    print("No hay ninguna mayúscula")




    
    