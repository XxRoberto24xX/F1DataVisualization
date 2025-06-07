import streamlit as st
import pandas as pd
import altair as alt

def circuitResultsYear(selected_race):

    selected_race['position'] = pd.to_numeric(selected_race['position'], errors='coerce')
    selected_race['grid'] = pd.to_numeric(selected_race['grid'], errors='coerce')

    order_option = st.radio(
        "Ordenar pilotos por:",
        ("Posición final", "Parrilla de salida"),
        key="order_selector"
    )

    if order_option == "Posición final":
        surname_order = selected_race.sort_values('position', na_position='last')['surname'].tolist()
    else:
        surname_order = selected_race.sort_values('grid', na_position='last')['surname'].tolist()

    melted = pd.melt(
        selected_race,
        id_vars=['surname', 'teamName'],
        value_vars=['grid', 'position'],
        var_name='Tipo',
        value_name='Posición'
    )

    circuit_results_chart = alt.Chart(melted).mark_line(point=True).encode(
        x=alt.X('surname:N', sort=surname_order, title='Piloto'),
        y=alt.Y('Posición:Q', sort='ascending', title='Posición'),
        color=alt.Color('Tipo:N', title='Tipo de posición', scale=alt.Scale(domain=['grid', 'position'], range=['steelblue', "#e10600"])),
        tooltip=['surname', 'teamName', 'Tipo', 'Posición']
    ).properties(
        background='#15151e'
    )

    st.write("Resultados de carrera - " + str(selected_race['circuitName'].iloc[0]) + " " + str(selected_race['year'].iloc[0]))
    st.altair_chart(circuit_results_chart, use_container_width=True)
