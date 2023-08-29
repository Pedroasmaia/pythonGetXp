class Carros:
    def __init__(self):
        self.pneus = 4
        self.estepe = 1
    motor = None
    def total_pneus(self):
        total = self.pneus + self.estepe
        print(f'Seu carro tem {total} pneus')


ferrari = Carros()
ferrari.estepe = 2
ferrari.total_pneus()
ferrari.estepe()