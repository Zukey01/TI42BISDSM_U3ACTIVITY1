#Importacion del modulo unittest para poder ralizar pruebas unitarias

import unittest 
#importacion de la clase calculadora desde el archivo calculadora.py
from calculadora import Calculadora

#Definicion de la clase de pruebas que hereda de unittest.Testcase 
class TestCalculadora(unittest.TestCase):
        #metodo que se ejecuta anres de cada prueba
        def setUp(self):
            self.calc = Calculadora()
            
        #Pruebas del metodo suma
        def test_suma(self):
            #Prueba la suma de dos numeros positivos 
            self.assertEqual(self.calc.suma(5,2),7)
            #prueba la suma de dos ceros
            self.assertEqual(self.calc.suma(0,0),0)
            
#Bloque condicional que permite ejecutar las pruebas directamente

if __name__ == '__main__':
    #inicializar la ejecucion de todas las pruebas definidas de la clase
    unittest.main()