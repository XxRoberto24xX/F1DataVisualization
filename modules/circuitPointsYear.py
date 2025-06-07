import streamlit as st
import pandas as pd
import altair as alt

def circuitPointsYear(selected_race):
    selected_race['points'] = pd.to_numeric(selected_race['points'], errors='coerce')

    circuit_points_chart = alt.Chart(selected_race).mark_bar(color="#e10600").encode(
        x=alt.X('surname:N', sort='-y', title='Pilotos'),
        y=alt.Y('points:Q', title='Puntos'),
        tooltip=['forename', 'surname', 'points', 'teamName']
    ).properties(
        background='#15151e'
    )

    st.write("Reparto de puntos - " + str(selected_race['circuitName'].values[0]) + " " + str(selected_race['year'].values[0]))
    st.altair_chart(circuit_points_chart, use_container_width=True)