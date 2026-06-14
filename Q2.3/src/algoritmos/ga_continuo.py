import numpy as np

class GAContinuo:
    def __init__(self, problema, tam_populacao=100, p_crossover=0.9, p_mutacao=0.1, eta=1.0, sigma=0.5):
        self.prob = problema
        self.N = tam_populacao
        self.pc = p_crossover
        self.pm = p_mutacao
        self.eta = eta       # Parâmetro do SBX
        self.sigma = sigma   # Desvio padrão da mutação Gaussiana
        self.dimensoes = len(self.prob.limites)
        
        lim_inf = self.prob.limites[:, 0]
        lim_sup = self.prob.limites[:, 1]
        self.P = np.random.uniform(lim_inf, lim_sup, size=(self.N, self.dimensoes))
        self.custos = np.zeros(self.N)
        self.avaliar_populacao()

    def avaliar_populacao(self):
        for i in range(self.N):
            self.custos[i] = self.prob.avaliar(self.P[i])

    def selecao_torneio(self, k=3):
        indices = np.random.choice(self.N, size=k, replace=False)
        melhor_indice = indices[np.argmin(self.custos[indices])]
        return np.copy(self.P[melhor_indice])

    def crossover_sbx(self, p1, p2):
        """Implementação do Simulated Binary Crossover (SBX)"""
        if np.random.uniform() > self.pc:
            return np.copy(p1), np.copy(p2)
            
        c1, c2 = np.empty_like(p1), np.empty_like(p2)
        
        for i in range(self.dimensoes):
            u = np.random.uniform()
            if u <= 0.5:
                beta = (2.0 * u) ** (1.0 / (self.eta + 1.0))
            else:
                beta = (1.0 / (2.0 * (1.0 - u))) ** (1.0 / (self.eta + 1.0))
                
            c1[i] = 0.5 * ((1 + beta) * p1[i] + (1 - beta) * p2[i])
            c2[i] = 0.5 * ((1 - beta) * p1[i] + (1 + beta) * p2[i])
            
        return c1, c2

    def mutacao_gaussiana(self, cromossomo):
        """Mutação contínua que adiciona um ruído Gaussiano aos genes."""
        for i in range(self.dimensoes):
            if np.random.uniform() <= self.pm:
                cromossomo[i] += np.random.normal(0, self.sigma)
                
        # Garante que a mutação não jogue o gene para fora do domínio [-5.12, 5.12]
        lim_inf = self.prob.limites[:, 0]
        lim_sup = self.prob.limites[:, 1]
        cromossomo = np.clip(cromossomo, lim_inf, lim_sup)
        return cromossomo

    def evoluir_geracao(self):
        nova_pop = []
        
        # Elitismo
        melhor_idx = np.argmin(self.custos)
        nova_pop.append(np.copy(self.P[melhor_idx]))
        
        while len(nova_pop) < self.N:
            pai1 = self.selecao_torneio()
            pai2 = self.selecao_torneio()
            
            f1, f2 = self.crossover_sbx(pai1, pai2)
            f1 = self.mutacao_gaussiana(f1)
            f2 = self.mutacao_gaussiana(f2)
            
            nova_pop.append(f1)
            if len(nova_pop) < self.N:
                nova_pop.append(f2)
                
        self.P = np.array(nova_pop)
        self.avaliar_populacao()