import numpy as np

class GAPermutacao:
    def __init__(self, problema, tam_populacao=100, p_crossover=0.8, p_mutacao=0.01, elitismo_n=2):
        self.prob = problema
        self.N = tam_populacao
        self.pc = p_crossover
        self.pm = p_mutacao
        self.num_elitismo = elitismo_n
        
        # Cria a população inicial: cada linha é uma permutação única de índices de cidades
        self.P = np.array([np.random.permutation(self.prob.num_genes) for _ in range(self.N)])
        self.custos = np.zeros(self.N)
        self.avaliar_populacao()

    def avaliar_populacao(self):
        """Calcula o custo de distância para cada indivíduo da população."""
        for i in range(self.N):
            self.custos[i] = self.prob.calcular_custo_rota(self.P[i])

    def selecao_torneio(self, k_participantes=3):
        """Seleciona um pai utilizando o método do torneio (Minimização)."""
        indices = np.random.choice(self.N, size=k_participantes, replace=False)
        melhor_indice = indices[np.argmin(self.custos[indices])]
        return np.copy(self.P[melhor_indice])

    def crossover_dois_pontos_combinatorio(self, pai1, pai2):
        """Operador exigido no item 4 do edital para não repetir cidades."""
        if np.random.uniform() > self.pc:
            return np.copy(pai1), np.copy(pai2)

        tam = len(pai1)
        # Sorteia os dois pontos de corte aleatórios
        pt1, pt2 = sorted(np.random.choice(tam, size=2, replace=False))

        def preencher_filho(p1, p2):
            filho = np.full(tam, -1, dtype=int)
            # Propaga a seção central selecionada do primeiro pai
            filho[pt1:pt2] = p1[pt1:pt2]
            
            # Preenche o restante com os elementos do segundo pai na ordem em que aparecem, sem repetir
            pos_filho = 0
            for gene in p2:
                # Se o espaço do filho já está preenchido pelo bloco central, pula a posição
                if pos_filho == pt1:
                    pos_filho = pt2
                if gene not in filho:
                    filho[pos_filho] = gene
                    pos_filho += 1
            return filho

        return preencher_filho(pai1, pai2), preencher_filho(pai2, pai1)

    def mutacao_swap(self, cromossomo):
        """Mutação exigida no item 5: troca dois genes de posição (1% chance)."""
        if np.random.uniform() <= self.pm:
            idx1, idx2 = np.random.choice(len(cromossomo), size=2, replace=False)
            cromossomo[idx1], cromossomo[idx2] = cromossomo[idx2], cromossomo[idx1]
        return cromossomo

    def evoluir_geracao(self):
        nova_pop = []
        
        # --- ELITISMO (Item 7) ---
        # Preserva os melhores indivíduos sem alteração genética
        indices_ordenados = np.argsort(self.custos)
        for i in range(self.num_elitismo):
            nova_pop.append(np.copy(self.P[indices_ordenados[i]]))

        # Preenche o restante da população gerando prole
        while len(nova_pop) < self.N:
            pai1 = self.selecao_torneio()
            pai2 = self.selecao_torneio()

            filho1, filho2 = self.crossover_dois_pontos_combinatorio(pai1, pai2)
            
            filho1 = self.mutacao_swap(filho1)
            filho2 = self.mutacao_swap(filho2)

            nova_pop.append(filho1)
            if len(nova_pop) < self.N:
                nova_pop.append(filho2)

        self.P = np.array(nova_pop)
        self.avaliar_populacao()