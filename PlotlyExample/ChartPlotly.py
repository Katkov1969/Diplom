import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np


def plot_interactive_line(x, y):
    """ Интерактивный линейный график"""
    trace = go.Scatter(x=x, y=y, mode='lines+markers', name='Линия')
    layout = go.Layout(title='Интерактивный линейный график', xaxis=dict(title='Ось X'), yaxis=dict(title='Ось Y'))
    fig = go.Figure(data=[trace], layout=layout)
    pyo.plot(fig, filename='interactive_line.html')

# Вызов функции
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plot_interactive_line(x, y)

#***************************************************************************************************


def plot_interactive_histogram(data):
    """ Интерактивная гистограмма"""
    trace = go.Histogram(x=data, nbinsx=30, marker=dict(color='blueviolet'))
    layout = go.Layout(title='Интерактивная гистограмма', xaxis=dict(title='Значение'), yaxis=dict(title='Частота'))
    fig = go.Figure(data=[trace], layout=layout)
    pyo.plot(fig, filename='interactive_histogram.html')

# Вызов функции
data = np.random.normal(0, 1, 1000)
plot_interactive_histogram(data)

#*************************************************************************************************


def plot_interactive_scatter(x, y):
    """ Интерактивная диаграмма рассеяния"""
    trace = go.Scatter(x=x, y=y, mode='markers', marker=dict(size=10, color='rgba(125, 0, 0, .8)'))
    layout = go.Layout(title='Интерактивная диаграмма рассеяния', xaxis=dict(title='Ось X'), yaxis=dict(title='Ось Y'))
    fig = go.Figure(data=[trace], layout=layout)
    pyo.plot(fig, filename='interactive_scatter.html')

# Вызов функции
x = np.random.rand(100)
y = np.random.rand(100)
plot_interactive_scatter(x, y)

#*******************************************************************************************


def plot_interactive_3d_surface(x, y, z):
    """ Интерактивный 3D график поверхности"""
    trace = go.Surface(z=z, x=x, y=y, colorscale='Viridis')
    layout = go.Layout(title='Интерактивный 3D график', scene=dict(xaxis=dict(title='Ось X'), yaxis=dict(title='Ось Y'), zaxis=dict(title='Ось Z')))
    fig = go.Figure(data=[trace], layout=layout)
    pyo.plot(fig, filename='interactive_3d_surface.html')

# Вызов функции
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = (np.cos(np.sqrt(x**2 + y**2)))**2
plot_interactive_3d_surface(x, y, z)


