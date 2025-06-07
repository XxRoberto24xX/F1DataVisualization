import streamlit as st
import altair as alt

def mostPointsConstructorCircuit(races, circuit_name):
    
    all_circuit_races = races[races['circuitName'] == circuit_name]

    # Datos de los pilotos
    constructors_points = all_circuit_races.groupby('teamName')['points'].sum().reset_index(name='total_points')
    constructors_points = constructors_points.merge(races, on='teamName', how='left').drop_duplicates('teamName')

    total_points_of_all_constructors = constructors_points['total_points'].sum()
    constructors_points['percentage'] = constructors_points['total_points'] / total_points_of_all_constructors

    # Create the pie chart for constructors by points
    pie_constructors_points = alt.Chart(constructors_points).mark_arc().encode(
        theta=alt.Theta(field="total_points", type="quantitative", stack=True),
        color=alt.Color(field="teamName", type="nominal", legend=None),
        order=alt.Order(field="total_points", sort="descending"),
        tooltip=["teamName", "teamNationality", "total_points", alt.Tooltip("percentage", format=".1%")]
    ).properties(
        background='#15151e',
    )

    st.write(circuit_name + " - Equipos con más puntos")
    st.write("")
    st.write("")
    st.altair_chart(pie_constructors_points, use_container_width=True)
    