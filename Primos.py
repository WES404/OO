class Primos:
    def éPrimo(self, k):
        #recebe um numero e diz se é primo ou não
        é_primo = True
        divisor = 2

        while divisor < k and é_primo:
            if k % divisor == 0:
                é_primo = False
            divisor += 1

        if é_primo and k != 1:
            #se for primo o numero será retornado
            return k
        else:
            #senão retorna "False"
            return é_primo

    def cria_lista_primos(self, n):
        #Devolve uma lista com todos os primos no intervalo de 0 a N
        
        lista = []
        x = 2
        
        if n == 2:
            lista.append(n)
        
        while x <= limite:
            while n % fator != 0 and fator <= n/2:
                fator += 1    
            if n % fator != 0:
                lista.append(x)
        return lista
        
        

    def maior_primo(self, n):
        #recebe um numero e diz o maior primo abaixo dele
        if (self.éPrimo(n) == n):
            return n
        else:
            while self.éPrimo(n) == False:
                n -= 1
                self.éPrimo(n)
                if self.éPrimo(n) == n:
                    return n
                    
