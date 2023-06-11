import datetime

from conexao import *

from startup import *

from create import *
from read import *
from update import *
from delete import *

def exibir_tabela(tabela):
    if len(tabela) == 0:
        print("Nenhum registro encontrado.")
    else:
        for registro in tabela:
            print(registro)
        print()


# Criação das tabelas
criar_tabelas()

# Inserção de marcas
inserir_marca("Ford")
inserir_marca("Chevrolet")
inserir_marca("Volkswagen")

# Inserção de modelos
inserir_modelo(1, "Fiesta")
inserir_modelo(1, "Focus")
inserir_modelo(2, "Cruze")
inserir_modelo(2, "Onix")
inserir_modelo(3, "Gol")
inserir_modelo(3, "Polo")

# Inserção de carros
inserir_carro(1, "Carro 1", 123456, "ABC123", 25000.0, 2018)
inserir_carro(2, "Carro 2", 789012, "XYZ789", 30000.0, 2019)
inserir_carro(3, "Carro 3", 345678, "DEF456", 35000.0, 2020)

# Obtendo todas as marcas
print("Todas as marcas:")
marcas = obter_marcas()
exibir_tabela(marcas)

# Obtendo todos os modelos de uma marca
id_marca = 1  # ID da marca desejada
print(f"Modelos da marca com ID {id_marca}:")
modelos = obter_modelos_por_marca(id_marca)
exibir_tabela(modelos)

# Obtendo todos os carros
print("Todos os carros:")
carros = obter_carros()
exibir_tabela(carros)

# Obtendo informações de um carro específico pelo ID
id_carro = 2  # ID do carro desejado
carro = obter_carro_por_id(id_carro)
print(f"Informações do carro com ID {id_carro}:")
exibir_tabela([carro])

# Obtendo modelos e carros de uma marca específica
id_marca = 2  # ID da marca desejada
print(f"Modelos e carros da marca com ID {id_marca}:")
modelos_carros = obter_modelos_e_carros_por_marca(id_marca)
exibir_tabela(modelos_carros)

# Atualizando um carro
id_carro = 1  # ID do carro a ser atualizado
nome = "Novo Nome"
renavam = 987654321
placa = "XYZ987"
valor = 28000.0
ano = datetime(2022, 1, 1).date()

atualizar_carro(id_carro, nome, renavam, placa, valor, ano)

# Atualizando uma marca
id_marca = 1  # ID da marca a ser atualizada
nome_marca = "Nova Marca"

atualizar_marca(id_marca, nome_marca)

# Atualizando um modelo
id_modelo = 2  # ID do modelo a ser atualizado
nome_modelo = "Novo Modelo"

atualizar_modelo(id_modelo, nome_modelo)

# Excluindo uma marca
id_marca = 3  # ID da marca a ser excluída
excluir_marca(id_marca)

# Excluindo um modelo
id_modelo = 2  # ID do modelo a ser excluído
excluir_modelo(id_modelo)

# Excluindo um carro
id_carro = 3  # ID do carro a ser excluído
excluir_carro(id_carro)

# Exibindo todas as marcas após as exclusões
print("Todas as marcas após exclusões:")
marcas = obter_marcas()
exibir_tabela(marcas)

# Exibindo todos os carros após as exclusões
print("Todos os carros após exclusões:")
carros = obter_carros()
exibir_tabela(carros)

# Deletando todas as tabelas
deletar_tabelas()



conn.close()
