#Ejercicio 1 – Cálculo simple (20%)
#Una tienda vende tres tipos de materiales:
#- Tornillos a ₡15 cada uno
#- Tuercas a ₡10 cada una
#- Arandelas a ₡5 cada una

# solicitamos al usuario el material requerido
Tornillos = int(input("Cuántos tornillos desea comprar?: "))
Tuercas = int(input("Cuántas tuercas desea comprar?: "))
Arandelas = int(input("Cuántas Arandelas desea comprar?: "))

# Definimos el precio de los materiales

precio_Tornillos = 15
precio_Tuercas = 10
precio_Arandela = 5

 # Calcular el total a pagar
total_pagar = precio_Tornillos * Tornillos + precio_Tuercas * Tuercas + precio_Arandela * Arandelas
print(f"El total a pagar es: {total_pagar:.2f}")

# Solicitar el medio de pago y el monto con el que se cancela
medio_pago = input("Ingrese el medio de pago (efectivo, tarjeta, transferencia, etc.): ")
monto_cancelado = float(input("Ingrese el monto con el que se cancela: "))