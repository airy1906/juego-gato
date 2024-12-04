import math

# Representación del tablero
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Verificar si alguien ganó
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

# Verificar si hay empate
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Evaluar el estado del tablero
def evaluate(board):
    winner = check_winner(board)
    if winner == "O":  # La máquina gana
        return 1
    elif winner == "X":  # El jugador gana
        return -1
    return 0  # Empate o juego no terminado

# Implementación del algoritmo Minimax
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score != 0 or is_draw(board):
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best_score

# Obtener la mejor jugada
def get_best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Juego principal
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Bienvenido al juego del gato. Tú eres 'X'. ¡Buena suerte!")
    print_board(board)

    while True:
        # Turno del jugador
        while True:
            try:
                move = input("Introduce tu movimiento (formato fila,columna): ")
                x, y = map(int, move.split(","))
                if board[x][y] == " ":
                    board[x][y] = "X"
                    break
                else:
                    print("Posición ocupada. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Movimiento inválido. Intenta de nuevo. Usa el formato fila,columna (por ejemplo, 0,0).")

        print_board(board)

        if check_winner(board) == "X":
            print("¡Felicidades! ¡Has ganado!")
            break
        elif is_draw(board):
            print("Es un empate.")
            break

        # Turno de la máquina
        print("Turno de la máquina...")
        move = get_best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
        print_board(board)

        if check_winner(board) == "O":
            print("La máquina ha ganado. ¡Suerte la próxima vez!")
            break
        elif is_draw(board):
            print("Es un empate.")
            break

# Ejecutar el juego
play_game()
