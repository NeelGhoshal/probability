import unittest
import Backtracking


class TestBacktracking(unittest.TestCase):
    


    def test_ndegree(self):
         self.assertEqual(Backtracking.backtracking
                          (lambda x: x**2 +3*x, lambda x: 2*x + 3,11), 0.49984899999999993)
         
         self.assertEqual(Backtracking.backtracking
                          (lambda x: x**10 +3*x, lambda x: 10*(x**9) + 3,2), 6.07776055631376e-05)
         
         self.assertEqual(Backtracking.backtracking
                          (lambda x: x**5 - 3*x, lambda x: 5*(x**4) - 3,2),1)
       
if __name__ == '__main__':
    unittest.main()