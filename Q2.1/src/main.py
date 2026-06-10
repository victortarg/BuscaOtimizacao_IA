import numpy as np
from tempera_simulada import TemperaSimulada
from visualizacao_rainhas import plotar_tabuleiro_rainhas

class OitoRainhas:
    def __init__(self):
        self.n = 8
        self.max_ataques = 28 

    def gerar_candidato_inicial(self):
        """Gera um vetor inicial com as rainhas em linhas aleatórias."""
        return np.random.randint(0, self.n, size=self.n)

    def calcular_fitness(self, x):
        """
        f(x) = 28 - h(x)
        Verifica os pares que estão na mesma linha ou na mesma diagonal.
        """
        h = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # verifia se estão na mesma linha ou na mesma diagonal
                if x[i] == x[j] or abs(x[i] - x[j]) == abs(i - j):
                    h += 1
        return self.max_ataques - h

    def perturbar(self, x):
        """
        Perturbação controlada: escolhe 1 coluna aleatória e move a rainha para outra linha.
        """
        novo_x = np.copy(x)
        coluna_sorteada = np.random.randint(self.n)
        nova_linha = np.random.randint(self.n)
        
        # Garante que a rainha realmente vai mudar de linha
        while nova_linha == x[coluna_sorteada]:
            nova_linha = np.random.randint(self.n)
            
        novo_x[coluna_sorteada] = nova_linha
        return novo_x


def buscar_92_solucoes():
    problema = OitoRainhas()
    # Melhor resultado foram para os parametro T_inicial=70.0, alpha=0.95, max_iter=5000
    # 92 soluções distintas encontradas
    # Custo computacional total: 333 execuções completas da Têmpera Simulada.
    ts = TemperaSimulada(problema, T_inicial=70.0, alpha=0.95, max_iter=5000)
    
    solucoes_unicas = set()
    tentativas = 0
    
    print("Iniciando...")
    while len(solucoes_unicas) < 92: # 92 é o numero de soluções distintas para o problema das 8 rainhas
        tentativas += 1
        x_otimo, f_otimo = ts.otimizar()
        
        # Se encontrou um tabuleiro sem nenhum ataque
        if f_otimo == 28:
            solucao = tuple(x_otimo)
            if solucao not in solucoes_unicas:
                solucoes_unicas.add(solucao)
                print(f"Solução {len(solucoes_unicas)}/92 encontrada! Vetor: {solucao} | Tentativas totais: {tentativas}")

    print("\n92 soluções distintas encontradas")
    print(f"Custo computacional total: {tentativas} execuções completas da Têmpera Simulada.")
    
    numero_solucao=30
    primeira_solucao = list(solucoes_unicas)[numero_solucao-1]
    
    plotar_tabuleiro_rainhas(primeira_solucao, numero_solucao)

if __name__ == "__main__":
    buscar_92_solucoes()