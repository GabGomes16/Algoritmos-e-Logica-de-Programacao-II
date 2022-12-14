import sqlite3
class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                    idusuario integer primary key autoincrement ,
                    nome text,
                    telefone text,
                    email text,
                    usuario text,
                    senha text)""")
        c.execute("""create table if not exists numeros (
                    numbers integer)""")
        self.conexao.commit()
        c.close()