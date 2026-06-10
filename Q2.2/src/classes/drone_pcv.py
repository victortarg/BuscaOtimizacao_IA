import os
import numpy as np

class DronePCV:
    def __init__(self, num_pontos_por_regiao=40, nome_csv="CaixeiroGruposGA.csv"):
        self.num_pontos = num_pontos_por_regiao
        pasta_classes = os.path.dirname(os.path.abspath(__file__))
        pasta_raiz_projeto = os.path.dirname(os.path.dirname(pasta_classes))
        self.caminho_csv = os.path.join(pasta_raiz_projeto, "dataset", nome_csv)

        self.pontos = self._carregar_pontos()
        self.origem = self.pontos[0]
        self.num_genes = len(self.pontos) - 1 

    def _carregar_pontos(self):
        """Carrega os dados do arquivo CSV e lança erro caso não exista."""
        if os.path.exists(self.caminho_csv):
            print(f"Carregando pontos de: {self.caminho_csv}")
            dados = np.genfromtxt(self.caminho_csv, delimiter=',', skip_header=1)
            return dados[:, :3] # Retorna apenas as colunas X, Y, Z
        else:
            raise FileNotFoundError(
                f"Caminho tentado: {self.caminho_csv}\n"
                f"Verifique se o nome do arquivo está idêntico ."
            )

    def calcular_custo_rota(self, cromossomo):
        """
        Métrica de Aptidão: Calcula a distância total percorrida em 3D.
        Rota: Origem -> Cidades do Cromossomo -> Origem.
        """
        # Reconstrói a rota real convertendo os índices em coordenadas
        # Adiciona o índice 0 (origem) no início e no fim
        rota_indices = np.concatenate(([0], cromossomo + 1, [0]))
        coordenadas_rota = self.pontos[rota_indices]
        
        # Calcula as diferenças entre pontos consecutivos em X, Y, Z
        diferencas = np.diff(coordenadas_rota, axis=0)
        # Distância Euclidiana 3D de toda a rota somada
        distancia_total = np.sum(np.sqrt(np.sum(diferencas**2, axis=1)))
        return distancia_total