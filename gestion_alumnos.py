#!/usr/bin/env python3

class Estudiantes:
    lista_estudiantes = []
    lista_calificaciones = []

    def __init__(self, nombre, edad, grado, calificaciones):
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.calificaciones = calificaciones
        self.datos = {
            "Nombre": self.nombre,
            "Edad": self.edad,
            "Grado": self.grado,
            "Calificacion": self.calificaciones
        }
        Estudiantes.lista_estudiantes.append(self.datos)
        Estudiantes.lista_calificaciones.append(self.calificaciones)

    @staticmethod
    def mostrar_info():
        for estudiante in Estudiantes.lista_estudiantes:
            for key, value in estudiante.items():
                print(f"{key}: {value}")
            print("--------------------")

    @staticmethod
    def calcular_promedio():
        suma_calificaciones = sum(Estudiantes.lista_calificaciones)
        numero_calificaciones = len(Estudiantes.lista_calificaciones)
        return suma_calificaciones / numero_calificaciones

while True: 
    opcion = input("Seleccione una opción:\n1. Añadir estudiante\n2. Ver información de los estudiantes\n3. Calcular promedio de calificaciones\n")

    if opcion == "1":
        pedir_nombre = input("Introduzca su nombre: ")
        pedir_edad = int(input("Introduzca su edad: "))
        pedir_grado = input("Introduzca su grado: ")
        pedir_calificacion = float(input("Introduzca su calificacion: \n"))
        estudiante = Estudiantes(pedir_nombre, pedir_edad, pedir_grado, pedir_calificacion)

    elif opcion == "2":
        Estudiantes.mostrar_info()

    elif opcion == "3":
        promedio = Estudiantes.calcular_promedio()
        print(f"\nEl promedio de las calificaciones es: {promedio}\n")

    else:
        print("Opción inválida")