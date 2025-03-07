import streamlit as st
import pandas as pd
from datetime import date

# Nome do arquivo para armazenar as reservas
CSV_FILE = "reservas.csv"

# Função para carregar dados
def load_data():
    try:
        return pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nome", "Data"])

# Função para salvar dados
def save_data(df):
    df.to_csv(CSV_FILE, index=False)

# Carregar dados existentes
df = load_data()

st.title("Reserva de Almoço")

# Formulário para reserva
with st.form("reserva_form"):
    nome = st.text_input("Nome")
    data_reserva = st.date_input("Data da Reserva", min_value=date.today())
    submit = st.form_submit_button("Reservar")

    if submit:
        if nome:
            nova_reserva = pd.DataFrame([[nome, data_reserva]], columns=["Nome", "Data"])
            df = pd.concat([df, nova_reserva], ignore_index=True)
            save_data(df)
            st.success("Reserva realizada com sucesso!")
        else:
            st.error("Por favor, preencha seu nome.")

# Exibir reservas existentes
st.subheader("Reservas Realizadas")
st.dataframe(df)
