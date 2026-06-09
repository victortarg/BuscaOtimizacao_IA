import numpy as np
from optimizador_base import OptimizadorBase 

class HillClimbing(OptimizadorBase):
    def __init__(self, problema, epsilon=0.1, max_iter=1000, max_sem_melhora=50):
        super().__init__(problema, max_iter, max_sem_melhora)
        self.epsilon = epsilon
        
    def _gerar_ponto_inicial(self):
        """Obrigatório: inicia no limite inferior do domínio de x."""
        return np.copy(self.problema.limites[:, 0])

    def gerar_candidato(self, x_best):
        """Vizinhança baseada em |x_best - y| <= epsilon."""
        # Gera uma perturbação com distribuição uniforme entre -epsilon e +epsilon
        perturbacao = np.random.uniform(-self.epsilon, self.epsilon, size=len(x_best))
        return x_best + perturbacao