import matplotlib.pyplot as plt
import numpy as np
"""    
Построение гистограммы на основе предоставленных данных 
data - список числовых значений 
bins - количество бинов на гистограмме
"""

def plot_histogram(data, bins):

    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, color='c', edgecolor='k')
    plt.title('Гистограмма распределения')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()

    # вызов
data = np.random.normal(loc=0, scale=1, size=1000)
plot_histogram(data, 20)

