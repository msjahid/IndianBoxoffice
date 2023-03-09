import pandas as pd
from visualization.pxplotly import Chart

data = pd.read_csv('./data/highest_grossing_indian_films.csv',
                   engine='python',
                   nrows=50,
                   )


def bar_chart_instance():
    chart = Chart(data=data, film='Film', rank='Rank', primary_language='Primary  language',
                  worldwide_gross='Worldwide gross', year='Year', studio='Studio(s)',
                  director='Director', title='Top Grossing Indian Films')
    return chart.plot_bar_chart()


def bubble_chart_instance():
    chart = Chart(data=data, year='Year', film='Film', rank='Rank', studio='Studio(s)',
                  primary_language='Primary  language', worldwide_gross='Worldwide gross',
                  director='Director', title='Highest Grossing Indian Films by Year, Film, and Language')
    return chart.bubble_chart()


def line_chart_instance():
    chart = Chart(data=data, year='Year', film='Film', rank='Rank', studio='Studio(s)',
                  primary_language='Primary  language', worldwide_gross='Worldwide gross',
                  director='Director', title='Yearly Highest Grossing Indian Films')
    return chart.line_chart()


def heatmap_chart_instance():
    chart = Chart(data=data, year='Year', film='Film', rank='Rank', studio='Studio(s)',
                  primary_language='Primary  language', worldwide_gross='Worldwide gross',
                  director='Director', title='Distribution of Worldwide Gross Earnings by Primary Language')
    return chart.heatmap_chart()


def box_plot_instance():
    chart = Chart(data=data, year='Year', film='Film', rank='Rank', studio='Studio(s)',
                  primary_language='Primary  language', worldwide_gross='Worldwide gross',
                  director='Director', title='Distribution of Worldwide Gross Earnings by Studio and Rank')
    return chart.box_plot()


def area_chart_instance():
    chart = Chart(data=data, year='Year', film='Film', rank='Rank', studio='Studio(s)',
                  primary_language='Primary  language', worldwide_gross='Worldwide gross',
                  director='Director', title='Composition of Worldwide Gross Earnings by Primary Language, Genre, '
                                             'and Director')
    return chart.area_chart()
