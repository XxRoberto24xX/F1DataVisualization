import streamlit as st
import pandas as pd
import altair as alt

def driverResultsYear(races_of_season):
    races_of_season['position'] = pd.to_numeric(races_of_season['position'], errors='coerce')
    races_of_season['grid'] = pd.to_numeric(races_of_season['grid'], errors='coerce')

    circuit_order = races_of_season['circuitName'].tolist()

    melted = pd.melt(
        races_of_season,
        id_vars=['circuitName', 'teamName'],
        value_vars=['grid', 'position'],
        var_name='Tipo',
        value_name='Posición'
    )

    chart = alt.Chart(melted).mark_line(point=True).encode(
        x=alt.X('circuitName:N', title='Carrera', sort=circuit_order),
        y=alt.Y('Posición:Q', title='Posición'),
        color=alt.Color('Tipo:N', title='Tipo de posición', scale=alt.Scale(domain=['grid', 'position'], range=['steelblue', "#e10600"])),
        tooltip=['Tipo', 'Posición', 'teamName']
    ).properties(
        background='#15151e'
    )

    st.write("Posición de salida y final en cada circuito a lo largo de la temporada " + str(races_of_season['year'].iloc[0]))
    st.altair_chart(chart, use_container_width=True)