# Busca e Otimização Meta-heurística

Este repositório contém as implementações práticas de algoritmos de Inteligência Artificial para a resolução de problemas contínuos e discretos utilizando busca e otimização meta-heurística.

## Estrutura do Projeto

O projeto está dividido em três seções principais, cada uma contendo sua própria lógica de execução:

* **Q1:** Otimização de funções contínuas utilizando Global Random Search (GRS), Local Random Search (LRS) e Hill Climbing.
* **Q2.1 e Q2.2:** Resolução de problemas discretos/combinatórios, incluindo o Problema das 8 Rainhas (Têmpera Simulada) e o Problema do Caixeiro-Viajante Tridimensional para Drones (Algoritmo Genético de Permutação).
* **Q3:** Análise comparativa em alta dimensionalidade (50D) entre um Algoritmo Genético Não Canônico (Crossover SBX e Mutação Gaussiana) e o LRS.

## Pré-requisitos

Para executar este projeto, é necessário ter instalado em sua máquina:

* Python 3.8 ou superior.

## Configuração do Ambiente Virtual (venv)

É uma boa prática na comunidade Python utilizar um Ambiente Virtual (`venv`) para isolar as dependências do projeto. Isso impede que as bibliotecas instaladas interfiram em outros projetos na sua máquina.

Siga os passos abaixo no terminal, na pasta raiz do projeto:

### 1. Criar o ambiente virtual

Execute o seguinte comando para criar uma pasta oculta chamada `venv` que conterá o ambiente isolado:

**No Windows, Linux ou macOS:**

```bash
python -m venv venv

```

### 2. Ativar o ambiente virtual

Antes de instalar as dependências ou rodar o código, você deve ativar o ambiente.

**No Windows (Prompt de Comando ou PowerShell):**

```bash
venv\Scripts\activate

```

**No Linux ou macOS:**

```bash
source venv/bin/activate

```

*Nota: Você saberá que o ambiente está ativado quando o nome `(venv)` aparecer no início da linha do seu terminal.*

### 3. Instalar as dependências

Com o ambiente ativado, instale as bibliotecas matemáticas e de plotagem necessárias utilizando o arquivo de requisitos:

```bash
pip install -r requirements.txt

```

## Como Executar o Projeto

Certifique-se de que o seu terminal está com o ambiente virtual ativado e navegue até a pasta `src` da questão que deseja avaliar.

### Parte 1: Funções Contínuas

Para gerar os resultados, as superfícies 3D e os pontos de parada dos algoritmos GRS, LRS e Hill Climbing:

```bash
cd Q1/src
python main.py

```

### Parte 2.1: Problema das 8 Rainhas

Para buscar as 92 soluções únicas no tabuleiro utilizando a Têmpera Simulada e renderizar o gráfico do tabuleiro:

```bash
cd Q2.1/src
python main.py

```

### Parte 2.2: Caixeiro-Viajante 3D (Drones)

Para otimizar a rota combinatória do drone utilizando o Algoritmo Genético e gerar o gráfico de convergência:

```bash
cd Q2.2/src
python main_pcv.py

```

### Parte 3: Comparação de Métodos (Rastrigin 50D)

Para rodar a comparação entre o Algoritmo Genético Não Canônico e o Local Random Search sob um orçamento computacional fixo de 10.000 avaliações:

```bash
cd Q3/src
python main.py

```

## Desativando o Ambiente Virtual

Após terminar de testar os códigos, você pode desativar o ambiente virtual e retornar ao ambiente global do Python executando simplesmente:

```bash
deactivate

```
