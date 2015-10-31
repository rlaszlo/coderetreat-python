#!/usr/bin/env python
from player import Player

CATEGORY_ROCK = 'Rock'
CATEGORY_SPORTS = 'Sports'
CATEGORY_SCIENCE = 'Science'
CATEGORY_POP = 'Pop'


class Game:
    def __init__(self):
        self.timer = 0
        self.players = []

        self.questions = {
            CATEGORY_ROCK: [],
            CATEGORY_SPORTS: [],
            CATEGORY_SCIENCE: [],
            CATEGORY_POP: []
        }

        self.place_category = {
            0: CATEGORY_POP,
            4: CATEGORY_POP,
            8: CATEGORY_POP,
            1: CATEGORY_SCIENCE,
            5: CATEGORY_SCIENCE,
            9: CATEGORY_SCIENCE,
            2: CATEGORY_SPORTS,
            6: CATEGORY_SPORTS,
            10: CATEGORY_SPORTS,
        }

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False
        
        for i in range(50):
            for q in self.questions.keys():
                self.questions[q].append("%s Question %s" % (q, i))

    def is_playable(self):
        return self.how_many_players >= 2
    
    def add(self, player_name):
        self.players.append(Player(player_name))

        print player_name + " was added"
        print "They are player number %s" % len(self.players)
        return True
    
    @property
    def how_many_players(self):
        return len(self.players)
    
    def roll(self, roll):
        print "%s is the current player" % self.players[self.current_player].name
        print "They have rolled a %s" % roll
        
        if self.players[self.current_player].in_penalty_box:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True
                
                print "%s is getting out of the penalty box" % self.players[self.current_player].name
                self.step(roll)
            else:
                print "%s is not getting out of the penalty box" % self.players[self.current_player].name
                self.is_getting_out_of_penalty_box = False
        else:
            self.step(roll)

    def step(self, roll):
        self.players[self.current_player].places += roll
        if self.players[self.current_player].places > 11:
            self.players[self.current_player].places -= 12
        print self.players[self.current_player].name + \
              '\'s new location is ' + \
              str(self.players[self.current_player].places)
        print "The category is %s" % self._current_category
        self._ask_question()

    def _ask_question(self):
        print self.questions[self._current_category].pop(0)

    @property
    def _current_category(self):
        place = self.players[self.current_player].places
        return self.place_category.get(place, CATEGORY_ROCK)

    def was_correctly_answered(self):
        if self.players[self.current_player].in_penalty_box:
            if self.is_getting_out_of_penalty_box:
                self.players[self.current_player].in_penalty_box = False
                return self.increase_purses()
            else:
                self.next_player()
                return True
        return self.increase_purses()

    def increase_purses(self):
        print 'Answer was correct!!!!'
        self.players[self.current_player].purses += 1
        print self.players[self.current_player].name + \
              ' now has ' + \
              str(self.players[self.current_player].purses) + \
              ' Gold Coins.'
        winner = self._did_player_win()
        self.step_timer()
        self.next_player()
        return winner

    def step_timer(self):
        self.timer += 1

    def next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

    def wrong_answer(self):
        print 'Question was incorrectly answered'
        print self.players[self.current_player].name + " was sent to the penalty box"
        self.players[self.current_player].in_penalty_box = True

        self.step_timer()
        self.next_player()
        return True
    
    def _did_player_win(self):
        return not (self.players[self.current_player].purses == 6)


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()
        
        if not not_a_winner: break
