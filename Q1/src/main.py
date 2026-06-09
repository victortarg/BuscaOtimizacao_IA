from classes.problemas import lista_problemas
from algoritmos.grs import GlobalRandomSearch
from algoritmos.lrs import LocalRandomSearch
from algoritmos.hill_climbing import HillClimbing

def rodar_experimentos():
    rodadas = 100
    
    print(f"{'Prob.':<6} | {'GRS Moda (x1, x2)':<25} | {'LRS Moda (x1, x2)':<25} | {'Hill Climbing Moda (x1, x2)':<25}")
    print("-" * 85)
    
    for idx, problema in enumerate(lista_problemas):
        num_prob = idx + 1
        
        # Instanciando os algoritmos.
        grs = GlobalRandomSearch(problema)
        lrs = LocalRandomSearch(problema, sigma=0.5) 
        hc = HillClimbing(problema, epsilon=0.1)
        
        moda_grs = grs.executar_experimento(num_rodadas=rodadas)
        moda_lrs = lrs.executar_experimento(num_rodadas=rodadas)
        moda_hc = hc.executar_experimento(num_rodadas=rodadas)
        
        str_grs = f"[{moda_grs[0]:.2f}, {moda_grs[1]:.2f}]"
        str_lrs = f"[{moda_lrs[0]:.2f}, {moda_lrs[1]:.2f}]"
        str_hc = f"[{moda_hc[0]:.2f}, {moda_hc[1]:.2f}]"
        
        print(f"F{num_prob:<5} | {str_grs:<25} | {str_lrs:<25} | {str_hc:<25}")

if __name__ == "__main__":
    rodar_experimentos()