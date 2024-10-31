import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def scatter_plot(data):
    """"
     Диаграмма рассеяния
     """
    data.head()
    sns.scatterplot(data=data, color='r', x="year", y="passengers")
    plt.grid(True)
    plt.show()

flights_data = sns.load_dataset("flights")   # Загрузка датасета из Seaborn
scatter_plot(flights_data)

#==========================================================================
def line_plot(data):
    """ Линейный график
    """
    sns.lineplot(data=data, x="year", y="passengers")
    plt.grid(True)
    plt.show()

line_plot(flights_data)