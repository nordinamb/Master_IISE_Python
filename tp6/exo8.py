import unittest
from exo1 import safe_division

class TestDivision (unittest.TestCase) :
    def test_zero_division(self) :
        with self.assertRaises(ZeroDivisionError) :
            safe_division(10,0)
            
if __name__ == '__main__' :
    unittest.main()