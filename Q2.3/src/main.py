import time
import numpy as np
import matplotlib.pyplot as plt
from algoritmos.ga_continuo import GAContinuo

class ProblemaRastrigin50D:
    def __init__(self):
        self.n = 50
        self.limites = np.array([[-5.12, 5.12] for _ in range(self.n)])
        self.tipo = "min"

    def avaliar(self, x):
        return 10 * self.n + np.sum(x**2 - 10 * np.cos(np.pi * x))

    def gerar_ponto_inicial(self):
        return np.random.uniform(self.limites[:, 0], self.limites[:, 1])

def executar_lrs(problema, max_avaliacoes, sigma=0.5):
    """LRS adaptado para parar por limite exato de avaliações, igualando o GA."""
    x_best = problema.gerar_ponto_inicial()
    f_best = problema.avaliar(x_best)
    
    historico = [f_best]
    
    for _ in range(max_avaliacoes - 1):
        perturbacao = np.random.normal(loc=0.0, scale=sigma, size=problema.n)
        x_cand = x_best + perturbacao
        
        x_cand = np.clip(x_cand, problema.limites[:, 0], problema.limites[:, 1])
        f_cand = problema.avaliar(x_cand)
        
        if f_cand < f_best:
            x_best = x_cand
            f_best = f_cand
            
        historico.append(f_best)
        
    return historico, f_best

def executar_comparacao():
    problema = ProblemaRastrigin50D()
    orcamento = 10000 
    
    cenarios_ga = [
        {"populacao": 20, "geracoes": orcamento // 20},
        {"populacao": 50, "geracoes": orcamento // 50},
        {"populacao": 100, "geracoes": orcamento // 100}
    ]
    
    resultados_grafico = {}
    
    print("-" * 60)
    print(f"{'Método/População':<20} | {'Tempo (s)':<10} | {'Melhor Custo Encontrado'}")
    print("-" * 60)
    
    # Testando o Algoritmo Genético Não Canônico
    for config in cenarios_ga:
        pop = config["populacao"]
        ger = config["geracoes"]
        
        inicio = time.time()
        ga = GAContinuo(problema, tam_populacao=pop)
        
        historico_ga = [np.min(ga.custos)]
        for _ in range(ger - 1):
            ga.evoluir_geracao()
            historico_ga.append(np.min(ga.custos))
            
        tempo_exec = time.time() - inicio
        melhor_custo = np.min(ga.custos)
        
        # Esticando o histórico para bater com o eixo X de avaliações
        eixo_x_avaliacoes = np.linspace(0, orcamento, len(historico_ga))
        resultados_grafico[f"GA (Pop={pop})"] = (eixo_x_avaliacoes, historico_ga)
        
        print(f"GA Pop={pop:<13} | {tempo_exec:<10.3f} | {melhor_custo:.4f}")
        
    # Testando o LRS (Busca Local Aleatória)
    inicio = time.time()
    historico_lrs, custo_lrs = executar_lrs(problema, max_avaliacoes=orcamento)
    tempo_exec = time.time() - inicio
    
    resultados_grafico["LRS (Local Random)"] = (np.arange(orcamento), historico_lrs)
    print(f"{'LRS':<20} | {tempo_exec:<10.3f} | {custo_lrs:.4f}")
    print("-" * 60)

    plt.figure(figsize=(12, 6))
    cores = ['blue', 'orange', 'green', 'red']
    
    for (nome, (eixo_x, hist)), cor in zip(resultados_grafico.items(), cores):
        plt.plot(eixo_x, hist, label=nome, color=cor, lw=2 if "GA" in nome else 1.5)
        
    plt.title("Comparação: GA Não Canônico vs LRS (Função Rastrigin 50D)")
    plt.xlabel("Avaliações da Função Objetivo (Custo Computacional Equilibrado)")
    plt.ylabel("Melhor Custo (Minimização)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    
    plt.savefig("graficos/comparacao_metodos_parte3.png", dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    executar_comparacao()