from lista_ligada import LinkedList

class pilha:
    def __init__(self):
        self.lista = LinkedList()

    def vazia(self) -> bool:
        return self.lista.esta_vazio()

    def empilhar(self, item):
        self.lista.inserir_inicio(item)

    def desempilhar(self):
        if self.lista():
            return None
        item = self.lista.inicio.valor
        self.lista.remove(item)
        return item

    def procura(self, item):
        self.lista.procura(item)

class FilaPrioritaria:
    def __init__(self):
        self.fila_normal = LinkedList()
        self.fila_prioritaria = LinkedList()

    def vazia(self) -> bool:
        return self.fila_normal.esta_vazio() and self.fila_prioritaria.esta_vazio()

    def enfileirar_normal(self, item):
        self.fila_normal.inserir_fim(item)

    def enfileirar_prioritario(self, item):
        self.fila_prioritaria.inserir_fim(item)

    def desenfileirar(self):
        if not self.fila_prioritaria.esta_vazio():
            return self.fila_prioritaria.remove_primeiro()
        elif not self.fila_normal.esta_vazio():
            return self.fila_normal.remove_primeiro()
        else:
            return None
    def procura(self, item):
        return self.fila_normal.procura(item) or self.fila_prioritaria.procura(item)

