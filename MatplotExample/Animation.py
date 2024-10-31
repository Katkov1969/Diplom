import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def animate_sine_wave():                         # функция будет создавать и отображать анимацию синусоидальной волны
    fig, ax = plt.subplots()                      # Создает фигуру (fig) и набор осей (ax).
    x = np.linspace(0, 2 * np.pi, 100)  # Создает массив x из 100 равномерно распред. точек от 0 до (2pi).
    """
    Создается начальный график синусоидальной волны. ax.plot() возвращает список линий,
    и запятая после line распаковывает его. np.sin(x) вычисляет синус для каждого значения в массиве x.
    """
    line, = ax.plot(x, np.sin(x))


    def update(frame):                # функция будет вызываться для обновления графика на каждом шаге анимации.
        """
        Обновляет данные по оси Y линии, смещая синусоидальную волну на frame / 10.0 радиан.
        Это создает эффект движения волны. Возвращает обновленный объект линии. Запятая необходима для
        возврата в виде кортежа, что требуется для правильной работы с blit
        """
        line.set_ydata(np.sin(x + frame / 10.0))  #
        return line,

    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True) # Создает объект анимации ani.
    """
    fig: Фигура, на которой будет отображаться анимация.
    update: Функция, которая будет вызываться для обновления графика.
    frames=np.arange(0, 100): Генерирует последовательность кадров от 0 до 99.
    blit=True: Оптимизирует процесс анимации, перерисовывая только те части, которые изменились.
    """
    plt.grid(True)
    plt.show()

# Вызов функции для создания анимации
animate_sine_wave()