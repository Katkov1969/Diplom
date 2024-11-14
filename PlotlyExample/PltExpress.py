import plotly.express as px
"""
Использование PlotlyExpress
Кластеризация ирисов Фишера
"""
df = px.data.iris()
fig = px.scatter(df,
                 x="sepal_width", y="sepal_length",
                 color="species",
                 title="A Plotly Express Figure")
fig.show()
