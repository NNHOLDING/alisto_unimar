def validar_temperatura_horno():
    """
    Solicita la temperatura del horno y evalúa el estado del lote (Aceptable, Dudoso, Descartado).
    """
    try:
        temperatura = float(input("Por favor, ingrese la temperatura registrada en el horno (en grados Celsius): "))

        if 350 <= temperatura <= 400:
            print("Aceptable")
        elif (300 <= temperatura <= 349) or (401 <= temperatura <= 450):
            print("Dudoso")
        else:
            print("Descartado")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para la temperatura.")

# Llama a la función para ejecutar el programa
validar_temperatura_horno()