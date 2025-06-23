temperatura = float(input("Ingrese la temperatura del horno: "))

if 350 <= temperatura <= 400:
    print("Lote Aceptable")
elif (300 <= temperatura < 350) or (400 < temperatura <= 450):
    print("Lote Dudoso")
else:
    print("Lote Descartado")