# Crea un programa que pida al usuario un número entero positivo y dibuje una pirámide numérica cuya altura sea ese número.

num = int(input("Dime un número: "))

for i in range(1, num + 1):
    for z in range(1, i +1):
        print(z, end="")
    print()