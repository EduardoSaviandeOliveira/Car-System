from conexao import *


def obter_marcas():
    cursor.execute("SELECT * FROM Marca")
    marcas = cursor.fetchall()

    if not marcas:
        print("Não existem marcas cadastradas.")
    else:
        for marca in marcas:
            print(f"ID: {marca['id']}, Nome: {marca['nome']}")
        print()


def obter_modelos_por_marca(id_marca):
    cursor.execute("SELECT * FROM Modelo WHERE id_marca = ?", (id_marca,))
    modelos = cursor.fetchall()

    if not modelos:
        print(f"Não existem modelos cadastrados para a marca com ID {id_marca}.")
    else:
        for modelo in modelos:
            print(f"ID: {modelo['id']}, Nome: {modelo['nome']}")
        print()


def obter_carros():
    cursor.execute('''SELECT c.id, c.nome, c.renavam, c.placa, c.valor, c.ano, m.nome AS modelo, ma.nome AS marca
                      FROM Carro c
                      JOIN Modelo m ON c.id_modelo = m.id
                      JOIN Marca ma ON m.id_marca = ma.id''')
    carros = cursor.fetchall()

    if not carros:
        print("Não existem carros cadastrados.")
    else:
        for carro in carros:
            print(f"ID: {carro['id']}, Nome: {carro['nome']}, Marca: {carro['marca']}, Modelo: {carro['modelo']}")
        print()


def obter_carro_por_id(id_carro):
    cursor.execute('''SELECT c.id, c.nome, c.renavam, c.placa, c.valor, c.ano, m.nome AS modelo, ma.nome AS marca
                      FROM Carro c
                      JOIN Modelo m ON c.id_modelo = m.id
                      JOIN Marca ma ON m.id_marca = ma.id
                      WHERE c.id = ?''', (id_carro,))
    carro = cursor.fetchone()

    if not carro:
        print(f"Não existe um carro cadastrado com o ID {id_carro}.")
    else:
        print(f"Informações do carro com ID {id_carro}:")
        print(f"Nome: {carro['nome']}")
        print(f"Renavam: {carro['renavam']}")
        print(f"Placa: {carro['placa']}")
        print(f"Valor: {carro['valor']}")
        print(f"Ano: {carro['ano']}")
        print(f"Marca: {carro['marca']}")
        print(f"Modelo: {carro['modelo']}")
        print()


def obter_modelos_e_carros_por_marca(id_marca):
    cursor.execute('''SELECT m.id, m.nome AS modelo, c.id AS id_carro, c.nome AS carro, c.renavam, c.placa, c.valor, c.ano
                      FROM Modelo m
                      LEFT JOIN Carro c ON m.id = c.id_modelo
                      WHERE m.id_marca = ?''', (id_marca,))
    modelos_carros = cursor.fetchall()

    if not modelos_carros:
        print(f"Não existem modelos e carros cadastrados para a marca com ID {id_marca}.")
    else:
        for mc in modelos_carros:
            modelo = mc['modelo']
            carro = mc['carro']
            renavam = mc['renavam']
            placa = mc['placa']
            valor = mc['valor']
            ano = mc['ano']
            id_carro = mc['id_carro']

            print(f"Modelo: {modelo}")
            if carro:
                print(f"ID Carro: {id_carro}, Carro: {carro}, Renavam: {renavam}, Placa: {placa}, Valor: {valor}, Ano: {ano}")
            else:
                print("Nenhum carro cadastrado para este modelo.")
            print()

