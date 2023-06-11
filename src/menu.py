from conexao import *

from startup import *

from create import *
from read import *
from update import *
from delete import *


def exibir_menu():
    print("Menu:")
    print("1. Inserir marca")
    print("2. Inserir modelo")
    print("3. Inserir carro")
    print("4. Obter marcas")
    print("5. Obter modelos por marca")
    print("6. Obter carros")
    print("7. Obter carro por ID")
    print("8. Obter modelos e carros por marca")
    print("9. Atualizar marca")
    print("10. Atualizar modelo")
    print("11. Atualizar carro")
    print("12. Deletar marca")
    print("13. Deletar modelo")
    print("14. Deletar carro")
    print("15. Criar tabelas")
    print("16. Deletar tabelas")
    print("0. Sair")
    print()


def menu():
    while True:
        exibir_menu()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da marca: ")
            inserir_marca(nome)
        elif opcao == "2":
            id_marca = input("Digite o ID da marca: ")
            nome = input("Digite o nome do modelo: ")
            inserir_modelo(id_marca, nome)
        elif opcao == "3":
            id_modelo = input("Digite o ID do modelo: ")
            nome = input("Digite o nome do carro: ")
            renavam = input("Digite o renavam do carro: ")
            placa = input("Digite a placa do carro: ")
            valor = input("Digite o valor do carro: ")
            ano = input("Digite o ano do carro: ")
            inserir_carro(id_modelo, nome, renavam, placa, valor, ano)
        elif opcao == "4":
            obter_marcas()
        elif opcao == "5":
            id_marca = input("Digite o ID da marca: ")
            obter_modelos_por_marca(id_marca)
        elif opcao == "6":
            obter_carros()
        elif opcao == "7":
            id_carro = input("Digite o ID do carro: ")
            obter_carro_por_id(id_carro)
        elif opcao == "8":
            id_marca = input("Digite o ID da marca: ")
            obter_modelos_e_carros_por_marca(id_marca)
        elif opcao == "9":
            id_marca = input("Digite o ID da marca: ")
            nome = input("Digite o novo nome da marca: ")
            atualizar_marca(id_marca, nome)
        elif opcao == "10":
            id_modelo = input("Digite o ID do modelo: ")
            nome = input("Digite o novo nome do modelo: ")
            atualizar_modelo(id_modelo, nome)
        elif opcao == "11":
            id_carro = input("Digite o ID do carro: ")
            nome = input("Digite o novo nome do carro: ")
            renavam = input("Digite o novo renavam do carro: ")
            placa = input("Digite a nova placa do carro: ")
            valor = input("Digite o novo valor do carro: ")
            ano = input("Digite o novo ano do carro: ")
            atualizar_carro(id_carro, nome, renavam, placa, valor, ano)
        elif opcao == "12":
            id_marca = input("Digite o ID da marca a ser deletada: ")
            excluir_marca(id_marca)
        elif opcao == "13":
            id_modelo = input("Digite o ID do modelo a ser deletado: ")
            excluir_modelo(id_modelo)
        elif opcao == "14":
            id_carro = input("Digite o ID do carro a ser deletado: ")
            excluir_carro(id_carro)
        elif opcao == "15":
            criar_tabelas()
        elif opcao == "16":
            deletar_tabelas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
        print()

    conn.close()
