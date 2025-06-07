import streamlit as st
import altair as alt
from utilities.lapTimeToMilliseconds import lap_time_to_milliseconds

def lapRecords(races, circuit_name):

    races_of_the_circuit = races[races['circuitName'] == circuit_name]

    races_of_the_circuit['fastestLapTime_miliseconds'] = races_of_the_circuit['fastestLapTime'].apply(lap_time_to_milliseconds)
    races_of_the_circuit = races_of_the_circuit.dropna(subset=['fastestLapTime_miliseconds'])

    if not races_of_the_circuit.empty:
        fastest_laps = races_of_the_circuit.loc[
            races_of_the_circuit.groupby(['circuitName', 'year'])['fastestLapTime_miliseconds'].idxmin()
        ]

        fastest_laps = fastest_laps.sort_values('year')

        line = alt.Chart(fastest_laps).mark_line(color="#e10600").encode(
            x=alt.X('year:O', title='Año'),
            y=alt.Y('fastestLapTime_miliseconds:Q', title='Vuelta más rápida (milisegundos)'),
            tooltip=['year', 'fastestLapTime', 'forename', 'surname', 'teamName']
        )
        points = alt.Chart(fastest_laps).mark_point(color="#e10600", size=80).encode(
            x=alt.X('year:O'),
            y=alt.Y('fastestLapTime_miliseconds:Q'),
            tooltip=['year', 'fastestLapTime', 'forename', 'surname', 'teamName']
        )

        lap_time_chart = (line + points).properties(
            background='#15151e'
        )

        st.write("Vueltas más rápidas por año - " + str(fastest_laps['circuitName'].iloc[0]))
        st.altair_chart(lap_time_chart, use_container_width=True)

    else:
        st.warning("No hay datos de vueltas rápidas disponibles para esta carrera posteriores a 2004 (año en que comienza el registro)")