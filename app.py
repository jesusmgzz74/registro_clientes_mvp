import streamlit as st
import pandas as pd
import os

# Archivo CSV donde se guardarán los datos
CSV_FILE = "clientes.csv"

# Inicializar archivo si no existe
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Nombre", "Correo", "Teléfono"])
    df.to_csv(CSV_FILE, index=False)

# Título de la app
st.title("Registro de Clientes")

# Formulario de entrada
with st.form("formulario_cliente"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo electrónico")
    telefono = st.text_input("Teléfono")
    submitted = st.form_submit_button("Guardar")

    if submitted:
        if nombre and correo and telefono:
            nuevo_cliente = pd.DataFrame([[nombre, correo, telefono]], columns=["Nombre", "Correo", "Teléfono"])
            nuevo_cliente.to_csv(CSV_FILE, mode='a', header=False, index=False)
            st.success("✅ Cliente guardado exitosamente.")
        else:
            st.error("❌ Por favor, completa todos los campos.")

# Mostrar registros guardados
st.subheader("📋 Clientes registrados")
df = pd.read_csv(CSV_FILE)
st.dataframe(df)
