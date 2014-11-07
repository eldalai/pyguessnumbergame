'''
@author: gabriel.flores
'''

import unittest
import numbersUtil
from Computer import Computer

class Test(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCompareGoodNumbers(self):
    	mynumber = "1234"
    	otherQuestion = "1253"
    	goodNumbers = numbersUtil.goodNumbers(mynumber, otherQuestion)
    	self.assertEqual(2, goodNumbers, "shoud be 2 good Numbers because 1 and 2 are in good place")

    def testCompareRegularNumbers(self):
    	mynumber = "1234"
    	otherQuestion = "0124"
    	goodNumbers = numbersUtil.regularNumbers(mynumber, otherQuestion)
    	self.assertEqual(2, goodNumbers, "shoud be 2 good Numbers because 1 and 2 are not in good place")

    def testNumberIsCorrect(self):
    	number = "1232"
    	self.assertFalse( numbersUtil.isCorrect( number ) )	
    	number = "4234"
    	self.assertFalse( numbersUtil.isCorrect( number ) )	
    	number = "1234"
    	self.assertTrue( numbersUtil.isCorrect( number ) )	
    	number = "1A34"
    	self.assertFalse( numbersUtil.isCorrect( number ) )	

    	number = "134"
    	self.assertFalse( numbersUtil.isCorrect( number ) )	
    	number = "13456"
    	self.assertFalse( numbersUtil.isCorrect( number ) )	

    def testPlayWithComputer(self):
    	computer = Computer()
    	computer.setNumber("1234")

    	goods, regulars = computer.play("1567") # 1 good
    	self.assertEqual(1, goods)
    	self.assertEqual(0, regulars)
    	goods, regulars = computer.play("0356") # 1 regular
    	self.assertEqual(0, goods)
    	self.assertEqual(1, regulars)
    	goods, regulars = computer.play("9831") # 1 good and 1 regular
    	self.assertEqual(1, goods)
    	self.assertEqual(1, regulars)
    	goods, regulars = computer.play("1243") # 2 goods and 2 regulars
    	self.assertEqual(2, goods)
    	self.assertEqual(2, regulars)
    	goods, regulars = computer.play("1234") # 4 goods and you win!
    	self.assertEqual(4, goods)
    	self.assertEqual(0, regulars)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()    	