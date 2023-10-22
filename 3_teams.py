import streamlit as st
import requests

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
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
df_filtered = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)",
           "Joined", "Height(cm.)", "Weight(lbs.)", "Contract Valid Until",
           "Release Clause(£)"]
# Web scraping cotización dolar/libra esterlina
pedido = requests.get("https://economia.awesomeapi.com.br/last/GBP-USD")
pedido_dic = pedido.json()
gbpusd = pedido_dic["GBPUSD"]["bid"]
valor = float(gbpusd)

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                 "Value(£)": st.column_config.NumberColumn("Value(U$D)", format="U$D %.0f"),
                 "Wage(£)": st.column_config.ProgressColumn("Wage(U$D)", format="U$D %.0f",
                                                            min_value=0, max_value=(df_filtered["Wage(£)"]*valor).max()),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
}, height=2000)
