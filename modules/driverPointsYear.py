import streamlit as st
import pandas as pd
import altair as alt

def driverPointsYear(races_of_season):
    races_of_season['points'] = pd.to_numeric(races_of_season['points'], errors='coerce')

    circuit_order = races_of_season['circuitName'].tolist()

    circuit_points_chart = alt.Chart(races_of_season).mark_bar(color="#e10600").encode(
        x=alt.X('circuitName:N', sort=circuit_order, title='Pilotos'),
        y=alt.Y('points:Q', title='Puntos'),
        tooltip=['circuitName', 'points', 'teamName']
    ).properties(
        background='#15151e'
    )

    st.write("Puntos obtenidos a lo largo de la temporada " + str(races_of_season['year'].iloc[0]))
    st.altair_chart(circuit_points_chart, use_container_width=True)