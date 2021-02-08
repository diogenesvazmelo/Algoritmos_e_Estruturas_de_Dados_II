from functools import total_ordering
import math
class MaxHeap:

    def __init__(self):
        #inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
    
    #Os metodos esquerda, direita e pai serão usados nos demais metodos do heap
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
        """
        return 2*i

    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
        """
        return (2*i)+1

    def pai(self, i:int) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        if (i % 2) == 0:
            return i/2
        else:
            return math.floor(i/2)



    @property
    def pos_ultimo_item(self) -> int:
        return len(self.arr_heap)-1

    def refaz(self, pos_raiz_sub_arvore:int):

        #maior_filho é inicializado com o da esqueda de pos raiz subarvore
        pos_pai = pos_raiz_sub_arvore
        pos_maior_filho = self.esquerda(pos_pai)


        #obtem o item raiz da subarvore do heap
        val_raiz_sub_arvore = self.arr_heap[pos_pai]

        val_maior_filho = -10000
        while self.esquerda(pos_pai) <= self.pos_ultimo_item:
            #se a posição do filho a esquerda não for a ultima do vetor,
            #atualize, se necessario, o pos_maior_filho considerando o filho a direita
            
            if pos_maior_filho < self.pos_ultimo_item:
                val_filho_esquerda = self.arr_heap[self.esquerda(pos_pai)]
                val_filho_direita = self.arr_heap[self.direita(pos_pai)]
                if val_filho_esquerda < val_filho_direita:
                    pos_maior_filho = self.direita(pos_pai)
                    val_maior_filho = val_filho_direita
                else:
                    val_maior_filho = val_filho_esquerda


            #caso o valor da  raiz desta subarvore (val_raiz_sub_arvore)
            #possua um valor maior que o de seus filhos, 
            # finaliza o while 

            if val_raiz_sub_arvore > val_maior_filho:
                break


            #realize a troca conforme especificação
            self.arr_heap[pos_pai] = val_maior_filho


            #prepare as variáveis pos_pai e pos_maior_filho para a proxima iteração
            #substitua os "None" das duas linhas abaixo apropriadamente
            pos_pai = pos_maior_filho
            pos_maior_filho = self.esquerda(pos_pai)

        #atualize a posição pos_pai apropriadamente
        self.arr_heap[pos_pai] = val_raiz_sub_arvore

    def retira_max(self):
        if len(self.arr_heap)<=1:
            # raise IndexError("Heap Vazio")
            return None
        ## Faça a retirada do máximo conforme especificação/slides da aula teórica
        
        maximo = self.arr_heap[1]
        self.arr_heap[1] = self.arr_heap[-1]
        self.arr_heap.pop()

        i = 1

        while(i*2 < len(self.arr_heap)):
            if (i*2)+1 < len(self.arr_heap):
                if self.arr_heap[i*2] > self.arr_heap[(i*2)+1]:
                    if self.arr_heap[i*2] > self.arr_heap[i]:
                        temp = self.arr_heap[i]
                        self.arr_heap[i] = self.arr_heap[i*2]
                        self.arr_heap[i*2] = temp
                        i = i*2
                    else:
                        break
                else:
                    if self.arr_heap[(i*2)+1] > self.arr_heap[i]:
                        temp = self.arr_heap[i]
                        self.arr_heap[i] = self.arr_heap[(i*2)+1]
                        self.arr_heap[(i*2)+1] = temp
                        i = (i*2)+1
                    else:
                        break
            elif self.arr_heap[i*2] > self.arr_heap[i]:
                temp = self.arr_heap[i]
                self.arr_heap[i] = self.arr_heap[i*2]
                self.arr_heap[i*2] = temp
                i = i*2
            else:
                break

        return maximo

    def insere(self, item):
        self.arr_heap.append(self.arr_heap[-1])
        pos_inserir = self.pos_ultimo_item
        pai_pos_inserir = self.pai(pos_inserir)

        #substitua o "None" apropriadamente
        while pos_inserir > 1 and item > self.arr_heap[int(pai_pos_inserir)]:
            #realiza a atualização (substitua os "None")
            self.arr_heap[int(pos_inserir)] = self.arr_heap[int(pai_pos_inserir)]

            #ajusta para a proxima iteração (substitua os None apropriadamente)
            pos_inserir = pai_pos_inserir
            pai_pos_inserir = self.pai(pos_inserir)

        #finalize o insere apropriadamente
        self.arr_heap[int(pos_inserir)] = item
