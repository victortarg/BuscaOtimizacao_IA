import numpy as np

class TemperaSimulada:
    def __init__(self, problema, T_inicial=100.0, alpha=0.99, max_iter=10000):
        self.problema = problema
        self.T_inicial = T_inicial
        self.alpha = alpha # Fator de decaimento da temperatura
        self.max_iter = max_iter

    def otimizar(self):
        x_atual = self.problema.gerar_candidato_inicial()
        f_atual = self.problema.calcular_fitness(x_atual)
        T = self.T_inicial
        
        for i in range(self.max_iter):
            # Critério de parada atingiu o ótimo absoluto (28)
            if f_atual == self.problema.max_ataques:
                break

            x_cand = self.problema.perturbar(x_atual)
            f_cand = self.problema.calcular_fitness(x_cand)

            # Para MAXIMIZAÇÃO: aceita se f_cand for MAIOR que f_atual
            delta = f_cand - f_atual
            
            if delta > 0:
                x_atual = x_cand
                f_atual = f_cand
            else:
                # Se for pior, aceita com uma probabilidade que diminui com o tempo
                # P = e^(delta / T). Como delta é negativo, a potência será negativa
                probabilidade = np.exp(delta / T)
                if np.random.uniform() < probabilidade:
                    x_atual = x_cand
                    f_atual = f_cand
            
            # Decaimento da temperatura
            T = T * self.alpha

        return x_atual, f_atual