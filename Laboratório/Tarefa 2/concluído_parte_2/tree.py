from typing import List
import math as m

class Node:
    def __init__(self, key, left:"Node"=None, right:"Node"=None):
        self.key = key
        self.left = left
        self.right = right

    def print_tree(self):
        """
        Imprime a arvore a partir do nodo atual
        """
        if self.left:
            self.left.print_tree()
        print(self.key, end=" ")
        if self.right:
            self.right.print_tree()


    def insert(self, key) -> bool:
        """
        Insere um nodo na árvore que a chave "key"
        """
        if key < self.key:
            if self.left:
                return self.left.insert(key)
            else:
                self.left = Node(key)
                return True
        elif key > self.key:
            if self.right:
                return self.right.insert(key)
            else:
                self.right = Node(key)
                return True
        else:
            return False


    def search(self, key) -> bool:
        """
        Retorna verdadeiro caso a chave `key` exista na árvore
        """
        if key < self.key:
            if self.left:
                return self.left.search(key)
        elif key > self.key:
            if self.right:
                return self.right.search(key)
        else:
            return True
        return False


    def to_sorted_array(self, arr_result:List =None) -> List:
        """
        Retorna um vetor das chaves ordenadas.
        arr_result: Parametro com os itens já adicionados.
        """
        if(arr_result == None):
            arr_result = []

        if self.left:
            self.left.to_sorted_array(arr_result)

        arr_result.append(self.key)

        if self.right:
            self.right.to_sorted_array(arr_result)
        return arr_result

    def max_depth(self,current_max_depth:int=0) -> int:
        """
        Calcula a maior distancia entre o nodo raiz e a folha
        current_max_depth: Valor representando a maior distancia até então
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        current_max_depth = current_max_depth +1
        val_left,val_right = current_max_depth,current_max_depth

        if self.left:
            val_left = self.left.max_depth(current_max_depth)
        if self.right:
            val_right = self.right.max_depth(current_max_depth)

        if(val_left>val_right):
            return val_left
        else:
            return val_right

    def position_node(self, key, current_position:int=1) -> int:
        """
            Retorna a posição do nodo desejado na árvore
            current_position: representa a posição da árvore naquele momento
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        if key < self.key:
            if self.left:
                current_position = 2*current_position
                return self.left.position_node(key, current_position)
        elif key > self.key:
            if self.right:
                current_position = 2*current_position + 1
                return self.right.position_node(key, current_position)
        else:
            # print(current_position)
            return current_position

        return current_position

    def caminhos(self, i: int = 0, val_left: int = 0, val_right: int = 0):
        """
            Conta quantas vezes novos valores foram colocados à esquerda e à direita na árvore  
        """
        if self.left:
            val_left = val_left + 1
            val_left, val_right = self.left.caminhos(0, val_left, val_right)
        if self.right:
            val_right = val_right + 1
            val_left, val_right = self.right.caminhos(0, val_left, val_right)

        # Sair da func
        # print("Saiu")
        # print("Esq = {}".format(val_left))
        # print("Dir = {}".format(val_right))
        return val_left, val_right
    
    def caminhos3(self, key, val_left: int = 0, val_right: int = 0, opcao: str = "nada"):
        """
            Avalia o balanço de cada nodo
        """
        if self.left and opcao is not "direita":
            val_left = val_left + 1
            val_left, val_right = self.left.caminhos3(key, val_left, val_right, "esquerda")
        if self.right and opcao is not "esquerda":
            val_right = val_right + 1
            val_left, val_right = self.right.caminhos3(key, val_left, val_right, "direita")

        # print("Saiu")
        # print("Esq = {}".format(val_left))
        # print("Dir = {}".format(val_right))
        return val_left, val_right

    def caminhos2(self, key, array: List):
        """
            Percorre a árvore, chamando caminhos3 para avaliar o balanço de cada nodo
        """
        # print(self.key)
        a, b = self.caminhos3(self.key)
        
        if (b-a < -1) or (b-a > 1):
            array.append(False)

        # print("\n\n")
        if self.left:
            self.left.caminhos2(key, array)

        if self.right:
            self.right.caminhos2(key, array)

        # print("Retorna Vdd")
        return array
    
    def is_balanced(self) -> bool:
        """
            Retorna true caso a árvore seja balanceada, false caso não seja
        """
        respostas = []
        respostas = self.caminhos2(self.key, respostas)

        # print(respostas)
        if not respostas:
            return True
        return False

    def sorted_array_to_balanced_tree(self, array:List, start:int, end:int) -> "Node":
        if (start > end):
            return None
        
        pos_raiz_sub_arvore = m.ceil(((start + end)/2))
        raiz_sub_arvore = Node(array[pos_raiz_sub_arvore]) ### NÃO MEXER!

        raiz_sub_arvore.left = self.sorted_array_to_balanced_tree(
            array, start, pos_raiz_sub_arvore-1)

        raiz_sub_arvore.right = self.sorted_array_to_balanced_tree(
            array, pos_raiz_sub_arvore+1, end)

        return raiz_sub_arvore

    def to_balanced_tree(self):

        array = self.to_sorted_array()

        return self.sorted_array_to_balanced_tree(array, 0, len(array)-1)


