import streamlit as st
import altair as alt

def driversChampionship(reaces_of_season):
    
    driver_points_season = reaces_of_season.groupby('driverId')['points'].sum().reset_index()
    driver_points_season = driver_points_season.sort_values('points', ascending=False)
    driver_points_season = driver_points_season.rename(columns={'points': 'totalPoints'})

    driver_points_season = driver_points_season.merge(reaces_of_season, on='driverId', how='left').drop_duplicates('driverId')

    bar_driversChampionship = alt.Chart(driver_points_season).mark_bar(color="#e10600").encode(
        x=alt.X('surname:N', sort='-y', title='Piloto'),
        y=alt.Y('totalPoints:Q', title='Puntos'),
        tooltip=['forename', 'surname', 'totalPoints', 'teamName']
    ).properties(
        background='#15151e'
    )

    st.write("Clasificación final de Contructores " + str(reaces_of_season['year'].iloc[0]))
    st.altair_chart(bar_driversChampionship, use_container_width=True)