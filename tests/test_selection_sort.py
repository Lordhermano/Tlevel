import unittest
from mathTL import MathTL

#the parent class for this test refers back to MATHTL Class in it's method
class Test_selection_sort(unittest.TestCase):
   def test_float(self):
        result=MathTL.Selection_sort([9.0,5.5,3.3,6,0])
        self.assertEqual(result,[0,3.3,5.5,6,9.0])
   def test_neg(self):
        result=MathTL.Selection_sort([-2,4,6,0])
        self.assertEqual(result,[-2,0,4,6])
   def test_dups(self):
        result=MathTL.Selection_sort([2,2,2,5,7,1,-9])
        self.assertEqual(result,[-9,1,2,2,2,5,7])
   def test_string(self):
        result=MathTL.Selection_sort(['d','f','g','a','b'] )
        self.assertEqual(result,['a','b','d','f','g'])
if __name__=='main':
    unittest.main()  