if __name__ == "__main__":
    arr_tests = []
    # arr_tests.append(Node(3))
    # arr_tests[0].insert(4)
    # arr_tests[0].insert(5)
    # arr_tests[0].insert(10)
    # arr_tests[0].insert(6)
    # arr_tests[0].insert(8)
    # arr_tests[0].insert(9)
    # arr_tests[0].insert(15)

#     # arr_tests.append(Node(5))
#     # arr_tests[0].insert(4)
#     # arr_tests[0].insert(3)
#     # arr_tests[0].insert(2)
#     # arr_tests[0].insert(1)
#     # arr_tests[0].insert(6)
#     # arr_tests[0].insert(7)
#     # arr_tests[0].insert(8)
#     # arr_tests[0].insert(9)

#     arr_tests.append(Node(7))
#     arr_tests[0].insert(6)
#     arr_tests[0].insert(4)
#     arr_tests[0].insert(3)
#     arr_tests[0].insert(5)
#     arr_tests[0].insert(9)
#     arr_tests[0].insert(8)
#     arr_tests[0].insert(10)
#     arr_tests[0].insert(11)


    arr_tests.append(Node(1))
    arr_tests.append(Node(1))
    arr_tests.append(Node(1))

    arr_tests.append(Node(3))
    arr_tests[3].insert(4)
    arr_tests[3].insert(5)
    arr_tests[3].insert(10)
    arr_tests[3].insert(6)
    arr_tests[3].insert(8)
    arr_tests[3].insert(9)
    arr_tests[3].insert(15)

    arr_tests.append(Node(8))

    arr_tests.append(Node(6))
    arr_tests[5].insert(5)
    arr_tests[5].insert(4)
    arr_tests[5].insert(3)
    arr_tests[5].insert(10)
    arr_tests[5].insert(9)
    arr_tests[5].insert(8)
    arr_tests[5].insert(15)

    arr_tests.append(Node(5))
    arr_tests[6].insert(3)
    arr_tests[6].insert(4)
    arr_tests[6].insert(8)
    arr_tests[6].insert(6)
    arr_tests[6].insert(10)
    arr_tests[6].insert(9)


    resp1 = Node.is_balanced(arr_tests[3])
    print("resp1={}".format(resp1))

    resp1 = Node.is_balanced(arr_tests[4])
    print("resp1={}".format(resp1))

    resp1 = Node.is_balanced(arr_tests[5])
    print("resp1={}".format(resp1))

    resp1 = Node.is_balanced(arr_tests[6])
    print("resp1={}".format(resp1))



    # resp2 = Node.to_balanced_tree(arr_tests[0])

