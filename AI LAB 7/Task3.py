import copy

pieceValues = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 1000}

def initializeBoard():
    return [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    ]

def printBoard(board):
    for row in board:
        print(" ".join(row))
    print()

def getPieceValue(piece):
    return pieceValues.get(piece.upper(), 0)

def evaluateBoard(board):
    score = 0
    for row in board:
        for piece in row:
            if piece.isupper():
                score += getPieceValue(piece)
            elif piece.islower():
                score -= getPieceValue(piece)
    return score

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluateBoard(board)
    
    if maximizing:
        maxEval = float('-inf')
        for move in generateMoves(board, 'white'):
            newBoard = applyMove(board, move)
            eval = minimax(newBoard, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for move in generateMoves(board, 'black'):
            newBoard = applyMove(board, move)
            eval = minimax(newBoard, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

def generateMoves(board, color):
    moves = []
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if (color == 'white' and piece.isupper()) or (color == 'black' and piece.islower()):
                moves.extend(getPieceMoves(board, r, c, piece))
    return moves

def getPieceMoves(board, r, c, piece):
    moves = []
    directions = {
        'P': [(1, 0), (2, 0)],
        'p': [(-1, 0), (-2, 0)],
        'N': [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)],
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'R': [(1, 0), (-1, 0), (0, 1), (0, -1)],
        'Q': [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)],
        'K': [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    }
    if piece.upper() in directions:
        for dr, dc in directions[piece.upper()]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == '.' or (board[nr][nc].isupper() != piece.isupper()):
                    moves.append(((r, c), (nr, nc)))
    return moves

def applyMove(board, move):
    newBoard = copy.deepcopy(board)
    (r1, c1), (r2, c2) = move
    newBoard[r2][c2] = newBoard[r1][c1]
    newBoard[r1][c1] = '.'
    return newBoard

def playChess():
    board = initializeBoard()
    printBoard(board)
    
    while True:
        move = input("ENTER YOUR MOVE: ").strip().split()
        if len(move) != 2:
            print("INVALID ATTEMPT! TRY AGAIN")
            continue
        
        start = (8 - int(move[0][1]), ord(move[0][0]) - ord('a'))
        end = (8 - int(move[1][1]), ord(move[1][0]) - ord('a'))
        
        if (start, end) in generateMoves(board, 'white'):
            board = applyMove(board, (start, end))
        else:
            print("INVALID ATTEMPT! TRY AGAIN")
            continue
        
        printBoard(board)
        
        print("AI is thinking...")
        aiMove = bestMove(board, 3, 'black')
        if aiMove is None:
            print("YOU WIN!")
            break
        
        board = applyMove(board, aiMove)
        printBoard(board)
        print("AI MOVED!")

playChess()
