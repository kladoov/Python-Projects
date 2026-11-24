secret_number = 2468
llaves = 3
salida = True

num = int(input("Introduce el código: "))

while salida and num != secret_number:
    llaves = llaves - 1
    print("Código incorrecto. Llaves restantes: ", llaves)

    if llaves == 0:
        print("Te has quedado atrapado. Game Over.")
        salida = False
    else:
        num = int(input("Introduce el código: "))

if num == secret_number:
    print("¡Has escapado de la mazmorra!")