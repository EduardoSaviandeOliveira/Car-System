from conexao import *


def excluir_marca(id_marca):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE id_modelo IN (SELECT id FROM Modelo WHERE id_marca = ?)", (id_marca,))
    total_carros = cursor.fetchone()[0]

    if total_carros > 0:
        print("Não é possível excluir a marca. Existem carros associados a ela.")
    else:
        cursor.execute("SELECT COUNT(*) FROM Marca WHERE id = ?", (id_marca,))
        marca_existe = cursor.fetchone()[0]

        if marca_existe > 0:
            cursor.execute("DELETE FROM Marca WHERE id = ?", (id_marca,))
            conn.commit()
            print(f"Marca {id_marca} excluída com sucesso.")
        else:
            print(f"A marca com id {id_marca} não existe.")


def excluir_modelo(id_modelo):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE id_modelo = ?", (id_modelo,))
    total_carros = cursor.fetchone()[0]

    if total_carros > 0:
        print("Não é possível excluir o modelo. Existem carros associados a ele.")
    else:
        cursor.execute("SELECT COUNT(*) FROM Modelo WHERE id = ?", (id_modelo,))
        modelo_existe = cursor.fetchone()[0]

        if modelo_existe > 0:
            cursor.execute("DELETE FROM Modelo WHERE id = ?", (id_modelo,))
            conn.commit()
            print(f"Modelo {id_modelo} excluído com sucesso.")
        else:
            print(f"O modelo com id {id_modelo} não existe.")


def excluir_carro(id_carro):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE id = ?", (id_carro,))
    carro_existe = cursor.fetchone()[0]

    if carro_existe > 0:
        cursor.execute("DELETE FROM Carro WHERE id = ?", (id_carro,))
        conn.commit()
        print(f"Carro {id_carro} excluído com sucesso.")
    else:
        print(f"O carro com id {id_carro} não existe.")


def deletar_tabelas():
    cursor.execute("DROP TABLE IF EXISTS Carro")
    cursor.execute("DROP TABLE IF EXISTS Modelo")
    cursor.execute("DROP TABLE IF EXISTS Marca")

    print("Tabelas excluídas.")

from conexao import *


def excluir_marca(id_marca):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE id_modelo IN (SELECT id FROM Modelo WHERE id_marca = ?)", (id_marca,))
    total_carros = cursor.fetchone()[0]

    if total_carros > 0:
        print("Não é possível excluir a marca. Existem carros associados a ela.")
    else:
        cursor.execute("SELECT COUNT(*) FROM Marca WHERE id = ?", (id_marca,))
        marca_existe = cursor.fetchone()[0]

        if marca_existe > 0:
            cursor.execute("DELETE FROM Marca WHERE id = ?", (id_marca,))
            conn.commit()
            print(f"Marca {id_marca} excluída com sucesso.")
        else:
            print(f"A marca com id {id_marca} não existe.")


def excluir_modelo(id_modelo):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE id_modelo = ?", (id_modelo,))
    total_carros = cursor.fetchone()[0]

    if total_carros > 0:
        print("Não é possível excluir o modelo. Existem carros associados a ele.")
    else:
        cursor.execute("SELECT COUNT(*) FROM Modelo WHERE id = ?", (id_modelo,))
        modelo_existe = cursor.fetchone()[0]

        if modelo_existe > 0:
            cursor.execute("DELETE FROM Modelo WHERE id = ?", (id_modelo,))
            conn.commit()
            print(f"Modelo {id_modelo} excluído com sucesso.")
        else:
            print(f"O modelo com id {id_modelo} não existe.")


def excluir_carro(id_carro):
    cursor.execute("SELECT COUNT(*) FROM Carro WHERE id = ?", (id_carro,))
    carro_existe = cursor.fetchone()[0]

    if carro_existe > 0:
        cursor.execute("DELETE FROM Carro WHERE id = ?", (id_carro,))
        conn.commit()
        print(f"Carro {id_carro} excluído com sucesso.")
    else:
        print(f"O carro com id {id_carro} não existe.")


def deletar_tabelas():
    cursor.execute("DROP TABLE IF EXISTS Carro")
    cursor.execute("DROP TABLE IF EXISTS Modelo")
    cursor.execute("DROP TABLE IF EXISTS Marca")

    print("Tabelas excluídas.")

