import streamlit as st
import requests

st.set_page_config(
    page_title="Players",
    page_icon="🏃",
    layout="wide"
)

df_data = st.session_state["data"]

# Compruebe si la 'key' ya existe en session_state
# Si no esta, inicialízalo.
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

clubes = df_data["Club"].value_counts().index
clubes2 = sorted(clubes)
club = st.sidebar.selectbox("Club", clubes2)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
players2 = sorted(players)
player = st.sidebar.selectbox("Jugador", players2)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")

st.markdown(f"**Club:** {player_stats['Club']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Posición:** {player_stats['Position']}")
col2.markdown(f"**Nacionalidad:** {player_stats['Nationality']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Edad:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

# Web scraping cotización dolar/libra esterlina
pedido = requests.get("https://economia.awesomeapi.com.br/last/GBP-USD")
pedido_dic = pedido.json()
gbpusd = pedido_dic["GBPUSD"]["bid"]
valor = float(gbpusd)

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado",
            value=f"U$D {player_stats['Value(£)']*valor:,.0f}")
col2.metric(label="Remuneración semanal",
            value=f"U$D {player_stats['Wage(£)']*valor:,.0f}")
col3.metric(label="Cláusula de rescisión",
            value=f"U$D {player_stats['Release Clause(£)']*valor:,.0f}")
