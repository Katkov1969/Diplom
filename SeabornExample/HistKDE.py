import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

"""
    Строит гистограмму и оценку плотности распределения
    """


def plot_hist_kde(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=True, color='b', bins=30)
    plt.title('Гистограмма и KDE')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()


# Вызов
data = np.random.normal(loc=0, scale=1, size=1000)
plot_hist_kde(data)
