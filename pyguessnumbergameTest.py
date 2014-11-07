'''
@author: gabriel.flores
'''

import unittest
import numbersUtil

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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()    	