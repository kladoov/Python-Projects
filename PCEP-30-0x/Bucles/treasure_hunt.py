secret_number = 1234
num = int(input("Introduce el código secreto: "))

while num != secret_number:
    num = int(input("Código incorrecto. Inténtalo de nuevo: "))

print("¡Has encontrado el tesoro!")