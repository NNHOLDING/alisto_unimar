tipo = input("Ingrese el tipo de servicio (A, B o C): ").upper()
urgente = input("¿Desea servicio urgente? (sí/no): ").lower()

if tipo == "A":
    precio = 25000
elif tipo == "B":
    precio = 18000
elif tipo == "C":
    precio = 12000
else:
    print("Tipo de servicio no válido.")
    precio = 0

if urgente == "sí" and precio > 0:
    recargo = precio * 0.20
else:
    recargo = 0

total = precio + recargo
print("Total a pagar: ₡", total)