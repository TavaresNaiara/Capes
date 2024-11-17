import streamlit as st
import requests

st.set_page_config(layout="wide", page_title="Dashboard Interativo")

st.title("Dashboard Centralizado")
query = st.text_input("Digite sua busca")
filters = st.multiselect("Filtros", options=["Data", "Categoria", "Autor"])

if st.button("Buscar"):
    response = requests.post(
        "http://localhost:8000/search",
        json={"user_id": "123", "query": query, "filters": {"selected": filters}},
    )
    results = response.json().get("results", [])
    st.write("Resultados:")
    for result in results:
        st.write(f"- {result}")
