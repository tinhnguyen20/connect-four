from ai import MinimaxAgent

PLAYER1 = 'x'
PLAYER2 = 'o'


class Player():
    """
        side: 'x', 'o'
    """
    def __init__(self, side=PLAYER1, name=None):
        self.side = side
        self.name = name

    def __eq__(self, other):
        # print(self.side, other)
        return self.side == other.side

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
    def __init__(self, depth, side):
        super(side, name=self.getName())
        self.depth = depth
        self.agent = MinimaxAgent(self.depth, me=self)

    def makeMove(self, board):
        # build game tree
        return self.agent.getMove(board)

    def getName(self):
        return "COMPUTER - " + str(self.depth) + self.side
