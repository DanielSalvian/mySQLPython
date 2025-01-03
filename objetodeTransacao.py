import sqlite3 as sql

class objetodeTransacao():

    database = "sql.db"

    conn = None
    cur = None
    connected = False

    def connect(self):
        self.conn = sql.connect(self.database)
        self.cur = self.conn.cursor()
        self.connected = True

    def disconnect(self):
        if self.connected:
            self.conn.close()
            self.connected = False

    def execute(self, sql, parms=None):
        if self.connected:
            if parms is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return self.cur.fetchall()

    def persist(self):
        if self.connected:
            self.conn.commit()
            return True
        else:
            return False

    def initDB(self):
        self.connect()
        try:
            self.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
            self.persist()
        except Exception as e:
            print("Erro ao criar tabela:", e)
        finally:
            self.disconnect()

    def insert(self, nome, sobrenome, email, cpf):
        self.connect()
        self.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        self.persist()
        self.disconnect()

    def view(self):
        self.connect()
        self.execute("SELECT * FROM clientes")
        rows = self.fetchall()
        self.disconnect()
        return rows

    def search(self, nome="", sobrenome="", email="", cpf=""):
        self.connect()
        self.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
        rows = self.fetchall()
        self.disconnect()
        return rows

    def delete(self, id):
        self.connect()
        self.execute("DELETE FROM clientes WHERE id = ?", (id,))
        self.persist()
        self.disconnect()

    def update(self, id, nome, sobrenome, email, cpf):
        self.connect()
        self.execute("UPDATE clientes SET nome =?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
        self.persist()
        self.disconnect()


trans = objetodeTransacao()
trans.initDB()

