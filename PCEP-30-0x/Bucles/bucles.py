# Pregunta 1: Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla:
for i in range(1, 11):
    if i % 2 != 0:
        print(i, "Es un numero impar.")

# Extra: Crea un bucle for que cuente de 0 a 10, e imprima números pares en la pantalla:
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Es un numero par.")

# Pregunta 2: Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.
i = 0
while i <= 10:
    if i % 2 != 0:
        print(i, "Es un número impar.")
    i+=1 

# Pregunta 3: Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres 
# en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. 
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

# Pregunta 4: Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, 
# reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")