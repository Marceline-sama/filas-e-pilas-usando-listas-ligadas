from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        return self.inicio is None

    def remove(self, item):
        if self.inicio is None:
            return
        if self.inicio.valor == item:
            self.inicio = self.inicio.proximo
            return
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.valor == item:
                anterior.set_proximo(atual.get_proximo())
                return
            anterior = atual
            atual = atual.get_proximo()

    def tamanho(self) -> int:
        contador = 0
        atual = self.inicio
        while atual is not None:
            contador += 1
            atual = atual.get_proximo()
        return contador

    def limpa(self):
        self.inicio = None

    def procura(self, item) -> bool:
        atual = self.inicio
        while atual is not None:
            if atual.valor == item:
                return True
            atual = atual.proximo
        return False

    def indice_de(self, item):
        indice = 0
        atual = self.inicio
        while atual is not None:
            if atual.valor == item:
                return indice
            indice += 1
            atual = atual.get_proximo()
        return -1

    def recupera_indice(self, index):
        atual = self.inicio
        contador = 0
        while atual is not None:
            if contador == index:
                return atual.valor
            contador += 1
            atual = atual.get_proximo()
        return None
