# Solicitar tiempo en minutos

minutos = int(input("Ingrese los minutos: "))
hora, minutos = divmod( minutos, 60)

# Mostrar resultado
print(f"{minutos} minutos equivalen a {hora} horas y {minutos} minutos.")