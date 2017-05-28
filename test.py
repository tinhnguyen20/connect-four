# test file for connect-four
from ai import *
from board import Board
from player import Player, ComputerPlayer

import unittest


PLAYER1 = 'x'
PLAYER2 = 'o'


class GameTestCase(unittest.TestCase):
    def setUp(self):
        redPlayer = Player(side=PLAYER1, name='player1')
        bluePlayer = Player(side=PLAYER2, name='player2')
        board = Board(player1=redPlayer, player2=bluePlayer)
        return board, redPlayer, bluePlayer

    def testVerticalWin(self):
        board, player1, player2 = self.setUp()
        for i in range(4):
            board = board.simulateMove(0, player1)
            board = board.simulateMove(1, player2)
        w = board.is_won()
        self.assertTrue(player1, w)

    def testHorizontalWin(self):
        board, player1, player2 = self.setUp()
        for i in range(4):
            board = board.simulateMove(i, player1)
            board = board.simulateMove(i, player2)
        w = board.is_won()
        self.assertEqual(player1, w)


if __name__ == '__main__':
    unittest.main()
