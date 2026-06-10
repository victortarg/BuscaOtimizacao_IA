import numpy as np

class OptimizadorBase:
    def __init__(self, problema, max_iter=1000, max_sem_melhora=50):
        self.problema = problema
        self.max_iter = max_iter
        self.max_sem_melhora = max_sem_melhora # Critério de parada antecipada (t)

    def _gerar_ponto_inicial(self):
        return np.random.uniform(self.problema.limites[:, 0], self.problema.limites[:, 1])

    def gerar_candidato(self, x_best):
        raise NotImplementedError

    def e_melhor(self, f_cand, f_best):
        if self.problema.tipo == "min":
            return f_cand < f_best
        return f_cand > f_best

    def otimizar(self):
        # Ponto inicial aleatório dentro dos limites
        dimensoes = len(self.problema.limites)
        x_best = self._gerar_ponto_inicial()
        f_best = self.problema.avaliar(x_best)
        
        iteracoes_sem_melhora = 0
        
        for _ in range(self.max_iter):
            x_cand = self.gerar_candidato(x_best)
            
            if self.problema.dentro_dos_limites(x_cand):
                f_cand = self.problema.avaliar(x_cand)
                
                if self.e_melhor(f_cand, f_best):
                    x_best = x_cand
                    f_best = f_cand
                    iteracoes_sem_melhora = 0
                else:
                    iteracoes_sem_melhora += 1
            
            # Parada antecipada
            if iteracoes_sem_melhora >= self.max_sem_melhora:
                break
                
        return x_best, f_best

    def executar_experimento(self, num_rodadas=100):
        """Executa R rodadas e coleta os resultados."""
        solucoes = []
        for _ in range(num_rodadas):
            x_best, _ = self.otimizar()
            solucoes.append(np.round(x_best, 4)) 
            
        solucoes_array = np.array(solucoes)
        
        # Encontrando a moda
        valores_unicos, contagens = np.unique(solucoes_array, axis=0, return_counts=True)
        indice_moda = np.argmax(contagens)
        moda_solucao = valores_unicos[indice_moda]
        
        return moda_solucao