import os
import numpy as np
import matplotlib.pyplot as plt

def plotar_rota_drone_3d(problema, melhor_cromossomo, custo, pasta_destino="graficos"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    pontos = problema.pontos
    
    # Plota os pontos a serem visitados (cidades/alvos)
    ax.scatter(pontos[1:, 0], pontos[1:, 1], pontos[1:, 2], 
               c='royalblue', marker='o', s=50, alpha=0.6, label='Alvos a visitar')
    
    # Plota a origem (Base do Drone) em destaque
    ax.scatter(pontos[0, 0], pontos[0, 1], pontos[0, 2], 
               c='red', marker='*', s=300, edgecolors='black', label='Origem (Base)')
    
    # Reconstrói as coordenadas da rota na ordem exata
    rota_indices = np.concatenate(([0], melhor_cromossomo + 1, [0]))
    coordenadas_rota = pontos[rota_indices]
    
    # Desenha a linha conectando a trajetória
    ax.plot(coordenadas_rota[:, 0], coordenadas_rota[:, 1], coordenadas_rota[:, 2], 
            color='forestgreen', linewidth=1.5, alpha=0.8, label='Trajetória')
            
    ax.set_title(f"Trajetória Subótima do Drone 3D\nCusto Total: {custo:.2f} u.d.")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_zlabel("Eixo Z")
    ax.legend()
    
    # Salvamento automático
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    caminho_completo = os.path.join(pasta_destino, "trajetoria_drone_3d.png")
    plt.savefig(caminho_completo, dpi=300, bbox_inches='tight')
    
    plt.show()