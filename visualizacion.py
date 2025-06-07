import streamlit as st
import pandas as pd
import base64
import numpy as np

from views.circuitsView import circuitsView
from views.driversView import driversView


# Leemos los CSV y obtenemos asi los datos sobre los que trabajar
races = pd.read_csv('dataBase/races.csv')  #
results = pd.read_csv('dataBase/results.csv')  #
circuits = pd.read_csv('dataBase/circuits.csv')  #
drivers = pd.read_csv('dataBase/drivers.csv')    #
constructors = pd.read_csv('dataBase/constructors.csv')  #

# Lo primero que vamos a hacer es unir todos los dataframes para tener un dataframe con toda la informacion
races = races[['raceId', 'year', 'circuitId', 'date', 'name']]
races = races.rename(columns={'name': 'raceName'})

races = races.merge(circuits, on='circuitId', how='left')
races = races[['raceId', 'year', 'circuitId', 'date', 'raceName', 'name', 'location', 'country', 'lat', 'lng', 'url']]
races = races.rename(columns={'name': 'circuitName', 'url': 'circuitUrl'})

races = races.merge(results, on='raceId', how='left')
races = races[['raceId', 'year', 'circuitId', 'date', 'raceName', 'circuitName', 'location', 'country', 'lat', 'lng', 'circuitUrl',
               'resultId', 'driverId', 'constructorId', 'grid', 'position', 'points', 'milliseconds', 'fastestLapTime']]

races = races.merge(drivers, on='driverId', how='left')
races = races[['raceId', 'year', 'circuitId', 'date', 'raceName', 'circuitName', 'location', 'country', 'lat', 'lng', 'circuitUrl',
               'resultId', 'driverId', 'constructorId', 'grid', 'position', 'points', 'milliseconds', 'fastestLapTime', 
               'forename', 'surname', 'nationality','url']]
races = races.rename(columns={'nationality': 'driverNationality', 'url': 'driverUrl'})

races = races.merge(constructors, on='constructorId', how='left')
races = races[['raceId', 'year', 'circuitId', 'date', 'raceName', 'circuitName', 'location', 'country', 'lat', 'lng', 'circuitUrl',
               'resultId', 'driverId', 'constructorId', 'grid', 'position', 'points', 'milliseconds', 'fastestLapTime', 
               'forename', 'surname', 'driverNationality','driverUrl', 'name', 'nationality']]
races = races.rename(columns={'name':'teamName', 'nationality': 'teamNationality'})

races = races[['year', 'date', 'raceName', 'circuitName', 'location', 'country', 'lat', 'lng', 'grid', 'position', 'points', 'milliseconds', 
               'fastestLapTime', 'driverId', 'forename', 'surname', 'driverNationality', 'teamName', 'teamNationality', 'driverUrl', 'circuitUrl']]


# Ordenamos el dataframe por fecha y ponermos a nulos los valores de posición y grid que sean 0 (no clasificado / no acaba la carrera) pues a veces vienen como 0 y no nan
races['date'] = pd.to_datetime(races['date'])
races = races.sort_values('date')
races['position'] = races['position'].replace({0: np.nan, '0': np.nan})
races['grid'] = races['grid'].replace({0: np.nan, '0': np.nan})





# Configuaramos la página de Streamlit
st.set_page_config(
    page_title="Informacion de Fórmula 1",
    page_icon=":racing_car:",
    layout="wide"
)

# Cargar fuente TTF y convertir a base64
with open("Formula1-Regular.otf", "rb") as f:
    font_data = f.read()
    font_base64 = base64.b64encode(font_data).decode()

# Inyectar estilo global para usar la fuente como predeterminada
st.markdown(f"""
    <style>
    @font-face {{
        font-family: "F1Font";
        src: url(data:font/otf;base64,{font_base64}) format('opentype');
    }}
    
    html, body, div, p, span, h1, h2, h3, h4, h5, h6, section, [class^="css"] {{
        font-family: "F1Font", sans-serif !important;
    }}

    .stApp {{
        background-color: #15151e;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("Visualización Formula 1")
st.subheader("")

tab1, tab2 = st.tabs(["Analisis de Temporadas", "Datos de Pilotos"])
with tab1:
    circuitsView(races)
with tab2:
    driversView(races)
