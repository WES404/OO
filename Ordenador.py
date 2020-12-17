class Ordenador():

    def ordenada(self, lista):
        #Recebe uma lista co numeros e retorna True se estiver ordenadar
        tamanho = len(lista)
        for i in range(tamanho):
            primeira_posição = i
            for j in range(i+1, tamanho):
                if lista[j] < lista[primeira_posição]:
                    return False
            return True

    def selecao_direta(self, lista):
        #ordena lista trocando os valores maiores por menores
        tamanho = len(lista)
        for i in range(tamanho):
            for j in range(i+1, tamanho):
                #percorre a lista e compara a ultima posição com a atual
                if lista[j] < lista[i]:
                    posicao_menor_item = j
                    #troca as posições dos item em ordem crescente
                    lista[i], lista[posicao_menor_item] = lista[posicao_menor_item], lista[i]
        return lista
            
    def bolha_curta(self, lista):        
        """ ordena lista trocando os valores se estiver ordenada devolve no
        primeiro for """
        
        tamanho = len(lista)
        for i in range(tamanho-1, 0, -1):
            trocou = False
            #percorre a lista do fim e compara a de dois em dois
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    #troca as posições dos item em ordem crescente
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return lista

    def bolha(self, lista):        
        """ ordena lista trocando os valores """
        
        tamanho = len(lista)
        for i in range(tamanho-1, 0, -1):
            
            #percorre a lista do fim e compara a de dois em dois
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    #troca as posições dos item em ordem crescente
                    lista[j], lista[j+1] = lista[j+1], lista[j]    
            return lista
    
