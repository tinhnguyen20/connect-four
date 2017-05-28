BIG_NUM = 9999999999


def evaluationFunction(board, player):
    """
        Evaluation for board from <player> perspective
    """
    if board.is_won():
        pass
    pass


class Agent:
    def __init__(self, depth, me=None):
        self.depth = depth
        self.me = me

    def getMove(self):
        raise Exception("Not Defined")


class MinimaxAgent(Agent):
    """
        ideas learned from cs188 (uc Berkeley)
    """
    def getMove(self, board):
        d = {}  # holds {value:move}
        for col in board.getLegalActions():
            nextBoard = board.simulateMove(col, self.me)
            value = self.minVal(nextBoard, self.depth)
            d[value] = col
        return d[max(d.keys())]

    def minVal(self, board, depth):
        other = board.player1 if self.me is board.player2 else board.player2
        winner = board.is_won()
        if winner is not None:
            return evaluationFunction(board, self.me)

        v = BIG_NUM
        for col in board.getLegalActions():
            nextBoard = board.simulateMove(col, other)
            v = min(v, self.maxVal(nextBoard, depth - 1))
        return v

    def maxVal(self, board, depth):
        if depth == 0:
            return evaluationFunction(board, self.me)
        winner = board.is_won()
        if winner is not None:
            return evaluationFunction(board, self.me)
        v = -BIG_NUM
        legalMoves = board.getLegalActions()
        for move in legalMoves:
            nextBoard = board.simulateMove(move, self.me)
            v = max(v, self.minVal(nextBoard, depth))
        return v
