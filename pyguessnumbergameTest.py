'''
@author: gabriel.flores
'''

import unittest
import numbersUtil
import mock
from Computer import Computer
from Game import Game
import random

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
    	self.assertFalse(numbersUtil.isCorrect(number))	
    	number = "4234"
    	self.assertFalse(numbersUtil.isCorrect(number))	
    	number = "1234"
    	self.assertTrue(numbersUtil.isCorrect(number))	
    	number = "1A34"
    	self.assertFalse(numbersUtil.isCorrect(number))	

    	number = "134"
    	self.assertFalse(numbersUtil.isCorrect(number))	
    	number = "13456"
    	self.assertFalse(numbersUtil.isCorrect(number))	

    def testPlayWithComputer(self):
        print "testPlayWithComputer"
        with mock.patch('Computer.Computer.generatePosibleNumber', return_value='1234'):
            computer = Computer()
            # computer.setNumber("1234")
            goods, regulars = computer.play("1567")  # 1 good
            self.assertEqual(1, goods)
            self.assertEqual(0, regulars)
            goods, regulars = computer.play("0356")  # 1 regular
            self.assertEqual(0, goods)
            self.assertEqual(1, regulars)
            goods, regulars = computer.play("9831")  # 1 good and 1 regular
            self.assertEqual(1, goods)
            self.assertEqual(1, regulars)
            goods, regulars = computer.play("1243")  # 2 goods and 2 regulars
            self.assertEqual(2, goods)
            self.assertEqual(2, regulars)
            goods, regulars = computer.play("1234")  # 4 goods and you win!
            self.assertEqual(4, goods)
            self.assertEqual(0, regulars)

    def testPlayGameWithComputer(self):
        print "testPlayGameWithComputer"
        
        with mock.patch('Game.Computer.Computer.generatePosibleNumber', return_value='1234'):
            game = Game()
        with mock.patch('__builtin__.raw_input', return_value='1234'):
            humanGoods, humanRegulars = game.playHuman()
            self.assertEqual(4, humanGoods)
            self.assertEqual(0, humanRegulars)
            

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()    	
