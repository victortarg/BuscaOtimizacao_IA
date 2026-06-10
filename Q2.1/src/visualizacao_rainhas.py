import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plotar_tabuleiro_rainhas(solucao, numero_solucao=1, pasta_destino="graficos"):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    tabuleiro = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            tabuleiro[i, j] = (i + j) % 2
            
    cmap_xadrez = ListedColormap(['#f0d9b5', '#b58863'])
    
    ax.imshow(tabuleiro, cmap=cmap_xadrez, extent=[0.5, 8.5, 0.5, 8.5], origin='lower')
    
    for col_idx, linha_idx in enumerate(solucao):
        coluna_real = col_idx + 1
        linha_real = linha_idx + 1
        
        ax.text(coluna_real, linha_real, '♟️', fontsize=30, ha='center', va='center', zorder=3)
        
    ax.set_xticks(range(1, 9))
    ax.set_yticks(range(1, 9))
    ax.set_xticklabels([str(i) for i in range(1, 9)], fontsize=12, fontweight='bold')
    ax.set_yticklabels([str(i) for i in range(1, 9)], fontsize=12, fontweight='bold')
    
    ax.set_xticks(np.arange(0.5, 9.5, 1), minor=True)
    ax.set_yticks(np.arange(0.5, 9.5, 1), minor=True)
    ax.grid(which='minor', color='#7a583a', linestyle='-', linewidth=2)
    
    ax.tick_params(which='both', top=False, bottom=False, left=False, right=False)
    
    vetor_professor = tuple(np.array(solucao) + 1)
    ax.set_title(f"Problema das 8 Rainhas - Solução #{numero_solucao}", 
                 fontsize=14, fontweight='bold', pad=15)
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    nome_arquivo = f"tabuleiro_rainhas_solucao_{numero_solucao}.png"
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    plt.savefig(caminho_completo, dpi=300, bbox_inches='tight')
    plt.show()