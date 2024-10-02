import streamlit as st
import pandas as pd

st.title("Charts regionais do Spotify Brasil")

spotify_chart = pd.read_csv("archive/tracks_info-update.csv")

st.dataframe(spotify_chart)

artista = st.multiselect("Escolha um artista:", spotify_chart["artist_names"].unique())

st.write(f"Bora ver seu gosto musical: {artista}")

spotify_artistas = spotify_chart[spotify_chart['artist_names'].isin(artista)]

st.data_editor(spotify_artistas)