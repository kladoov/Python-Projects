# EJERCICIO PARA PRACTICAR LAS CONDICIONES IF

vida = int(input("Dime la vida del jugador: ")) # valor entre 0 y 100
municion = int(input("Dime la munición que te queda: "))
comida = input("¿Tienes comida? si/no: ") # True o False
if comida == "si": # Para convertir un texto a un bool debe pasarse por un condicional ya que cualquier texto introducido es True
    comida = True
else:
    comida = False

infeccion = int(input("Dime el nivel de infección: ")) # valor entre 0 y 100

if infeccion >= 100:
    print("Te has transformado en Zombie.")
else:
    if vida <= 0:
        print("Has muerto...")
    else:
        if vida <= 25:
            print("Estas gravemente herido...")
        elif vida >= 26 and vida <= 60:
            print("Estas herido...")
        elif vida > 60 and vida <= 100: 
            print("!Estas en muy buen estado!")

        print()
        decision = int(input("!!ZOMBIE!!, ¿que quieres hacer? 1 Atacar, 2 Huir, 3 Esconderse: "))

        if decision == 1:
            if municion >= 3:
                print("Has matado al Zombie.")
            elif municion >= 1 and municion <= 2:
                print("Has herido al Zombie pero sigue vivo...")
            else:
                print("Te acaba de hacer daño el zombie...")
        elif decision == 2:
            if vida > 50:
                print("Has escapado con exito.")
            elif vida <= 50: 
                print("Has sido herido durante la huida...")
        elif decision == 3:
            if comida:
                print("El zombie ha detectado el olor y debes cambiar el escondite")
            else:
                print("!Te has escondido sin ser detectado!")
        else:
            print("Por gracioso te ha matado el admin por no escoger entre el 1, 2 o 3")

        print()
        if infeccion <= 0:
            print("No estas infectado.")
        elif infeccion >= 1 and infeccion <= 30:
            print("Tienes una infeccion leve.")
        elif infeccion >= 31 and infeccion <= 70:
            print("Tienes una infeccion peligrosa.")
        elif infeccion > 70 and infeccion < 100:
            print("Estas en estado critico.")