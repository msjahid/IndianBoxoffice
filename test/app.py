import pandas as pd
import plotly.express as px
import streamlit_app as st

text = """
    <h1 style='
        font-size: 30px;
        color:red;
        -webkit-background-clip: text;
    '>
        List of Indian Highest Grossing Movies
    </h1>
"""

st.set_page_config(page_title="Indian Highest Grossing Movies",
                   page_icon=":movie_camera:",
                   layout="wide",
                   )

with st.container():
    st.write(text, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

data = pd.read_csv('data/highest_grossing_indian_films.csv',
                   engine='python',
                   nrows=50,
                   )

st.sidebar.header('Please Filter Here:')
selected_languages = st.sidebar.multiselect(
    "Select Primary language:",
    options=data["Primary language"].unique(),
    default=data["Primary language"].unique()
)

year = st.sidebar.slider('Select Year:', min_value=int(data['Year'].min()), max_value=int(data['Year'].max()),
                         value=(int(data['Year'].min()), int(data['Year'].max())))

# customer_type = st.sidebar.multiselect(
#     "Select the Customer Type:",
#     options=data["Customer_type"].unique(),
#     default = data["Customer_type"].unique()
# )
#
# gender = st.sidebar.multiselect(
#     "Select the Gender:",
#     options = data["Gender"].unique(),
#     default = data["Gender"].unique()
# )
#
# language_selection = data[data["Primary language"].isin(selected_languages)]
# language_selection = data.query('`Primary language`.isin(@film)')
# &Customer_type == @customer_type & Gender == @gender"

filtered_data = data[data['Primary language'].isin(selected_languages) & data['Year'].between(year[0], year[1])]

st.dataframe(filtered_data)
# data["Gender"].hist()

# graph = """
#     <h2 style='
#         font-size: 15px;
#         color:Blue;
#         -webkit-background-clip: text;
#     '>
#         Bar plot worldwide gross Highest Grossing Indian Films
#     </h1>
# """
#
#
# with st.container():
#     st.write(graph, unsafe_allow_html=True)