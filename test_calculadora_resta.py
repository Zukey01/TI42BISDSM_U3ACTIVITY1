import unittest

from calculadora import Calculadoraresta

class Testcalculadoraresta(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadoraresta()
        
        def test_resta(self):
            self.assertEqual(self.calc.resta(5,2),3)
            
            self.assertEqual(self.calc.resta(0,0),0)
            
if __name__ == '__main__':
    
    unittest.main()

