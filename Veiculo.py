class Veiculo:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __str__(self):
        return f"{self.modelo} - Placa: {self.placa}"