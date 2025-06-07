import streamlit as st
import requests
from bs4 import BeautifulSoup

def driverImage(url):
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
                            .img-wrapper {{
                                height: 100%;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                background-color: '#15151e';
                                padding: 10px;
                                border-radius: 8px;
                            }}
                            .img-wrapper img {{
                                max-height: 100%;
                                height: auto;
                                max-width: 100%;
                                object-fit: contain;
                            }}
                        </style>

                        <div class="img-wrapper">
                            <img src="{img_url}" alt="Driver image">
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