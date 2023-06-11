from conexao import *


def obter_marcas():
    cursor.execute("SELECT * FROM Marca")
    marcas = cursor.fetchall()

    if not marcas:
        print("Não existem marcas cadastradas.")
    else:
        for marca in marcas:
            id_marca = marca[0]
            nome = marca[1]
            print(f"ID: {id_marca}, Nome: {nome}")
        print()


def obter_modelos_por_marca(id_marca):
    cursor.execute("SELECT * FROM Modelo WHERE id_marca = ?", (id_marca,))
    modelos = cursor.fetchall()

    if not modelos:
        print(f"Não existem modelos cadastrados para a marca com ID {id_marca}.")
    else:
        for modelo in modelos:
            id_modelo = modelo[0]
            nome_modelo = modelo[1]
            print(f"ID: {id_modelo}, Nome: {nome_modelo}")
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
            id_carro = carro[0]
            nome_carro = carro[1]
            marca = carro[7]
            modelo = carro[6]
            print(f"ID: {id_carro}, Nome: {nome_carro}, Marca: {marca}, Modelo: {modelo}")
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
        id_carro = carro[0]
        nome_carro = carro[1]
        renavam = carro[2]
        placa = carro[3]
        valor = carro[4]
        ano = carro[5]
        marca = carro[7]
        modelo = carro[6]
        print(f"Informações do carro com ID {id_carro}:")
        print(f"Nome: {nome_carro}")
        print(f"Renavam: {renavam}")
        print(f"Placa: {placa}")
        print(f"Valor: {valor}")
        print(f"Ano: {ano}")
        print(f"Marca: {marca}")
        print(f"Modelo: {modelo}")
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
            id_modelo = mc[0]
            modelo = mc[1]
            id_carro = mc[2]
            carro = mc[3]
            renavam = mc[4]
            placa = mc[5]
            valor = mc[6]
            ano = mc[7]

            print(f"Modelo: {modelo}")
            if carro:
                print(f"ID Carro: {id_carro}, Carro: {carro}, Renavam: {renavam}, Placa: {placa}, Valor: {valor}, Ano: {ano}")
            else:
                print("Nenhum carro cadastrado para este modelo.")
            print()
