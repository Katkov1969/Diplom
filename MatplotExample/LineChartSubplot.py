import matplotlib.pyplot as plt
import numpy as np

""" Компоновка двух графиков в одном окне """


def plot_multiple_subplots(x, y1, y2):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    axs[0].plot(x, y1, 'r', label='sin(x)')
    axs[0].set_title('Подграфик 1')
    axs[0].set_ylabel('sin x')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(x, y2, 'b', label='cos(x)')
    axs[1].set_title('Подграфик 2')
    axs[1].set_xlabel('Ось X')
    axs[1].set_ylabel('cos x')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()


# вызов
x_min = -4
x_max = 4
dx = 0.1

x = np.arange(x_min, x_max + dx, dx)
y1 = np.sin(x)
y2 = np.cos(x)

plot_multiple_subplots(x, y1, y2)
