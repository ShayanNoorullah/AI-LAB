import math

def printBoard(board):
    for row in board:
        print(" | ".join(row))
    print()

def checkWinner(board):
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

def isFull(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, isMaximizing):
    winner = checkWinner(board)
    if winner == "X":
        return 10 - depth
    elif winner == "O":
        return depth - 10
    elif isFull(board):
        return 0

    if isMaximizing:
        bestScore = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    bestScore = min(bestScore, score)
        return bestScore

def bestMove(board):
    bestScore = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = (i, j)
    return move

def playGame():
    board = [[" " for _ in range(3)] for _ in range(3)]
    printBoard(board)
    
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2): ").split())
        except ValueError:
            print("Invalid input. Enter two numbers between 0 and 2.")
            continue
        
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        
        board[row][col] = "O"
        printBoard(board)
        
        if checkWinner(board):
            print("You win!")
            break
        if isFull(board):
            print("It's a draw!")
            break
        
        print("AI's turn...")
        aiMove = bestMove(board)
        board[aiMove[0]][aiMove[1]] = "X"
        printBoard(board)
        
        if checkWinner(board):
            print("AI wins!")
            break
        if isFull(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    playGame()
