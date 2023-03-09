import os
import streamlit as st
import asyncio
import pandas as pd
from . types_chart import *
# from data.buildcsv import create_csv_file
chart_instances = [bar_chart_instance, bubble_chart_instance, line_chart_instance, heatmap_chart_instance,
                   box_plot_instance, area_chart_instance]


class MyApp:
    def __init__(self):
        self.text = """
            <h1 style='
                font-size: 30px;
                color:red;
                -webkit-background-clip: text;
            '>
                List of Indian Highest Grossing Movies
            </h1>
        """
        csv_file_path = './data/highest_grossing_indian_films.csv'
        if not os.path.exists(csv_file_path):
            print(f"File not found at {csv_file_path}.")
            # handle the exception as per your requirement

        self.data = pd.read_csv(csv_file_path)

    async def run(self):
        st.set_page_config(page_title="Indian Highest Grossing Movies",
                           page_icon=":smiley:",
                           layout="wide",
                           )

        with st.container():
            st.write(self.text, unsafe_allow_html=True)

        st.sidebar.header('Please Filter Here:')
        selected_languages = st.sidebar.multiselect(
            "Select Primary language:",
            options=self.data["Primary  language"].unique(),
            default=self.data["Primary  language"].unique()
        )

        year = st.sidebar.slider('Select Year:', min_value=int(self.data['Year'].min()),
                                 max_value=int(self.data['Year'].max()),
                                 value=(int(self.data['Year'].min()), int(self.data['Year'].max())))

        filtered_data = self.data[
            self.data['Primary  language'].isin(selected_languages) & self.data['Year'].between(year[0], year[1])]

        st.dataframe(filtered_data)

        for chart in chart_instances:
            chart()

        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
