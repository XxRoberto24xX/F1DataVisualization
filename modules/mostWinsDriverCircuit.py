import streamlit as st
import pandas as pd
import altair as alt

def mostWinsDriverCircuit(races, circuit_name):
    
    all_circuit_races = races[races['circuitName'] == circuit_name]

    # Datos de los pilotos
    all_circuit_races['position'] = pd.to_numeric(all_circuit_races['position'], errors='coerce')
    winners = all_circuit_races[all_circuit_races['position'] == 1]
    drivers_wins = winners.groupby('driverId').size().reset_index(name='wins')

    total_wins_of_all_drivers = drivers_wins['wins'].sum()
    drivers_wins['percentage'] = drivers_wins['wins'] / total_wins_of_all_drivers
    drivers_wins = drivers_wins.merge(races, on='driverId', how='left').drop_duplicates('driverId')

    pie_drivers_wins = alt.Chart(drivers_wins).mark_arc().encode(
        theta=alt.Theta(field="wins", type="quantitative", stack=True),
        color=alt.Color(field="surname", type="nominal", legend=None),
        order=alt.Order(field="wins", sort="descending"),
        tooltip=["forename", "surname", "driverNationality", "wins"]
    ).properties(
        background='#15151e'
    )

    st.write(circuit_name, " - Pilotos con más victorias")
    st.write("")
    st.write("")
    st.altair_chart(pie_drivers_wins, use_container_width=True)