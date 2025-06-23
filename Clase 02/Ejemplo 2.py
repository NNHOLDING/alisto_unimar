# Solicitar tiempo en minutos
try:
    minutos = int(input("Ingrese el tiempo en minutos: "))
except:
    print("Los minutos ingresaddos deben ser valores n{umericos")
else:
    horas = minutos // 60
    minutos = minutos % 60
# Mostrar resultado
    print(horas,"horas y", minutos,"minutos")