import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available) #Вывод списка доступных стилей

"""
Построение линейных графиков в Matplotlib
"""

"""******************************************************************************************************"""
"""
    Линейный график на основе предоставленных данных x и y.
"""
def plot_line_chart(x_values, y_values):

    plt.figure(figsize=(10, 6))  # Устанавливаем размер графика

    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Данные_1')  # Строим график

    plt.title('Линейный график')  # Заголовок графика
    plt.xlabel('Ось X')  # Метка оси X
    plt.ylabel('Ось Y')  # Метка оси Y
    plt.grid(True)  # Включаем сетку
    plt.legend()  # Добавляем легенду
    plt.show()  # Отображаем график


# Вызов функции
x = [1, 2, 3, 4, 5]
y = [4, 6, 8, 14, 18]

# Вызов функции
plot_line_chart(x, y)


''' *************************************************************************************************'''

"""
    Два графика на одной плоскости
"""

def plot_two_chart(x_value, y_value, k_value, z_value):

    plt.style.use('ggplot')

    plt.figure(figsize=(10, 6))  # Устанавливаем размер графика
    plt.plot(x_value, y_value, marker='o', linestyle='-', color='b', label='Данные_1')  # Строим график 1
    plt.plot(k_value, z_value, marker='>', linestyle='--', color='r', label='Данные_2', markerfacecolor='k')  # график 2

    plt.title('Два графика на плоскости ', fontsize=16, fontweight='bold')  # Заголовок графика
    plt.xlabel('Ось X', fontsize=14, fontweight='bold')  # Метка оси X
    plt.ylabel('Ось Y', fontsize=14, fontweight='bold')  # Метка оси Y
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=12)
    plt.grid(True)  # Включаем сетку
    plt.legend()  # Добавляем легенду

    plt.show()


""" Данные для графика линии"""
x = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
y = [0.1, 0.3, 0.6, 1.0, 1.4, 1.3, 1.8, 2.0, 1.6, 2.2]

""" Данные для графика кривой"""
k_min = -2
k_max = 10
dk = 0.2

""" Cписок координат по оси X для кривой на отрезке [k_min; K_max], включая концы"""
k = np.arange(k_min, k_max + dk, dk)
z = np.sin(0.2 * k) * np.cos(k)

# Вызов функции
plot_two_chart(x, y, k, z)


''' ********************************************************************************************************'''
"""  График с двумя осями Y"""

def plot_dual_axis(x_values, y1_values, y2_values):
    plt.style.use('seaborn-v0_8-colorblind')
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel('Время')
    ax1.set_ylabel('Температура', color='r')
    ax1.plot(x_values, y1_values, color='r')
    ax1.tick_params(axis='y', labelcolor='r')

    ax2 = ax1.twinx()  # Создаем вторую ось Y, которая делит ось X с ax1
    ax2.set_ylabel('Влажность', color='b')
    ax2.plot(x_values, y2_values, color='b')
    ax2.tick_params(axis='y', labelcolor='b')

    fig.tight_layout()  # Устраняем наложение меток
    plt.title('График с двумя осями Y', fontsize=14)
    plt.show()


# Вызов функции
x = np.arange(0, 10, 1)
y1 = [30, 32, 34, 33, 31, 29, 28, 27, 30, 32]
y2 = [75, 70, 72, 68, 65, 64, 70, 72, 74, 73]
plot_dual_axis(x, y1, y2)
