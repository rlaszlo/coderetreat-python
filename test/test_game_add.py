import unittest
from trivia import Game


class GameAddTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_6_players_can_play(self):
        self.game.add('1')
        self.game.add('2')
        self.game.add('3')
        self.game.add('4')
        self.game.add('5')
        self.game.add('6')

    def test_8_players_can_play(self):
        self.game.add('1')
        self.game.add('2')
        self.game.add('3')
        self.game.add('4')
        self.game.add('5')
        self.game.add('6')
        self.game.add('7')
        self.game.add('8')
