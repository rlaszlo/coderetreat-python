import unittest
from trivia import Game


class TimeTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.add('Chet')
        self.game.add('Pat')

    def test_game_has_timer(self):
        self.assertIsNotNone(self.game.timer)

    def test_game_timer_changes_after_correct_answer(self):
        timer = self.game.timer
        self.game.roll(4)
        self.game.was_correctly_answered()
        self.assertNotEquals(timer, self.game.timer)

    def test_game_timer_changes_after_wrong_answer(self):
        timer = self.game.timer
        self.game.roll(4)
        self.game.wrong_answer()
        self.assertNotEquals(timer, self.game.timer)
