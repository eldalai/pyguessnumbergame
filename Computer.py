import random
import numbersUtil

class Computer(object):

	guessNumber = ""

	def __init__(self):
		self.guessNumber = self.generatePosibleNumber()
		while not numbersUtil.isCorrect(self.guessNumber):
			self.guessNumber = self.generatePosibleNumber()

	def generatePosibleNumber(self):
		posibleGuessNumber = str(random.randint(123, 9876))
		if len(posibleGuessNumber) < 4 :
			posibleGuessNumber = "0" + posibleGuessNumber
		return posibleGuessNumber

	def setNumber(self, number):
		self.guessNumber = number

	def play(self, number):
		goods = numbersUtil.goodNumbers(self.guessNumber, number)
		regulars = numbersUtil.regularNumbers(self.guessNumber, number)

		return goods, regulars