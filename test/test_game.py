import unittest
from trivia import Game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.add('Chet')

    def test_player_put_in_penalty_box(self):
        self.game.wrong_answer()
        self.assertTrue(self.game.in_penalty_box[0])

    def test_player_gets_out_of_penalty_box_on_odd_roll(self):
        self.game.wrong_answer()
        self.game.roll(1)
        self.game.was_correctly_answered()
        self.assertFalse(self.game.in_penalty_box[0])

    def test_player_does_not_gets_out_of_penalty_box_on_even_roll(self):
        self.game.wrong_answer()
        self.game.roll(2)
        self.game.was_correctly_answered()
        self.assertTrue(self.game.in_penalty_box[0])
