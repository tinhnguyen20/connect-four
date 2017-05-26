from ai import Player, ComputerPlayer

RED_PLAYER = 'x'
BLUE_PLAYER = 'o'
NUM_COLUMNS = 7
NUM_ROWS = 6


class Board():
    """
        A represenation of a Connect-Four board state.

        Example board.
        _ _ _ _ _ _ _
        _ _ _ _ _ _ _
        _ _ _ _ _ _ _
        _ _ _ r _ _ _
        _ _ r b _ _ _
        _ r b r b _ _
        0 1 2 3 4 5 6

        Consists of two players: Player_1(r), Player_2(b)
    """
    def __init__(self, board=None, player1=None, player2=None):
        """
            initializes the board. 6 rows
        """
        if board is None:
            self.board = [Column() for x in range(NUM_COLUMNS)]
        else:
            self.board = board
        self.player1 = player1
        self.player2 = player2

    def simulateMove(self, move, player):
        """
            Returns a new board object, having taken the move

            move - desired column to put piece [0-6]
            player - Player
        """
        new_board = Board(self.board)
        new_board.place_piece(move, player)
        return new_board

    def __str__(self):
        s = ""
        for row in range(5, -1, -1):
            for col in self.board:
                s += (col.to_array()[row] + " ")
            s += "\n"

        for col_num in range(NUM_COLUMNS):
            s += str(col_num) + " "
        return s

    def to_array(self):
        """
            Returns a two dimensional array.
            arr[col][row]
        """
        return [col.to_array() for col in self.board]

    def isColumnFull(self, colNum):
        return len(self.board[colNum].data) == NUM_ROWS

    def getColumn(self, colNum):
        return self.board[colNum]

    def getPoint(self, point):
        return self.getColumn(point[0]).get(point[1])

    def is_won(self):
        """
            Returns None when no player has won.
            Returns RED_PLAYER/BLUE_PLAYER if they won.
        """
        arr = self.to_array()
        # check verticals
        for col in self.board:
            win = col.has_won_straight()
            if win:
                return win
        # check horizontals
        for row in range(NUM_ROWS):
            s = ""
            for col in range(NUM_COLUMNS):
                s += arr[col][row]
            if self.player1.getWinString() in s:
                return self.player1
            if self.player2.getWinString() in s:
                return self.player2

        diagonals = self.populateDiagonals()
        for diag in diagonals:
            if self.player1.getWinString() in diag:
                return self.player1
            if self.player2.getWinString() in diag:
                return self.player2

        return None

    def place_piece(self, col_num, player):
        """
            Places piece into the column
        """
        assert col_num >= 0 and col_num < NUM_COLUMNS
        column = self.board[col_num]
        column.push(player)

    def populateDiagonals(self):
        """
            Returns a list of strings representing all the diagonals in the
            game. A win has 'rrrr' or 'bbbb'.
        """
        lst = []
        leftStartingPoints = [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0)]
        for point in leftStartingPoints:
            p = point
            s = ""
            while not outOfBounds(p):
                s += self.getPoint(p)
                p = (p[0] + 1, p[1] + 1)
            lst.append(s)

        rightStartingPoints = [(0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5)]
        for point in rightStartingPoints:
            p = point
            s = ""
            while not outOfBounds(p):
                s += self.getPoint(p)
                p = (p[0] + 1, p[1] - 1)
            lst.append(s)
        return lst

    def getLegalActions(self):
        """
            returns an int - [0,6]
        """
        return [i for i in range(NUM_COLUMNS) if (not self.isColumnFull(i))]


class Column():
    def __init__(self):
        self.data = ['_' for _ in range(NUM_ROWS)]
        self.num_pieces = 0

    def push(self, player):
        if self.num_pieces == NUM_ROWS:
            print("Cannot place piece here, Column already filled.")
        else:
            self.data[self.num_pieces] = player.side
            self.num_pieces += 1

    def to_array(self):
        return self.data

    def get(self, index):
        return self.data[index]

    def __str__(self):
        s = ""
        for val in self.data:
            s += val
        return s

    def has_won_straight(self):
        """
            Should not happen. lul.
            Returns None when no player has won.
            Returns RED_PLAYER/BLUE_PLAYER if they won.
        """
        s = ""
        for val in self.data:
            s += val
        if 'bbbb' in s:
            return BLUE_PLAYER
        if 'rrrr' in s:
            return RED_PLAYER
        else:
            return None


def outOfBounds(pos):
        """
        Takes in a tuple (col, row) and checks if it is out of bounds.
        """
        if 0 <= pos[0] and pos[0] <= 6:
            if 0 <= pos[1] and pos[1] <= 5:
                return False
        return True


# 7 columns - 6 rows
def start_game():
    """
        Use input("Input message.")
    """
    redPlayer = Player(side=RED_PLAYER)
    bluePlayer = Player(side=BLUE_PLAYER)
    board = Board(player1=redPlayer, player2=bluePlayer)

    currentPlayer = redPlayer
    while not board.is_won():
        print("")
        print(board)
        currentPlayer.makeMove(board)
        if currentPlayer.side == RED_PLAYER:
            currentPlayer = bluePlayer
        else:
            currentPlayer = redPlayer

    print(board)
    print(currentPlayer.switch() + " wins!")


start_game()
