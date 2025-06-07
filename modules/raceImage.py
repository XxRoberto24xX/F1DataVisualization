import streamlit as st
import requests
from bs4 import BeautifulSoup

def raceImage(url):
    
    st.write("Trazado del circuito")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Buscar la imagen principal del infobox (normalmente es el trazado)
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                img_tag = infobox.find('img')
                if img_tag:
                    img_url = "https:" + img_tag['src']
                    st.markdown(
                        f"""
                        <style>
                            .responsive-img {{
                                width: 100%;
                                height: auto;
                                display: block;
                                margin-left: auto;
                                margin-right: auto;
                            }}
                            .img-container {{
                                background-color: white;
                                padding: 10px;
                                border-radius: 8px;
                            }}
                        </style>

                        <div class="img-container">
                            <img src="{img_url}" alt="Trazdo del circuito" class="responsive-img">
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("No se encontró imagen en la página de Wikipedia.")
            else:
                st.warning("No se encontró infobox en la página de Wikipedia.")
        else:
            st.error(f"No se pudo acceder a Wikipedia (código {response.status_code}).")
    except Exception as e:
        st.error(f"Error al cargar la imagen: {e}")