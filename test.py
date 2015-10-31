from trivia import Game

with open('randomSeq.txt') as f:
    f.readline()
    winner_range = f.readline().strip().split(',')[:-1]
    winner_range.reverse()
    f.readline()
    f.readline()
    rolls = f.readline().strip().split(',')[:-1]
    rolls.reverse()

game = Game()

game.add('Chet')
game.add('Pat')
game.add('Sue')

while True:
    game.roll(int(rolls.pop()))

    if int(winner_range.pop()) == 7:
        not_a_winner = game.wrong_answer()
    else:
        not_a_winner = game.was_correctly_answered()

    if not not_a_winner: break
