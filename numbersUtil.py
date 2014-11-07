
# compare 2 numbers and return how many numbers are in number from other
def goodNumbers(number, other):
	listNumber = list(number)
	listOther = list(other)
	goods = 0
	for indexNumber in xrange(0,4):
		for indexOther in xrange(0,4):
			print " compare (%d) %s with (%d) %s " % (indexNumber, listNumber[indexNumber], indexOther, listOther[indexOther] )
			if listNumber[indexNumber] == listOther[indexOther] and indexNumber == indexOther:
				print "GOOD!"
				goods = goods + 1 
	return goods

# compare 2 numbers and return how many numbers are in number from other
def regularNumbers(number, other):
	listNumber = list(number)
	listOther = list(other)
	regulars = 0
	for indexNumber in xrange(0,4):
		for indexOther in xrange(0,4):
			print " compare (%d) %s with (%d) %s " % (indexNumber, listNumber[indexNumber], indexOther, listOther[indexOther] )
			if listNumber[indexNumber] == listOther[indexOther] and indexNumber != indexOther:
				print "REGULAR!"
				regulars = regulars + 1 
	return regulars

