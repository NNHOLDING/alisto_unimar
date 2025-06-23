try:
    edad = int(input("Ingrese su edad: "))
except:
    print(" El dato ingresado deber ser numerico. ")
else:
 if edad >= 0:
    if edad >= 0 and edad <= 3:
       print("La edad es de un bebé")
    elif edad >= 4 and edad <= 12:
        print("La edad es de un niño")
    elif edad >= 13 and edad <= 17:
        print("La edad es de un adolecente")
    elif edad >= 18 and edad <= 29:
        print("La edad es de un adulto joven")
    elif edad >= 30 and edad <= 64:
        print("La edad es de un Adulto")
    elif edad >= 65 and edad <= 90:
        print("La edad es de un tercera edad")
    elif edad >= 91 and edad <= 100:
        print("La edad es de uan cuarta edad")
    elif edad >= 100:
        print("La edad es de un centenario")
