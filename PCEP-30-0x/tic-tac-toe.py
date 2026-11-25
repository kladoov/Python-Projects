from random import randrange

def mostrar_tablero():
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def movimiento_Robot():
    # Movimiento aleatorio por parte del robot
    noEncontrado = True
    while noEncontrado:
        random = randrange(10)
        for i in range(len(board)):
            for z in range(len(board[i])):
                if board[i][z] == random:
                    board[i][z] = "X"
                    noEncontrado = False

def movimiento_User(num):
    for i in range(len(board)):
        for z in range(len(board[i])):
            if board[i][z] == num:
                board[i][z] = "O"
                movimiento_Robot()
                return True
    return False

def victoria_para(sgn):
    if sgn == "X":
        who = 'Robot'
    elif sgn == "O":
        who = 'User'

    cross1 = cross2 = True  # para las diagonales
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who

    # Verifico si siguen quedando posiciones
    for i in range(3):
        for z in range(3):
            if type(board[i][z]) == int:
                return None

    return "Draw"

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Siempre empieza con el primer movimiento
board[1][1] = "X"

# Muestro el tablero inicial
mostrar_tablero()

# Comienza el juego
jugando = True
while jugando:
    pos = int(input("Ingresa tu movimiento: "))

    if pos > 0 and pos < 10:
        if movimiento_User(pos):
            resultado = victoria_para("O") or victoria_para("X")
            if resultado is None:
                mostrar_tablero()
            else:
                if resultado == "Draw":
                    print("Empate.")
                else:
                    print("Gana: ", resultado)

                mostrar_tablero()
                respuesta = input("¿Quieres seguir jugando? si/no: ")
                if respuesta == "si":
                    jugando = True
                    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                    board[1][1] = "X"
                    print("---------------------------------------------------------")
                    mostrar_tablero()
                else:
                    jugando = False
        else:
            print("El número introducido ya tiene una posición asignada.")
    else:
        print("El número introducido debe ser mayor que 0 y menor que 10.")