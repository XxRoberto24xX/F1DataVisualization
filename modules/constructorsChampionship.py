import streamlit as st
import altair as alt

def constructorChampionship(reaces_of_season):

    driver_points_season = reaces_of_season.groupby('teamName')['points'].sum().reset_index()
    driver_points_season = driver_points_season.sort_values('points', ascending=False)
    driver_points_season = driver_points_season.rename(columns={'points': 'totalPoints'})

    driver_points_season = driver_points_season.merge(reaces_of_season, on='teamName', how='left').drop_duplicates('teamName')

    bar_constructorChampionship = alt.Chart(driver_points_season).mark_bar(color="#e10600").encode(
        x=alt.X('teamName:N', sort='-y', title='Piloto'),
        y=alt.Y('totalPoints:Q', title='Puntos'),
        tooltip=['teamName', 'totalPoints', 'teamNationality']
    ).properties(
        background='#15151e'
    )

    st.write("Clasificación final de Pilotos - " + str(reaces_of_season['year'].iloc[0]))
    st.altair_chart(bar_constructorChampionship, use_container_width=True)