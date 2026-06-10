import matplotlib.pyplot as plt
import numpy as np
from classes.drone_pcv import DronePCV
from algoritmos.ga_permutacao import GAPermutacao
from algoritmos.visualizacao_pcv import plotar_rota_drone_3d

def executar():
    problema = DronePCV(num_pontos_por_regiao=45)
    max_geracoes = 200
    
    ga = GAPermutacao(
        problema, 
        tam_populacao=120, 
        p_crossover=0.85, 
        p_mutacao=0.01, # 1% 
        elitismo_n=0 # operador de Elitismo para análise
    )

    historico_melhor = []
    
    print("\nIniciando Evolução do Algoritmo Genético Combinatório para Drone 3D...")
    for geracao in range(max_geracoes):
        ga.evoluir_geracao()
        melhor_custo = np.min(ga.custos)
        historico_melhor.append(melhor_custo)
        
        if geracao % 20 == 0 or geracao == max_geracoes - 1:
            print(f" Geração {geracao:03d} | Menor Trajetória: {melhor_custo:.2f} unidades de distância.")

    # Plotando o histórico de convergência
    plt.figure(figsize=(10, 5))
    plt.plot(historico_melhor, color="darkgreen", lw=2, label="Melhor Rota da População")
    plt.title("Convergência do Algoritmo Genético - Caixeiro Viajante 3D")
    plt.xlabel("Gerações")
    plt.ylabel("Custo Total de Distância (Aptidão)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()

    # Plotando a trajetória subótima do drone 3D
    plotar_rota_drone_3d(problema, ga.P[np.argmin(ga.custos)], melhor_custo)

if __name__ == "__main__":
    executar()