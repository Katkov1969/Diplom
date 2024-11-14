import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Диаграмма рассеяния с регрессионной линией Seaborn
"""


def plot_scatter_with_regression(x, y):
    sns.set(style="darkgrid")  # Установка стиля Seaborn
    plt.figure(figsize=(10, 6))
    sns.regplot(x=x, y=y, color='m')
    plt.title('Диаграмма рассеяния с регрессионной линией')
    plt.xlabel('Значение X')
    plt.ylabel('Значение Y')
    plt.grid(True)
    plt.show()


# Вызов
x = np.random.rand(100)
y = x + np.random.rand(100)

plot_scatter_with_regression(x, y)
