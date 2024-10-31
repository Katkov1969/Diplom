import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_heatmap(data):
    """
    Тепловая карта матрицы 5 на 8
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, vmin=0, vmax=1,  annot=True, cmap='coolwarm')
    plt.title('Тепловая карта')
    plt.show()

data = np.random.rand(5, 8)
plot_heatmap(data)

def plot_corr_heatmap(data1):
    """
    Тепловая карта корреляционной матрицы 6 на 6
    """
    df = pd.DataFrame(data1)
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Тепловая карта корреляционной матрицы')
    plt.show()

data1 = np.random.rand(6, 6)
plot_corr_heatmap(data1)


