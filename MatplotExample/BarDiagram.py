import matplotlib.pyplot as plt
import numpy as np

users = ('Таня', 'Петя', 'Слава', 'Коля', 'Миша', 'Лена')
y_pos = np.arange(len(users))
age = [25, 28, 16, 34, 32, 41]

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

axs[0].bar(y_pos, age, color='r', align='center', alpha=0.5)
axs[0].set_xticks(y_pos, users)
axs[0].set_ylabel('Возраст')
axs[0].set_title('Вертикальная диаграмма')
axs[0].grid(True)

axs[1].barh(y_pos, age, color='g', align='center', alpha=0.5)
axs[1].set_xlabel('Возраст')
axs[1].set_yticks(y_pos, users)
axs[1].set_title('Горизонтальная диаграмма')
axs[1].grid(True)
plt.tight_layout()

plt.show()
