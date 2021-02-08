from functools import total_ordering
from datetime import datetime
from heap import MaxHeap

class Cliente:
    def __init__(self,nome:str, idade:int, necessidades_especiais:bool):
        self.nome = nome
        self.idade = idade
        self.necessidades_especiais = necessidades_especiais

    def __str__(self):
        return self.nome
    def __repr__(self):
        return str(self)


class PrioridadeCliente:
    ultima_ordem_chegada = 0
    def __init__(self, cliente:Cliente, prioridade:int):
        self.cliente = cliente
        self.prioridade = prioridade
        PrioridadeCliente.ultima_ordem_chegada += 1
        self.ordem_chegada = PrioridadeCliente.ultima_ordem_chegada

    def __eq__(self, outro:"PrioridadeCliente") ->bool:
        return True

    def __lt__(self,  outro:"PrioridadeCliente") -> bool:


        return True

    def __str__(self):
        return f"Cliente: {self.cliente} Prioridade: {self.prioridade}"

    def __repr__(self):
        return str(self)

class CaixaBanco:
    def __init__(self,nome_banco:str):
        self.fila_prioridade = MaxHeap()

        self.nome_banco = nome_banco


    def adiciona_cliente(self,cliente:Cliente):
        pass

    def proximo_cliente(self) -> Cliente:

        return None

    def __str__(self):
        return f"Banco: {self.nome_banco} Fila: {self.fila_prioridade}"

    def __repr__(self):
        return str(self)
