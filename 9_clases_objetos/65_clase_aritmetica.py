class Aritmetica:
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB



def __main__():
    aritmetica1 = Aritmetica(5,3)

    print(f'suma: {aritmetica1.sumar()}')
    print(f'resta: {aritmetica1.restar()}')
    print(f'multiplicar: {aritmetica1.multiplicar()}')
    print(f'dividir: {aritmetica1.dividir():.2f}')


__main__()
