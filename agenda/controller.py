from dao import ItemDAO
from model import Item

class ItemController:
    def __init__(self):
        self.dao = ItemDAO()

    def criarItem(self, descricao: str, quantidade: int):
        if descricao.strip() == "":
            raise ValueError("A descrição não pode ser vazia.")
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        
        item = Item(descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(item)

    def obterTodosOsItens(self) -> list:
        return self.dao.listarTodos()
