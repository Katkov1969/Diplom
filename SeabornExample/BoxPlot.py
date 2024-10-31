import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_boxplot(data, labels):
    """
    Строит диаграмму размаха.
    data: Список числовых значений, сгруппированных по категориям.
    labels: Метки категорий.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data)
    plt.xticks(ticks=np.arange(len(labels)), labels=labels)
    plt.title('Ящик с усами')
    plt.xlabel('Категории')
    plt.ylabel('Значение')
    plt.grid(True)
    plt.show()

""" 
Генератор норм распр. 
loc - центр 0-3, 
scale - разброс 
"""
data = [np.random.normal(loc, 1, 100) for loc in range(4)]
print(data)
labels = ['A', 'B', 'C', 'D']
plot_boxplot(data, labels)
