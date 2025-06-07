import streamlit as st
from modules.driversChampionship import driversChampionship
from modules.constructorsChampionship import constructorChampionship
from modules.circuitsMap import circuitsMap
from modules.mostPointsConstructorCircuit import mostPointsConstructorCircuit
from modules.mostWinsDriverCircuit import mostWinsDriverCircuit
from modules.raceImage import raceImage
from modules.circuitResultsYear import circuitResultsYear
from modules.circuitPointsYear import circuitPointsYear
from modules.lapRecords import lapRecords

def circuitsView(races):
    
    # Aplicamos el primer filtro, seleccion de temporada
    st.write("")
    years = races['year'].unique()
    years.sort()
    years = years[::-1]
    selected_year = st.select_slider("Selecciona una temporada:", years, key="season_selector_circuit")
    st.subheader("Resultados finales de la temporada " + str(selected_year))
    st.write("")

    reaces_of_season = races[races['year'] == selected_year]

    col_bar1, col_bar2 = st.columns(2)
    with col_bar1:
        driversChampionship(reaces_of_season)
    with col_bar2:
        constructorChampionship(reaces_of_season)

    #Aplicamos el segundo filtro, seleccion de la carrera
    st.subheader("Análisis por carrera ")
    circuit_name = st.selectbox("Selecciona un circuito:", reaces_of_season['circuitName'].unique())

    selected_race = reaces_of_season[reaces_of_season['circuitName'] == circuit_name]
    not_selected_races = reaces_of_season[reaces_of_season['circuitName'] != circuit_name].drop_duplicates('circuitName')

    circuitsMap(selected_race, not_selected_races)

    st.subheader("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        mostWinsDriverCircuit(races, circuit_name)
    with col2:
        raceImage(selected_race["circuitUrl"].values[0])
    with col3:
        mostPointsConstructorCircuit(races, circuit_name)

    st.write("")
    circuitResultsYear(selected_race)

    col4, col5 = st.columns(2)

    with col4:
        lapRecords(races, circuit_name)
    with col5:
        circuitPointsYear(selected_race)