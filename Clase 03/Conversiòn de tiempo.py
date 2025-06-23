# Solicitar tiempo en minutos
minutos = int(input("Ingrese el tiempo en minutos: "))

# Calcular horas y minutos restantes
horas = minutos // 60  # División entera
min_restantes = minutos % 60  # Módulo para obtener los minutos sobrantes
# minutos = minutos - horas *60
# Mostrar resultado
print(f"{minutos} minutos equivalen a {horas} horas y {min_restantes} minutos.")