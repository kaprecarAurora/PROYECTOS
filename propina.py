#!/usr/bin/env python3

def calidad_servicio_calcular():
    propinas = {"excelente": 20, "bueno": 15, "regular": 10, "malo": 5}
    while True:
        monto_cuenta = float(input("Introduzca la cantidad total de la cuenta:  "))
        calidad_servicio = input("¿Como ha sido la calidad del servicio?: ")

        porcentaje = propinas.get(calidad_servicio)

        if porcentaje:
            return (monto_cuenta * porcentaje) / 100
            
        else:
            print("Calidad del servicio no reconocida")
            continue
               
while True:
    print(calidad_servicio_calcular())
