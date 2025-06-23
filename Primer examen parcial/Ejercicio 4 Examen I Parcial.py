#Ejercicio 4 – Caso práctico industrial (25%)

#Un operario registra diariamente la cantidad de productos defectuosos. Según la cantidad, se genera una alerta:
#- Si hay 0 defectos, imprimir “Producción excelente”
#- De 1 a 5 defectos: “Producción aceptable”
#- De 6 a 10 defectos: “Atención: nivel de defectos elevado”
#- Más de 10 defectos: “ALERTA: debe detenerse la línea de producción”

#Solicite al usuario ingresar la cantidad de defectos y muestre el mensaje adecuado.

# Solicitamos al usuario la cantidad de productos defectuosos:
try:
   productos_defectos = int(input("la cantidad productos defectuosos: "))
except:
    print(" El dato ingresado deber ser numerico. ")
else:
    if productos_defectos == 0:
       print("Producción excelente.")
    elif productos_defectos >= 1 and productos_defectos <= 5:
       print("Producción excelente")
    elif productos_defectos >= 6 and productos_defectos <= 10:
        print("Atención: nivel de defectos elevado")
    elif productos_defectos >0:
        print("ALERTA: debe detenerse la línea de producción.n")
