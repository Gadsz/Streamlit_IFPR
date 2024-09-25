import streamlit as st
import pandas as pd

st.title("Apartamento na cidade do Rio de Janeiro")

rioAptos = pd.read_csv("https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv")

# st.dataframe(rioAptos)

bairro = st.multiselect("Escolha um bairro:", rioAptos["bairro"].unique())

st.write(f"Bairro escolhido: {bairro}")

rioAptos_bairro = rioAptos[rioAptos['bairro'].isin(bairro)]

if bairro:

    preco_menor = rioAptos_bairro['preco'].min()
    preco_maior = rioAptos_bairro['preco'].max()

    st.write(preco_menor)
    st.write(preco_maior)

    # st.data_editor(rioAptos_bairro)

    preço = st.slider("Faixa de valor:", preco_menor, preco_maior, (preco_menor, preco_maior))
    st.write(preço)