# Solicitamos al usuario el peso del paquete
try:
    peso = float(input("Ingrese el peso del paquete en kilogramos: "))
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número para el peso.")
    exit()

# Clasificamos el paquete según su peso
if peso < 1:
    clasificacion = "Ligero"
elif 1 <= peso <= 5:
    clasificacion = "Mediano"
else:
    clasificacion = "Pesado"

# Imprimimos el resultado
print(f"El paquete es clasificado como: {clasificacion}")
