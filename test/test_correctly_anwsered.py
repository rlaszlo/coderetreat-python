import unittest
from trivia import Game


class CorrectlyAnsweredTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.add('Chet')

    def test_player_not_in_penalty(self):
        self.game.was_correctly_answered()
        self.assertEqual(self.game.purses[0], 1)

    def test_player_in_penalty_not_getting_out(self):
        self.game.in_penalty_box[0] = True
        self.game.is_getting_out_of_penalty_box = False
        self.game.was_correctly_answered()
        self.assertEqual(self.game.purses[0], 0)

    def test_player_in_penalty_and_getting_out(self):
        self.game.in_penalty_box[0] = True
        self.game.is_getting_out_of_penalty_box = True
        self.game.was_correctly_answered()
        self.assertEqual(self.game.purses[0], 1)
