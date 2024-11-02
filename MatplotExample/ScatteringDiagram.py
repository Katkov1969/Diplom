import matplotlib.pyplot as plt
import numpy as np

""" 
Диаграмма рассеяния 
"""


def plot_scatter(x_values, y_values):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, y_values, color='r', marker='x')
    plt.title('Диаграмма рассеяния')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid(True)
    plt.show()


# Вызов функции
x = np.random.rand(1, 100)  # Генерация случайных чисел
y = np.random.rand(1, 100)
plot_scatter(x, y)
