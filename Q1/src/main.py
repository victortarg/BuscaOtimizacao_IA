import os
import numpy as np
import matplotlib.pyplot as plt
from classes.funcoes import lista_funcoes
from algoritmos.grs import GlobalRandomSearch
from algoritmos.lrs import LocalRandomSearch
from algoritmos.hill_climbing import HillClimbing

def garantir_diretorio_existente(diretorio="graficos"):
    """Garante que a pasta para salvar os gráficos exista no projeto."""
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    return diretorio

def plot_superficie_e_salvar(problema, num_prob, resultados, pasta_destino="graficos"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    x1 = np.linspace(problema.limites[0, 0], problema.limites[0, 1], 25)
    x2 = np.linspace(problema.limites[1, 0], problema.limites[1, 1], 25)
    X1, X2 = np.meshgrid(x1, x2)
    
    Z = problema.funcao(X1, X2)
    
    superficie = ax.plot_surface(X1, X2, Z, cmap = 'viridis', alpha=0.6, edgecolor='none')
    
    offset_z = np.min(Z) - (np.max(Z) - np.min(Z)) * 0.2
    ax.contour(X1, X2, Z, zdir='z', offset=offset_z, cmap='gray', alpha=0.5)
    ax.set_zlim(offset_z, np.max(Z))
    
    cores = {'GRS': 'black', 'LRS': 'magenta', 'Hill Climbing': 'orange'}
    marcadores = {'GRS': 'o', 'LRS': '^', 'Hill Climbing': 's'}
    
    for nome, ponto in resultados.items():
        z_val = problema.funcao(ponto[0], ponto[1])
        ax.scatter(ponto[0], ponto[1], z_val, color=cores[nome], s=150, 
                   label=f"{nome} [Z={z_val:.2f}]", marker=marcadores[nome], depthshade=False, zorder=5)
        
    ax.set_title(f"Problema {num_prob} - Objetivo: {problema.tipo.upper()}")
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('f(X1, X2)')
    ax.legend()
    
    # --- VISUALIZAÇÃO  ANTES DE SALVAR ---
    plt.show(block=False) 
    plt.pause(0.1) 
    
    print("-" * 50)
    input(f"ENTER no terminal para salvar...")
    
    garantir_diretorio_existente(pasta_destino)
    nome_arquivo = f"resultado_funcao_f{num_prob}.png"
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    plt.savefig(caminho_completo, dpi=300, bbox_inches='tight')
    print(f"Gráfico da F{num_prob} salvo com sucesso em: {caminho_completo}\n")
    
    plt.close(fig)

def gerar_todos_os_graficos():
    rodadas = 100
    
    # Agora configurado para rodar e salvar as 6 funções automáticas de uma vez só!
    for idx, problema in enumerate(lista_funcoes):
        num_prob = idx + 1
        print(f"Calculando 100 rodadas para a F{num_prob}...")
        
        grs = GlobalRandomSearch(problema)
        lrs = LocalRandomSearch(problema, sigma=1.5) # 0.5 0.8(tava bom)
        hc = HillClimbing(problema, epsilon=1) # 0.1 0.5(ruim) 1(bom para quase todas, menos a f3 e f2)
        
        moda_grs = grs.executar_experimento(num_rodadas=rodadas)
        moda_lrs = lrs.executar_experimento(num_rodadas=rodadas)
        moda_hc = hc.executar_experimento(num_rodadas=rodadas)
        
        resultados_finais = {
            'GRS': moda_grs,
            'LRS': moda_lrs,
            'Hill Climbing': moda_hc
        }
        
        plot_superficie_e_salvar(problema, num_prob, resultados_finais)

if __name__ == "__main__":
    gerar_todos_os_graficos()