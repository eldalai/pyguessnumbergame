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


    def testCompareNumbers(self):
    	mynumber = "1234"
    	otherQuestion = "1235"
    	goodNumbers = numbersUtil.goodNumbers(mynumber, otherQuestion)
    	self.assertEqual(3, goodNumbers, "shoud be 3 good Numbers because 1, 2 and 3 are in good place")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()    	