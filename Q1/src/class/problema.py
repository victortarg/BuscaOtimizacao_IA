import numpy as np

class Problema:
    """Encapsula a função matemática, os limites (caixa) e o objetivo (min/max)."""
    def __init__(self, funcao, limites, tipo="min"):
        self.funcao = funcao
        self.limites = np.array(limites) # Ex: np.array([[-100, 100], [-100, 100]])
        self.tipo = tipo # "min" ou "max"
        
    def avaliar(self, x):
        return self.funcao(*x) # Desempacota o vetor de variáveis para a função
        
    def dentro_dos_limites(self, x):
        """Testa se o candidato gerado está no limite imposto pelas variáveis."""
        return np.all(x >= self.limites[:, 0]) and np.all(x <= self.limites[:, 1])