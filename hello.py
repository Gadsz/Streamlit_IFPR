import streamlit as st

st.title("CD/TEC")
st.write ("Lista melhor que Letterboxd")

genero = {
    "Rock": ["Kiss", "Linkin Park"],
    "Metal": ["Metallica", "Massacration"],
            }

genero_escolhido = st.selectbox("Genero musical", genero.keys())

banda_prediletas = st.selectbox("Banda preferida", genero[genero_escolhido])

