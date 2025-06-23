# Definir precios de los productos
precio_paletas = 200
precio_batidos = 500
precio_conos = 350
precio_sunday = 1000

# Solicitar cantidades
paletas = int(input("Cuántas paletas desea comprar?: "))
batidos = int(input("Cuántos batidos desea ordenar?: "))
conos = int(input("Cuántos conos desea ordenar?: "))
sundays = int(input("Cuántos sundays desea ordenar?: "))

# Calcular el total a pagar
total_pagar = precio_paletas * paletas + precio_batidos * batidos + precio_conos * conos + precio_sunday * sundays
print(f"El total a pagar es: {total_pagar:.2f}")

# Solicitar el medio de pago y el monto con el que se cancela
medio_pago = input("Ingrese el medio de pago (efectivo, tarjeta, transferencia, etc.): ")
monto_cancelado = float(input("Ingrese el monto con el que se cancela: "))

# Calcular el cambio
cambio = monto_cancelado - total_pagar

# Verificar si el monto ingresado es suficiente
if monto_cancelado >= total_pagar:
    print(f"Monto recibido: {monto_cancelado:.2f} ({medio_pago})")
    print(f"Cambio a devolver: {cambio:.2f}")
else:
    print("Monto insuficiente para realizar la compra. Por favor ingrese un monto válido.")
