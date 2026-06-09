import numpy as np
from classes.problema import Problema # Sua classe Problema feita anteriormente

def f1(x1, x2):
    return x1**2 + x2**2

def f2(x1, x2):
    return np.exp(-(x1**2 + x2**2)) + 2 * np.exp(-((x1 - 1.7)**2 + (x2 - 1.7)**2))

def f3(x1, x2):
    termo1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2)))
    termo2 = -np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2)))
    return termo1 + termo2 + 20 + np.exp(1)

def f4(x1, x2):
    return (x1**2 - 10 * np.cos(2 * np.pi * x1) + 10) + (x2**2 - 10 * np.cos(2 * np.pi * x2) + 10)

def f5(x1, x2):
    return (x1 * np.cos(x1)) / 20 + 2 * np.exp(-(x1**2) - (x2 - 1)**2) + 0.01 * x1 * x2

def f6(x1, x2):
    return x1 * np.sin(4 * np.pi * x1) - x2 * np.sin(4 * np.pi * x2 + np.pi) + 1

lista_problemas = [
    Problema(f1, limites=[[-100, 100], [-100, 100]], tipo="min"),
    Problema(f2, limites=[[-2, 4], [-2, 5]], tipo="max"),
    Problema(f3, limites=[[-8, 8], [-8, 8]], tipo="min"),
    Problema(f4, limites=[[-5.12, 5.12], [-5.12, 5.12]], tipo="min"),
    Problema(f5, limites=[[-10, 10], [-10, 10]], tipo="max"),
    Problema(f6, limites=[[-1, 3], [-1, 3]], tipo="max")
]