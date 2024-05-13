#!/usr/bin/env python3

def calcular_IMC(peso, altura):

    if peso or altura <= 0:
        print("Has introducido un valor no contemplado")

    elif peso > 300 or altura > 240:
        print("Has introducido un valor no contemplado")

    else:
        print(f"Su índice metabólico basal es de: {resultado}") #Imprimimos la operación almacenada en resultado

    return peso / (altura) ** 2 #Calculamos la operación

resultado = calcular_IMC(-5, 1.75)


