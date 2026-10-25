class Abastecimento:
    def __init__(self, veiculo, combustivel, valor):
        self.veiculo = veiculo
        self.combustivel = combustivel
        self.valor = valor

    def mostrar_abastecimento(self):
        print(
            f"{self.veiculo} | "
            f"Combustível: {self.combustivel} | "
            f"Valor: R$ {self.valor:.2f}"
        )

    def ler_recibo(self):
        with open("recibo_posto.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        print(conteudo)