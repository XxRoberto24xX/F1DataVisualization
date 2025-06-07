import streamlit as st
import altair as alt

def driverTeams(selected_driver):
    seasons_per_team = selected_driver.groupby('teamName')['year'].nunique().reset_index()
    seasons_per_team = seasons_per_team.rename(columns={'year': 'seasons'})

    teams_piechart = alt.Chart(seasons_per_team).mark_arc().encode(
        theta=alt.Theta(field="seasons", type="quantitative"),
        color=alt.Color(field="teamName", type="nominal", legend=None),
        order=alt.Order(field="seasons", sort="descending"),
        tooltip=["teamName", "seasons"]
    ).properties(
        background='#15151e'
    )

    st.write("Escuderías en las que ha pilotado")
    st.altair_chart(teams_piechart, use_container_width=True)