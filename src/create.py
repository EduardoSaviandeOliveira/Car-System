from conexao import *


def inserir_marca(nome):
    cursor.execute("SELECT COUNT(*) FROM Marca WHERE nome = ?", (nome,))
    marca_existe = cursor.fetchone()[0]

    if marca_existe > 0:
        print(f"A marca '{nome}' já existe. Não é possível inserir novamente.")
    else:
        cursor.execute("INSERT INTO Marca (nome) VALUES (?)", (nome,))
        conn.commit()
        print(f"Marca '{nome}' inserida com sucesso.")


def inserir_modelo(id_marca, nome):
    cursor.execute("SELECT COUNT(*) FROM Modelo WHERE id_marca = ? AND nome = ?", (id_marca, nome))
    modelo_existe = cursor.fetchone()[0]

    if modelo_existe > 0:
        print(f"O modelo '{nome}' já existe. Não é possível criar outro com o mesmo nome e marca.")
    else:
        cursor.execute("SELECT COUNT(*) FROM Marca WHERE id = ?", (id_marca,))
        marca_existe = cursor.fetchone()[0]

        if marca_existe > 0:
            cursor.execute("INSERT INTO Modelo (id_marca, nome) VALUES (?, ?)", (id_marca, nome))
            conn.commit()
            print(f"Modelo '{nome}' inserido com sucesso.")
        else:
            print(f"A marca com id '{id_marca}' especificada não existe. Não é possível criar o modelo.")


def inserir_carro(id_modelo, nome, renavam, placa, valor, ano):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE nome = ?", (nome,))
    carro_existe = cursor.fetchone()[0]

    if carro_existe > 0:
        print(f"O carro '{nome}' já existe. Não é possível inserir novamente.")
    else:
        cursor.execute("INSERT INTO Carro (id_modelo, nome, renavam, placa, valor, ano) VALUES (?, ?, ?, ?, ?, ?)",
                       (id_modelo, nome, renavam, placa, valor, ano))
        conn.commit()
        print(f"Carro '{nome}' inserido com sucesso.")

