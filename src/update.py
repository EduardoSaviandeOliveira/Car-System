from conexao import *

def atualizar_marca(id_marca, nome):
    cursor.execute("SELECT COUNT(*) FROM Marca WHERE id = ?", (id_marca,))
    marca_existe = cursor.fetchone()[0]

    if marca_existe > 0:
        cursor.execute("UPDATE Marca SET nome = ? WHERE id = ?", (nome, id_marca))
        conn.commit()
        print(f"Marca com ID {id_marca} atualizada com sucesso.")
    else:
        print(f"Não existe uma marca cadastrada com o ID {id_marca}. Não é possível atualizá-la.")


def atualizar_modelo(id_modelo, nome):
    cursor.execute("SELECT COUNT(*) FROM Modelo WHERE id = ?", (id_modelo,))
    modelo_existe = cursor.fetchone()[0]

    if modelo_existe > 0:
        cursor.execute("UPDATE Modelo SET nome = ? WHERE id = ?", (nome, id_modelo))
        conn.commit()
        print(f"Modelo com ID {id_modelo} atualizado com sucesso.")
    else:
        print(f"Não existe um modelo cadastrado com o ID {id_modelo}. Não é possível atualizá-lo.")


def atualizar_carro(id_carro, nome, renavam, placa, valor, ano):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE id = ?", (id_carro,))
    carro_existe = cursor.fetchone()[0]

    if carro_existe > 0:
        cursor.execute("UPDATE Carro SET nome = ?, renavam = ?, placa = ?, valor = ?, ano = ? WHERE id = ?",
                       (nome, renavam, placa, valor, ano, id_carro))
        conn.commit()
        print(f"Carro com ID {id_carro} atualizado com sucesso.")
    else:
        print(f"Não existe um carro cadastrado com o ID {id_carro}. Não é possível atualizá-lo.")
