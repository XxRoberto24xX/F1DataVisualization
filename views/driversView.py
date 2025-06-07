import streamlit as st
from modules.driverTeams import driverTeams
from modules.driverImage import driverImage
from modules.driverResultsYear import driverResultsYear
from modules.driverPointsYear import driverPointsYear

def driversView(races):
    
    #Aplicamos el primer filtro, seleccion del piloto
    races['full_name'] = races['forename'] + ' ' + races['surname']

    # Usar la columna de nombre completo en el selectbox
    driver_names = races[['driverId', 'full_name']].drop_duplicates().sort_values('driverId')['full_name'].values
    selected_driver_name = st.selectbox("Selecciona un piloto:", driver_names, key="driver_selector")

    selected_driver = races[races['full_name'] == selected_driver_name]

    drivers_points = races.groupby(['full_name', 'year'])['points'].sum().reset_index()
    champion_dirvers = drivers_points.loc[drivers_points.groupby('year')['points'].idxmax()]
    selected_driver_championships = champion_dirvers[champion_dirvers['full_name'] == selected_driver_name]

    col1, col2, col3 = st.columns(3)

    with col1:
        driverImage(selected_driver["driverUrl"].values[0])
    with col2:
        st.subheader(" ")
        st.write(f"Nombre: {selected_driver_name}")
        st.write(f"Nacionalidad: {selected_driver['driverNationality'].values[0]}")
        if not selected_driver_championships.empty:
            years_str = ', '.join(str(year) for year in selected_driver_championships['year'].values)
            st.write(f"Mundiales ganados: {years_str}")
        else:
            st.write("No ha ganado ningún mundial.")
    with col3:
        driverTeams(selected_driver)

    #Aplicamos el segundo filtro, seleccion del año
    years = races[races['full_name'] == selected_driver_name]['year'].unique()
    years.sort()
    years = years[::-1]
    selected_year = st.select_slider("Selecciona una temporada:", years, key="season_selector_driver")

    races_of_season = selected_driver[selected_driver['year'] == selected_year]

    driverResultsYear(races_of_season)

    driverPointsYear(races_of_season)

