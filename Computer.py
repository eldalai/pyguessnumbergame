import random
import numbersUtil
from player import Player

class Computer(Player):

	guessNumber = ""
	asked = []
	def __init__(self):
		self.first_number = self._generatePosibleNumber()

	def play(self):
		if len(self.asked) == 0:
			number_to_ask = self.first_number
		else:	
			number_to_ask = self.calculate_next_ask()

		goods, regulars = self.oponent().ask(number_to_ask)

		self.asked.append( ( number_to_ask, goods, regulars) )
		return goods == 4

	def calculate_next_ask(self):
		for int_posible_number in xrange(123, 9876):
			posible_number =  "%04d" % int_posible_number
			if numbersUtil.isCorrect(posible_number):
				some_number_dont_match = False
				for number, goods, regulars in self.asked:
					goods_posible = numbersUtil.goodNumbers(posible_number, number)
					regulars_posible = numbersUtil.regularNumbers(posible_number, number)
					if goods_posible != goods \
					or regulars_posible != regulars:
						some_number_dont_match = True
				if not some_number_dont_match:
					return posible_number
		raise Error()


	def generateNumber(self):
		self.guessNumber = self._generatePosibleNumber()
		while not numbersUtil.isCorrect(self.guessNumber):
			self.guessNumber = self._generatePosibleNumber()
		print "Cheat: Computer's guessNumber is %s" % self.guessNumber	

	def _generatePosibleNumber(self):
		posibleGuessNumber = str(random.randint(123, 9876))
		if len(posibleGuessNumber) < 4 :
			posibleGuessNumber = "0" + posibleGuessNumber
		return posibleGuessNumber

	def setNumber(self, number):
		self.guessNumber = number

	def ask(self, number):
		if self.guessNumber == "":
			self.generateNumber()
		goods = numbersUtil.goodNumbers(self.guessNumber, number)
		regulars = numbersUtil.regularNumbers(self.guessNumber, number)

		return goods, regulars