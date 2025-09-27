import sqlite3
from model import Item

class ItemDAO:
    _NOME_ARQUIVO_DB = 'inventario.db'

    def __init__(self):
        self._criar_tabela()

    def _conectar(self):
        return sqlite3.connect(self._NOME_ARQUIVO_DB)

    def _criar_tabela(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS itens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL,
                    quantidade INTEGER NOT NULL
                );
            """)
            conn.commit()

    def adicionar(self, item: Item):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
                (item.get_descricao(), item.get_quantidade())
            )
            conn.commit()

    def listarTodos(self) -> list[Item]:
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, descricao, quantidade FROM itens")
            resultados = cursor.fetchall()
            
            itens = []
            for row in resultados:
                novo_item = Item(id=row[0], descricao=row[1], quantidade=row[2])
                itens.append(novo_item)
            return itens