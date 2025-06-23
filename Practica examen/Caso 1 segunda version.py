peso = float(input("Ingrese el peso del paquete en kg: "))

if peso < 1:
    print("Ligero")
elif peso <= 5:
    print("Mediano")
else:
    print("Pesado")