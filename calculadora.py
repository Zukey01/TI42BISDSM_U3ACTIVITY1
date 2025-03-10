class Calculadora:
    def suma(self, a, b):
        return a + b 

class Calculadoraresta(Calculadora):  # Hereda de Calculadora
    def resta(self, c, d):
        return c - d

class Calculadoraigual:
    def igual(self, e,f):
        return e == f 