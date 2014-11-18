
# compare 2 numbers and return how many numbers are in number from other
def goodNumbers(number, other):
	listNumber = list(number)
	listOther = list(other)
	goods = 0
	for indexNumber in xrange(0,4):
		for indexOther in xrange(0,4):
			#print "goods: compare (%d) %s with (%d) %s " % (indexNumber, listNumber[indexNumber], indexOther, listOther[indexOther] )
			if listNumber[indexNumber] == listOther[indexOther] and indexNumber == indexOther:
				#print "GOOD!"
				goods = goods + 1 
	return goods

# compare 2 numbers and return how many numbers are in number from other
def regularNumbers(number, other):
	listNumber = list(number)
	listOther = list(other)
	regulars = 0
	for indexNumber in xrange(0,4):
		for indexOther in xrange(0,4):
			#print "regulars: compare (%d) %s with (%d) %s " % (indexNumber, listNumber[indexNumber], indexOther, listOther[indexOther] )
			if listNumber[indexNumber] == listOther[indexOther] and indexNumber != indexOther:
				#print "REGULAR!"
				regulars = regulars + 1 
	return regulars

def isCorrect(number):
	if len(number) != 4:
		#print "is not Correct, %s is not 4 character long..." % number
		return False
	listNumber = list(number)
	for indexNumber in xrange(0, 3):
		if listNumber[indexNumber] < "0" or listNumber[indexNumber] > "9" :
				#print "is not Correct, %s not a number" % listNumber[indexNumber] 
				return False

		for indexNumber2 in xrange(indexNumber+1, 4):
			#print "isCorrect: compare (%d) %s with (%d) %s " % (indexNumber, listNumber[indexNumber], indexNumber2, listNumber[indexNumber2] )
			if listNumber[indexNumber] == listNumber[indexNumber2] and indexNumber != indexNumber2:
				#print "is not Correct"
				return False
	#print "is correct"
	return True