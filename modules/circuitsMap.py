import streamlit as st
import pydeck as pdk

def circuitsMap(selected_race, not_selected_races):

    selected_race = selected_race.drop_duplicates('circuitName')

    # Capa para todos los circuitos (en rojo)
    layer_otros = pdk.Layer(
        "ScatterplotLayer",
        not_selected_races,
        get_position=['lng', 'lat'],
        get_color=[225, 6, 0, 200],  # rojo
        radiusScale=10,
        get_radius=2000,
        pickable=True,
        opacity=0.8
    )

    # Capa para el circuito seleccionado (en azul)
    layer_seleccionado = pdk.Layer(
        "ScatterplotLayer",
        selected_race,
        get_position=['lng', 'lat'],
        get_color=[0, 0, 255, 200],  # azul
        radiusScale=10,
        get_radius=4000,  # un poco más grande para destacarlo
        pickable=True,
        opacity=0.9
    )

    # Vista del mapa
    view_state = pdk.ViewState(
        latitude=selected_race['lat'].values[0],
        longitude=selected_race['lng'].values[0],
        zoom=4,
        pitch=0
    )

    # Mapa combinado
    mapa_circuitos = pdk.Deck(
        layers=[layer_otros, layer_seleccionado],
        initial_view_state=view_state,
        tooltip={"html": "<b>Nombre:</b> {circuitName}<br><b>Ubicación:</b> {location}<br><b>País:</b> {country}"}
    )

    st.pydeck_chart(mapa_circuitos, use_container_width=True)