import streamlit as st
import pandas as pd

ARCHIVO = "agenda_medica.csv"

st.set_page_config(
    page_title="Agenda Médica Familiar",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Agenda Médica Familiar")

try:

    df = pd.read_csv(
        ARCHIVO,
        header=None
    )

    df.columns = [
        "Paciente",
        "Fecha",
        "Hora",
        "Especialidad",
        "Medico",
        "Lugar",
        "Estado",
        "Observaciones",
        "Dias_Faltantes"
    ]

    st.success(
        f"Citas cargadas: {len(df)}"
    )

    paciente = st.selectbox(
        "Filtrar paciente",
        ["Todos"] + sorted(df["Paciente"].unique().tolist())
    )

    if paciente != "Todos":

        df = df[
            df["Paciente"] == paciente
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

except FileNotFoundError:

    st.error(
        "No existe agenda_medica.csv"
    )