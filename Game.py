
from Computer import Computer
from Human import Human

class Game(object):

	computer = Computer()
	human = Human()


	def __init__(self):
		self.computer.oponent(self.human) 
		self.human.oponent(self.computer)
		
	def play(self):
		game_end = False
		player_turn = self.human
		while not game_end:	
			game_end = player_turn.play()
			player_turn = player_turn.oponent()


if __name__ == "__main__":
	game = Game()
	game.play()
	