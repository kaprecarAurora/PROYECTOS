#!/usr/bin/env python3

archivos_sistema = []

def opciones():

    while True:

        print("\n1. AÑADIR ARCHIVOS")
        print("\n2. QUITAR ARCHIVOS")
        opcion = int(input("\nIntroduzca opcion: "))

        if opcion == 1:

            while True:

                archivo = str(input("\nIntroduzca el nombre del archivo que desea añadir: ")) 
        
                archivos_sistema.append(archivo)

                print(f"\nEstos son los archivos que tienes en el sistema:\n")

                for i in archivos_sistema:
                    print(i, end=' | ')

                print("\n")
        
                opcion2 = str(input("Desea seguir añadiendo archivos (Y/N): "))
            
                if opcion2 == "N":
                    break

                else:
                    print("\nOpción no contemplada")
                    continue
                   
opciones()
