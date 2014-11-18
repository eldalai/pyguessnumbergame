
from Computer import Computer
import numbersUtil

class Game(object):

	computer = Computer()

	#def __init__(self):
		# todo...

	def playHuman(self):
		#while True:
		humanGuessNumber = self.humanInput()
		humanGoods, humanRegulars = self.computer.play(humanGuessNumber)
		if humanGoods == 4:
			print "human win"
		else:
			print "You have %d goods and %d regulars" % ( humanGoods, humanRegulars )
		return humanGoods, humanRegulars 

	def humanInput(self):
		# human turn
		humanGuessNumber = raw_input("try to guess my number, Enter a 4-digit number without repetition , like '1234 ' or ' 0892 '")
		while not numbersUtil.isCorrect(humanGuessNumber):
			humanGuessNumber = raw_input("WRONG NUMBER! try to guess my number, Enter a 4-digit number without repetition , like '1234 ' or ' 0892 '")
		return humanGuessNumber	
