import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

'''
Создание графика с использованием Dash
'''

# Создание приложения Dash
app = dash.Dash(__name__)

# Генерация данных
df = pd.DataFrame({
    "Фрукты": ["Яблоки", "Апельсины", "Бананы", "Яблоки", "Апельсины", "Бананы"],
    "Количество": [4, 1, 2, 2, 4, 5],
    "Город": ["Ставрополь", "Ставрополь", "Ставрополь", "Москва", "Москва", "Москва"]
})

# Создание графика с помощью Plotly Express
fig = px.bar(df, x="Фрукты", y="Количество", color="Город", barmode="group")

# Определение макета приложения
app.layout = html.Div(children=[
    html.H1(children='Hello Dash!!!'),
    html.Div(children='''Dash: Фреймворк веб-приложения для Python.'''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
