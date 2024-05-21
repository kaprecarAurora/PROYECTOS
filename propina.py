
monto_cuenta = float(input("Introduzca la cantidad total de la cuenta:  "))
calidad_servicio = input("¿Como ha sido la calidad del servicio?: ")

def calidad_servicio_calcular(monto_cuenta, calidad_servicio): # Funcion que calcula la propina segun la calidad del servicio

    propinas = {"excelente": 20, "bueno": 15, "regular": 10, "malo": 5} # Diccionario con los porcentajes de propina segun la calidad del servicio
    porcentage = propinas.get(calidad_servicio) # Obtenemos el porcentaje de propina segun la calidad del servicio

    if porcentage: #Valoramos si la calidad del servicio es reconocida
        return (monto_cuenta * porcentage) / 100
    else:
        return "Calidad del servicio no reconocida"

print(calidad_servicio_calcular(monto_cuenta, calidad_servicio))

