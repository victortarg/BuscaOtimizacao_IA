import numpy as np
from optimizador_base import OptimizadorBase

class LocalRandomSearch(OptimizadorBase):
    def __init__(self, problema, sigma=0.5, max_iter=1000, max_sem_melhora=50):
        super().__init__(problema, max_iter, max_sem_melhora)
        self.sigma = sigma # desvio-padrão da perturbação
        
    def _gerar_ponto_inicial(self):
        """LRS começa com x_best aleatório dentro da caixa."""
        return np.random.uniform(self.problema.limites[:, 0], self.problema.limites[:, 1])

    def gerar_candidato(self, x_best):
        """Gera candidato com distribuição normal usando o desvio-padrão sigma."""
        perturbacao = np.random.normal(loc=0.0, scale=self.sigma, size=len(x_best))
        return x_best + perturbacao