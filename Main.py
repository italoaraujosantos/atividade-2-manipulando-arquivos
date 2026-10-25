from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento

# ==========================================
# COMBUSTÍVEIS
# ==========================================
etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")

# ==========================================
# VEÍCULOS
# ==========================================
carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")

caminhao = Veiculo("Caminhão", "JKL-3456")
onibus = Veiculo("Ônibus", "MNO-7890")
pickup = Veiculo("Picape", "PQR-1234")
taxi = Veiculo("Táxi", "STU-5678")
ambulancia = Veiculo("Ambulância", "VWX-9012")

# ==========================================
# ABASTECIMENTOS
# ==========================================
abastecimento1 = Abastecimento(carro,etanol,50)
abastecimento2 = Abastecimento(moto,gasolina,25)
abastecimento3 = Abastecimento(van,diesel,200)

abastecimento4 = Abastecimento(caminhao, diesel, 350)
abastecimento5 = Abastecimento(onibus, diesel, 400)
abastecimento6 = Abastecimento(pickup, gasolina, 150)
abastecimento7 = Abastecimento(taxi, gasolina, 80)
abastecimento8 = Abastecimento(ambulancia, etanol, 100)

# ==========================================
# LISTA DE ABASTECIMENTOS
# ==========================================
abastecimentos = [
    abastecimento1,
    abastecimento2,
    abastecimento3,
    abastecimento4,
    abastecimento5,
    abastecimento6,
    abastecimento7,
    abastecimento8
]

# ==========================================
# MOSTRANDO OS ABASTECIMENTOS
# ==========================================
print("========== ABASTECIMENTOS DO DIA ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()

# ==========================================
# TOTAL DE VENDAS POR COMBUSTÍVEL
# ==========================================
total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:
    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor
    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor
    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor

# ==========================================
# TOTAL DO DIA
# ==========================================
total_dia = (total_etanol + total_gasolina + total_diesel)

# ======================================
# GERANDO Arquivo recibo.txt
# ======================================

with open('recibo_posto.txt', 'w', encoding="utf-8") as arquivo:
    arquivo.write(f'=========== POSTO DE GASOLINA ====================\n')
    for abastecimento in abastecimentos:
        arquivo.write(f'{abastecimento.veiculo.modelo}'
                      f'{abastecimento.veiculo.placa}\n')
        arquivo.write(f'Combustível: {abastecimento.combustivel.nome}\n')
        arquivo.write(f'Valor R$ {abastecimento.valor}\n')

    arquivo.write("========================================\n")
    arquivo.write(f"Etanol: R$ {total_etanol:.2f}\n")
    arquivo.write(f"Gasolina: R$ {total_gasolina:.2f}\n")
    arquivo.write(f"Diesel: R$ {total_diesel:.2f}\n")
    arquivo.write(f"TOTAL DO DIA: R$ {total_dia:.2f}\n")

# ==========================================
# LENDO O RECIBO
# ==========================================

for abastecimento in abastecimentos:
    abastecimento.ler_recibo()