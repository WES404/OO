import random
class Lista:
    
    def lista_aleatoria(self, n, LIM1 = 0, LIM2 = 9999):
        #cria uma lista com N valores aleatorios com LIM1 <= x <= LIM2
        lista = [random.randrange(LIM1, LIM2) for x in range(n)]
        return lista

    def remove_repetidos(self, lista):
        #remove itens repetidos dentro de uma lista
        lista_nova = []
        num = 0
        cont = len(lista)
        for i in range(cont):
            num = lista[i]
            if lista.count(num) >= 2:
                if num not in lista_nova:
                    lista_nova.append(num)
            elif lista.count(num) <=2:
                if num not in lista_nova:
                    lista_nova.append(num)
        return lista_nova

