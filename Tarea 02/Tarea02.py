try:
    unidadesProducidas = int(input("Ingrese la cantidad de unidades producidas: "))
    horasTrabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))

except:
    print("Las unidades producidas y las horas deben ser datos numericos. ")
else:
    try:
        if  unidadesProducidas > 0 and horasTrabajadas > 0:
            rendimiento = unidadesProducidas / horasTrabajadas
            print(f" El rendimiento de produccion es de {rendimiento} unidades por hora. ")
        else:
            print("No se pueden ingresar numero negativos. ")
    except:
            print("No es posible dividir entre cero. ")
