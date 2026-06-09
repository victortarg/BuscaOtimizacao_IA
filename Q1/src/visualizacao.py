import numpy as np
import matplotlib.pyplot as plt
from classes.problemas import lista_problemas
from algoritmos.grs import GlobalRandomSearch
from algoritmos.lrs import LocalRandomSearch
from algoritmos.hill_climbing import HillClimbing

def plot_superficie_e_pontos(problema, num_prob, resultados):
    """
    Plota a superfície 3D da função e os pontos encontrados pelos algoritmos.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Gerando a malha (grid) baseada nos limites do problema
    # Usamos 100 pontos para criar uma superfície suave
    x1 = np.linspace(problema.limites[0, 0], problema.limites[0, 1], 100)
    x2 = np.linspace(problema.limites[1, 0], problema.limites[1, 1], 100)
    X1, X2 = np.meshgrid(x1, x2)
    
    # Calculando o Z para toda a malha de uma vez só (mágica do numpy!)
    Z = problema.funcao(X1, X2)
    
    # Plotando a superfície (cmap 'jet' é similar ao que o professor usou no PDF)
    superficie = ax.plot_surface(X1, X2, Z, cmap='jet', alpha=0.6, edgecolor='none')
    
    # Plotando as curvas de nível no "chão" do gráfico (eixo Z limite inferior)
    offset_z = np.min(Z) - (np.max(Z) - np.min(Z)) * 0.2
    ax.contour(X1, X2, Z, zdir='z', offset=offset_z, cmap='gray', alpha=0.5)
    ax.set_zlim(offset_z, np.max(Z))
    
    # Configurando os pontos dos nossos algoritmos
    cores = {'GRS': 'black', 'LRS': 'magenta', 'Hill Climbing': 'cyan'}
    marcadores = {'GRS': 'o', 'LRS': '^', 'Hill Climbing': 's'} # Bolinha, triângulo, quadrado
    
    # Plotando cada resultado na superfície
    for nome, ponto in resultados.items():
        z_val = problema.funcao(ponto[0], ponto[1])
        # s=150 define o tamanho do marcador, depthshade=False deixa ele opaco
        ax.scatter(ponto[0], ponto[1], z_val, color=cores[nome], s=150, 
                   label=f"{nome} [Z={z_val:.2f}]", marker=marcadores[nome], depthshade=False, zorder=5)
        
    ax.set_title(f"Problema {num_prob} - Objetivo: {problema.tipo.upper()}")
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('f(X1, X2)')
    ax.legend()
    
    plt.show()

def gerar_graficos_experimento():
    rodadas = 100
    
    # Vamos gerar o gráfico apenas para a F1 e F3 como exemplo, 
    # senão abrirão 6 janelas na sua tela de uma vez.
    # Você pode mudar a lista [0, 2] para testar as outras! (0 = F1, 1 = F2, etc.)
    indices_para_plotar = [0, 2] 
    
    for idx in indices_para_plotar:
        problema = lista_problemas[idx]
        num_prob = idx + 1
        print(f"Calculando 100 rodadas para a F{num_prob}...")
        
        # Executa os algoritmos para pegar a moda (os hiperparâmetros devem ser os mesmos do seu main.py)
        grs = GlobalRandomSearch(problema)
        lrs = LocalRandomSearch(problema, sigma=0.5) 
        hc = HillClimbing(problema, epsilon=0.1)
        
        moda_grs = grs.executar_experimento(num_rodadas=rodadas)
        moda_lrs = lrs.executar_experimento(num_rodadas=rodadas)
        moda_hc = hc.executar_experimento(num_rodadas=rodadas)
        
        resultados_finais = {
            'GRS': moda_grs,
            'LRS': moda_lrs,
            'Hill Climbing': moda_hc
        }
        
        print(f"Abrindo gráfico da F{num_prob}...")
        plot_superficie_e_pontos(problema, num_prob, resultados_finais)

if __name__ == "__main__":
    gerar_graficos_experimento()