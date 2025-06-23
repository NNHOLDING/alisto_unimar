try:
    c = float(input("Ingrese la temperatura en grados celsius: "))
except:
    print(("la temperatura debe ser valor numerico. "))
else:
    f = c * 9/5 *32
    print(f"{c} grados celsius son equivalentes {f} grados fahrenheit. ")
