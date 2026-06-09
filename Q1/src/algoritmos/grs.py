from classes.optimizador_base import OptimizadorBase
import numpy as np

class GlobalRandomSearch(OptimizadorBase):
    def gerar_candidato(self, x_best):
        """GRS ignora o x_best e gera um ponto totalmente aleatório."""
        return np.random.uniform(self.problema.limites[:, 0], self.problema.limites[:, 1])