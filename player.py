
class Player(object):

	def play(self):
		''' Return player win!
		''' 
		print str(self) + ' dont support play()... turn missed' 
		return False

	def ask(self, number):
		return 0, 0

	def oponent(self, value=None):
		if value is None:
			return self._oponent
		else:
			self._oponent = value
		