import streamlit as st
import plotly.express as px


class Chart:
    def __init__(self, data, film, rank, primary_language, worldwide_gross, studio, year, director, title=None,
                 height=600, width=800):
        self.data = data
        self.film = film
        self.rank = rank
        self.primary_language = primary_language
        self.worldwide_gross = worldwide_gross
        self.studio = studio
        self.year = year
        self.director = director
        self.title = title
        self.height = height
        self.width = width

    # create a plot bar chart
    def plot_bar_chart(self):
        fig = px.bar(data_frame=self.data, x=self.film,
                     y=self.worldwide_gross, color=self.year, title=self.title,
                     height=self.height, width=self.width)
        st.plotly_chart(fig)

    # create a bubble chart
    def bubble_chart(self):
        fig = px.scatter(data_frame=self.data, x=self.year, y=self.film, color=self.primary_language, title=self.title,
                         height=self.height, width=self.width)
        st.plotly_chart(fig)

    # create a line chart
    def line_chart(self):
        fig = px.line(data_frame=self.data, x=self.rank, y=self.worldwide_gross, color=self.year, title=self.title,
                      height=self.height, width=self.width)
        st.plotly_chart(fig)

    # create a heatmap chart
    def heatmap_chart(self):
        fig = px.histogram(data_frame=self.data, x=self.primary_language, y=self.worldwide_gross,
                           color=self.year, nbins=20, title=self.title, height=self.height, width=self.width)
        st.plotly_chart(fig)

    # Create a box plot
    def box_plot(self):
        fig = px.box(data_frame=self.data, x=self.studio, y=self.worldwide_gross, color=self.rank,
                     height=self.height, width=self.width)
        st.plotly_chart(fig)

    # create a area chart
    def area_chart(self):
        fig = px.area(data_frame=self.data, x=self.year, y=self.worldwide_gross,
                      color=self.primary_language, line_group=self.director, title=self.title,
                      height=self.height, width=self.width)
        st.plotly_chart(fig)
