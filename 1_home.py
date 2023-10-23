import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/ncq85zgH/background.jpg");
background-size: 180%;
background-position: top left;
background-repeat: repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

if "data" not in st.session_state:
    df_data = pd.read_csv("CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending = False)
    st.session_state["data"] = df_data
    
st.write("# FIFA 2023 OFFICIAL DATASET! ⚽")

# st.sidebar.write("PRUEBA")
st.sidebar.markdown("Pagina realizada por Guillermo Cerato")
st.sidebar.markdown("[Kaggle](https://www.kaggle.com/willycerato)")
st.sidebar.markdown("[Instagram](https://www.instagram.com/willycerato)")

# Alinear boton
columns = st.columns((1, 2, 3, 4))
btn = columns[2].button('Accese a los datos')

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    
st.markdown(
    '''
    El conjunto de datos de jugadores de fútbol de 2017 a 2023 proporciona información 
    completa sobre jugadores de fútbol profesionales. El conjunto de datos contiene una 
    amplia gama de atributos, incluidos datos demográficos de los jugadores, características 
    físicas, estadísticas de juego, detalles de contratos y afiliaciones de clubes. 
    
    Con más de 17.000 registros, este conjunto de datos ofrece un valioso recurso para 
    analistas, investigadores y entusiastas del fútbol interesados en explorar diversos 
    aspectos del mundo del fútbol, ya que permite estudiar atributos de jugadores, 
    métricas de rendimiento, valoración de mercado, análisis de clubes, posicionamiento 
    de jugadores y Desarrollo del jugador a lo largo del tiempo.
    ''')


    
