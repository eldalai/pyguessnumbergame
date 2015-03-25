from player import Player
import numbersUtil

class Human(Player):

	def play(self):
		#while True:
		humanGuessNumber = self.humanInput()
		humanGoods, humanRegulars = self.oponent().ask(humanGuessNumber)
		if humanGoods == 4:
			print "human win"
			return True

		print "You have %d goods and %d regulars" % ( humanGoods, humanRegulars )
		return False
		#return humanGoods, humanRegulars 

	def humanInput(self):
		# human turn
		humanGuessNumber = raw_input("try to guess my number, Enter a 4-digit number without repetition , like '1234 ' or ' 0892 ': ")
		while not numbersUtil.isCorrect(humanGuessNumber):
			humanGuessNumber = raw_input("WRONG NUMBER! try to guess my number, Enter a 4-digit number without repetition , like '1234 ' or ' 0892 ': ")
		return humanGuessNumber	

	def ask(self, number):
		goods = int(raw_input("How many goods has %s " % number))
		regulars = int(raw_input("How many regular has %s " % number))

		return goods, regulars	
