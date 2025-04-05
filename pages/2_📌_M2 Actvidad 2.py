import pandas as pd
import streamlit as st
import io


# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Solución")


st.title("Explorador de estudiantes - Colombia")

df = pd.read_csv("dataset/estudiantes_colombia.csv")

st.subheader("Vista completa del dataset")
st.dataframe(df)

st.header("Primeras 5 filas del dataframe")
st.write(df.head())

st.header("Ultimas 5 filas del dataframe")
st.write(df.tail())

st.header("Información del dataset")
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.header("Estadisticas del dataset")
st.write(df.describe())

st.header("Seleccionar columnas especificas")
columnas = st.multiselect(
    "Selecciona las columnas que quieres visualizar",
    df.columns.tolist(),
    default=["nombre", "edad", "promedio"] if all(col in df.columns for col in ["nombre", "edad", "promedio"]) else df.columns[:3]
)
st.write(df[columnas])

if "promedio" in df.columns:
    st.header("Filtrar estudiantes con promedio mayor a")
    valor_min, valor_max = float(df["promedio"].min()), float(df["promedio"].max())
    promedio_min = st.slider("Mostrar estudiantes con promedio mayor a:", min_value=valor_min, max_value=valor_max, value=valor_min)
    df_filtrado = df[df["promedio"] > promedio_min]
    st.write(df_filtrado)
else:
    st.warning("La columna 'promedio' no está disponible en el dataset.")







