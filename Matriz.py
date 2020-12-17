class Matriz:

    def cria_matriz(self, num_linhas,num_colunas):
        """monta a matriz a cada elemento de acordo com numero de linhas e colunas"""
        matriz = []
        for i in range(num_linhas):
            linha = []
            for j in range(num_colunas):
                valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) +"]: "))
                linha.append(valor)

            matriz.append(linha)

        return matriz

    def le_matriz(self):
        """recebe o numero de linhas e colunas"""
        lin = int(input("Digite o numero de linhas da matriz: "))
        col = int(input("Digite o numero de colunas da matriz: "))
        return cria_matriz(lin,col)


    def soma_matrizes(self, m1, m2):
        #soma 2 matrizes com linhas e colunas iguais umas as outras
        if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
            matriz_soma = [] #matriz nova
            for i in range(len(m1)):
                linha = []
                linha1 = m1[i]
                linha2 = m2[i]
                k = 0
                while k < len(linha2):
                    linha_soma = linha1[k] + linha2[k]
                    linha.append(linha_soma)
                    k += 1
                matriz_soma.append(linha)
            return matriz_soma

        else:
            return False

    def multiplica_matriz(self, m1, m2):
        pass
