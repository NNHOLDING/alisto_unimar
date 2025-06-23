 #Solicitar datos al usuario
base = (input("Ingrese la base del rectángulo: "))
altura = (input("Ingrese la altura del rectángulo: "))

# Calcular área
try:
    area = float(base) * float(altura)
except:
    print("Los datos ingresados no son númericos")
else:
    print(f"El área del rectángulo es: {area} unidades cuadradas")
