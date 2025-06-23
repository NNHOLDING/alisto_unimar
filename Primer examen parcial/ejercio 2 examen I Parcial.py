from openpyxl.styles.builtins import total

try:
    monto_pagar= float(input("Ingrese el monto a pagar: "))
except:
    print(" El dato ingresado deber ser numerico. ")
else:
    descuento = input("Ingrese el tipo tipo de descuento (A, B o C): ").upper()

if   descuento == "A":
     descuento = monto_pagar * 0.10
elif descuento == "B":
     descuento = monto_pagar * 0.05

elif descuento == "C":
     descuento = monto_pagar * 0
else:
         print("No hay descuento.")
         descuento = 0

# Calculamos el total que debe cancelarse
total_pagar = monto_pagar - descuento

# Imprime el resultado del total a pagar
print("Total a pagar: ₡", {total_pagar})