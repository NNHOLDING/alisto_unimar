# Definir precios por hora de alquiler de vehículos
precio_bicicleta = 5
precio_motocicleta = 10  # Corrección en la capitalización
precio_carro = 20

# Solicitar horas de alquiler
horas_bicicleta = float(input("Ingrese cuántas horas desea alquilar una bicicleta: "))
horas_motocicleta = float(input("Ingrese cuántas horas desea alquilar una motocicleta: "))
horas_carro = float(input("Ingrese cuántas horas desea alquilar un carro: "))

# Calcular total
total = (horas_bicicleta * precio_bicicleta +
         horas_motocicleta * precio_motocicleta +
         horas_carro * precio_carro)

print(f"\nEl total a pagar es: ${total}")
#print ( f"  cantidad de horas seleccionadas para bicicletas son: {horas_bicicletas}")
#print("La cantidad de horas seleccionadas para motocicletas son: " + str (horas_motocicletas))
#print(" La cantidad de horas seleccionadas para carro son:", choras_carro)
#print("El total a pagar es de:{}",format(total))

