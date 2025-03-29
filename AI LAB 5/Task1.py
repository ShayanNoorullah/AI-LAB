class ChessBoard:
    pieceValues = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 100,'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -100}
    def __init__(self):
        self.board = self.createInitialBoard()
        self.currentPlayer = 'w'
    def createInitialBoard(self):
        return [
            list("rnbqkbnr"),
            list("pppppppp"),
            [" " for _ in range(8)],
            [" " for _ in range(8)],
            [" " for _ in range(8)],
            [" " for _ in range(8)],
            list("PPPPPPPP"),
            list("RNBQKBNR")
        ]

    def getLegalMoves(self):
        return [(6, 4, 4, 4)]

    def makeMove(self, move):
        newBoard = ChessBoard()
        newBoard.board = [row[:] for row in self.board]
        fromX, fromY, toX, toY = move
        newBoard.board[toX][toY] = newBoard.board[fromX][fromY]
        newBoard.board[fromX][fromY] = " "
        return newBoard

    def evaluate(self):
        score = 0
        for row in self.board:
            for piece in row:
                if piece in self.pieceValues:
                    score += self.pieceValues[piece]
        return score

def beamSearch(board, beamWidth=3, depthLimit=3):
    beam = [(board, [], board.evaluate())]
    

    for _ in range(depthLimit):
        candidates = []
        for state, moves, _ in beam:
            legalMoves = state.getLegalMoves()
            for move in legalMoves:
                newBoard = state.makeMove(move)
                score = newBoard.evaluate()
                candidates.append((newBoard, moves + [move], score))
        if not candidates:
            break
        beam = sorted(candidates, key=lambda x: x[2], reverse=True)[:beamWidth]
    return beam[0][1], beam[0][2]





if __name__ == "__main__":
    board = ChessBoard()
    bestMoves, score = beamSearch(board, beamWidth=3, depthLimit=3)
    print("BEST MOVE SEQUENCE IS:", bestMoves)
    print("EVALUATION SCORE IS:", score)
