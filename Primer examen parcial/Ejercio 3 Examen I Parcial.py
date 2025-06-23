#Ejercicio 3 – Cálculo de horas extra (30%)

#Un empleado gana ₡2000 por hora. Si trabaja más de 8 horas en un día, las horas adicionales se pagan al doble.
#Solicite al usuario la cantidad de horas trabajadas y calcule el salario diario.

# Definimos el costo de la hora del empleado
costo_horas = 2000
salario = 586000

# Solicitamos la cantidad de horas extras del empleado
try:
    cantidad_horas= float(input("Ingrese la cantidad de horas extras: "))
except:
    print(" El dato ingresado deber ser numerico. ")

# calculamos el monto total de horas extras
else:
    Total_extras = cantidad_horas * costo_horas

# Genweramos el resultado con el total a pagar
total_pagar = salario + Total_extras
print("Total a pagar a empleado es de: ₡", {total_pagar})
