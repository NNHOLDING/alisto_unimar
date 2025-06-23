def calcular_costo_mantenimiento():
    """
    Calcula el costo total del servicio de mantenimiento, incluyendo recargo por urgencia.
    """
    precios = {
        'A': 25000,
        'B': 18000,
        'C': 12000
    }

    # Pedir al usuario el tipo de servicio
    while True:
        tipo_servicio = input("Ingrese el tipo de servicio (A, B o C): ").upper()
        if tipo_servicio in precios:
            break
        else:
            print("Tipo de servicio inválido. Por favor, ingrese A, B o C.")

    costo_base = precios[tipo_servicio]

    # Preguntar si desea servicio urgente
    while True:
        urgente = input("¿Desea servicio urgente? (sí/no): ").lower()
        if urgente in ["si", "sí", "no"]:
            break
        else:
            print("Respuesta inválida. Por favor, ingrese 'sí' o 'no'.")

    recargo = 0
    if urgente == "si" or urgente == "sí":
        recargo = costo_base * 0.20

    total = costo_base + recargo

    print(f"\nEl costo total del servicio es: ₡{total:,.2f}")

# Llamar a la función para ejecutar el programa
calcular_costo_mantenimiento()