from conexao import *

def criar_tabelas():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Marca (
                        id INTEGER PRIMARY KEY,
                        nome VARCHAR(50)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Modelo (
                        id INTEGER PRIMARY KEY,
                        id_marca INTEGER,
                        nome VARCHAR(50),
                        FOREIGN KEY (id_marca) REFERENCES Marca(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Carro (
                        id INTEGER PRIMARY KEY,
                        id_modelo INTEGER,
                        nome VARCHAR(50),
                        renavam INTEGER,
                        placa INTEGER,
                        valor DECIMAL(10,2),
                        ano YEAR,
                        FOREIGN KEY (id_modelo) REFERENCES Modelo(id)
                    )''')
    print("Tabelas de Carros, Marcas e Modelos criadas")