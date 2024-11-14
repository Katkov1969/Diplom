import matplotlib.pyplot as plt

''' Построение круговой диаграммы в Matplotlib '''


def plot_pie_chart(labels, sizes):
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Круговая диаграмма')
    plt.axis('equal')  # Уравниваем оси для круговой формы
    plt.show()


# Вызов функции
labels = ['Категория A', 'Категория B', 'Категория C', 'Категория D']  # Cписок категорий
sizes = [15, 30, 45, 10]  # Список значений
plot_pie_chart(labels, sizes)
