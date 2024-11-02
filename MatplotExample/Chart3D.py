import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

""" Построение линий и точек"""


def lines_points_3D(x, y, z):
    # Создается фигура и 3D-оси
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Строятся точки
    ax.scatter(x, y, z, c='b', marker='o')

    # Точки соединяются линиями
    for i in range(len(x)):
        ax.plot([0, x[i]], [0, y[i]], [0, z[i]], color='r', alpha=0.3)

    # Устанавливаются метки и заголовок
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Точки и линии')

    plt.show()


# Генерируются случайные точки
x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(size=100)

# Вызовфункции
lines_points_3D(x, y, z)

"""********************************************************************************************"""

"""График поверхности"""


def plot_3d_surface(x, y, z):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')  # Цветовая схема
    ax.set_title('3D поверхностный график')
    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')
    ax.set_zlabel('Ось Z')
    plt.show()


# Вызов функции
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.cos(np.sqrt(x ** 2 + y ** 2))
plot_3d_surface(x, y, z)

"""***************************************************************************"""

""" Каркасный график"""


def plot_3d_wireframe(x, y, z):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, color='r')  # Цветовая схема
    ax.set_title('3D каркасный график')
    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')
    ax.set_zlabel('Ось Z')
    plt.show()


# Вызов функции
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x ** 2 + y ** 2))
plot_3d_wireframe(x, y, z)

"""***************************************************************************************"""
