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

                elif opcion2 == "Y":
                    continue
                else:
                    print("\nOpción no contemplada")
        
        if opcion == 2:

            while True:

                archivo = str(input("\nIntroduce el nombre del archivo que desea eliminar: "))

                for i in archivos_sistema:

                    if i == archivo:
                        archivos_sistema.remove(archivo)

                        print(f"\nEstos son los archivos que tienes en el sistema:\n")

                        for i in archivos_sistema:
                            print(i, end=' | ')

                        print("\n")

                    else:
                        continue

                opcion3 = str(input("Desea seguir eliminando archivos (Y/N): "))

                if opcion3 == "N":
                    break 

opciones()
