PLAYER1 = 'x'
PLAYER2 = 'o'
NUM_COLUMNS = 7
NUM_ROWS = 6


def evaluationFunction(board):
    pass


class Player():
    """
        side: 'x', 'o'
    """
    def __init__(self, side=PLAYER1, name=None):
        self.side = side
        self.name = name

    def getName(self):
        if self.name:
            return self.name
        if self.side == 'x':
            return 'PLAYER1'
        else:
            return 'PLAYER2'

    def switch(self):
        """
            For win message purposes
        """
        if self.side == 'o':
            return 'PLAYER1'
        else:
            return 'PLAYER2'

    def getWinString(self):
        return 4*self.side

    def makeMove(self, board):
        """
            Prompts the user for a move and makes the move
            on the board.
        """
        pos = input(self.getName() +
                    ", please choose a column to place a piece: ")
        board.place_piece(int(pos), self)


class ComputerPlayer(Player):
    """
        difficulty - number (how many moves AI looks ahead)
    """
    def __init__(self, depth):
        self.depth = depth
        self.agent = MinimaxAgent(self.depth, me=self)

    def makeMove(self, board):
        # build game tree
        return self.agent.getMove(board)

    def getName(self):
        return "ROBOT - " + str(self.depth)


class Agent:
    def __init__(self, depth, me=None):
        self.depth = depth
        self.me = me

    def getMove(self):
        raise Exception("Not Defined")


class MinimaxAgent(Agent):
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
            return evaluationFunction(board)

        v = 999999999999
        for col in board.getLegalActions():
            nextBoard = board.simulateMove()

    def maxVal(self, board, depth):
        # if d == 0:
        #   return self.evaluationFunction(state)
        # if state.isLose() or state.isWin():
        #   return self.evaluationFunction(state)
        # # pacman is 0
        # v = -9999999999
        # legalMoves = state.getLegalActions(0)
        # for move in legalMoves:
        #   successor = state.generateSuccessor(0, move)
        #   v = max(v, self.minValue(successor, 1, d))
        # return v
        pass