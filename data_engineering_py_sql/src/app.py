import os
import psycopg2
import pandas as pd 
from PIL import Image
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv

# Load the environment variables 
load_dotenv()


API_KEY         =   os.getenv("API_KEY")
API_HOST        =   os.getenv("API_HOST")
LEAGUE_ID       =   os.getenv("LEAGUE_ID")
SEASON          =   os.getenv("SEASON")
DB_NAME         =   os.getenv("DB_NAME")
DB_USERNAME     =   os.getenv("DB_USERNAME")
DB_PASSWORD     =   os.getenv("DB_PASSWORD")
DB_HOST         =   os.getenv("DB_HOST")
DB_PORT         =   os.getenv("DB_PORT")



# Set up Postgres database connection
postgres_connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host="localhost",
    port="5432" 
)


# Get a cursor from the database
cur = postgres_connection.cursor()



# Fetch the Premier League data from Postgres
get_premier_league_standings_sql_query = """
    SELECT 
        position
        ,team
        ,games_played
        ,wins
        ,draws
        ,losses
        ,goals_for
        ,goals_against
        ,goal_difference
        ,points
    FROM 
        public.premier_league_standings_vw
    ORDER BY 
        wins DESC;
"""

# Read football data into dataframe
final_standings_df = pd.read_sql(get_premier_league_standings_sql_query, postgres_connection)

print(final_standings_df)


# # Remove the index displayed
# # final_standings_df.set_index('position', inplace=True)


# # Close database connection
# postgres_connection.close()


# Set the page configuration of the app
st.set_page_config(
    page_title      =   "Premier League Standings 2023/24",
    page_icon       =   "⚽",
    layout          =   "wide"
)


# # Create title

st.title(f"⚽🏆 Premier League Table Standings {SEASON} ⚽🏆") 
st.write("")


# # Display instructions
st.sidebar.title('Instructions 📖')
st.sidebar.write(f"""
The table showcases the current Premier League standings for the {SEASON} season. Toggle visualizations to gain deeper insights!
""")


show_visualization = st.sidebar.radio('Would you like to view the standings as a visualization too?', ('No', 'Yes'))
fig_specification  = px.bar(final_standings_df, 
                        x           =   'team', 
                        y           =   'points', 
                        title       =   f'Premier League Standings {SEASON}', 
                        labels      =   {'points':'Points', 'team':'Team', 'goals_for': 'Goals Scored', 'goals_against': 'Goals Conceded', 'goal_difference':'Goal Difference'},
                        color       =   'team',
                        height      =   700,
                        hover_data  =   ['goals_for', 'goals_against', 'goal_difference']
)

if show_visualization == 'Yes':
    st.table(final_standings_df)
    st.write("")
    fig = fig_specification 
    st.plotly_chart(fig, use_container_width=True)
else:
    st.table(final_standings_df)




# Miscellaneous watermark

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.title("Modified by WA✨")