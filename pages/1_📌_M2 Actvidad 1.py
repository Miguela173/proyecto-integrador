import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import openpyxl

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

# DataFrame desde Diccionario
st.subheader("DataFrame de Libros")
diccionario = {
    "título": ["Cien Años de Soledad", "El Principito", "1984", "Fahrenheit 451"],
    "autor": ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell", "Ray Bradbury"],
    "año de publicación": [1967, 1943, 1949, 1953],
    "género": ["Realismo Mágico", "Ficción", "Distopía", "Distopía"]
}
df_libros = pd.DataFrame(diccionario)
st.dataframe(df_libros)

# DataFrame desde Lista de Diccionarios
st.subheader("Información de Ciudades")
ciudades = [
    {"nombre": "Bogotá", "población": 7743955, "país": "Colombia"},
    {"nombre": "Ciudad de México", "población": 9209944, "país": "México"},
    {"nombre": "Lima", "población": 9688000, "país": "Perú"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# DataFrame desde Lista de Listas
st.subheader("Productos en Inventario")
productos = [
    ["Laptop", 1200, 50],
    ["Teléfono", 800, 200],
    ["Teclado", 50, 150]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

# DataFrame desde Series
st.subheader("Datos de Personas")
nombres = pd.Series(["Ana", "Luis", "María", "Pedro"])
edades = pd.Series([25, 30, 22, 28])
ciudades = pd.Series(["Bogotá", "Medellín", "Cali", "Barranquilla"])
df_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_personas)

# DataFrame desde CSV
st.subheader("Datos desde CSV")
df_csv = pd.read_csv("data.csv")
st.dataframe(df_csv)

# DataFrame desde Excel
st.subheader("Datos desde Excel")
df_excel = pd.read_excel("data.xlsx")
st.dataframe(df_excel)

# DataFrame desde JSON
st.subheader("Datos de Usuarios desde JSON")
df_json = pd.read_json("data.json")
st.dataframe(df_json)

# DataFrame desde URL
st.subheader("Datos desde URL")
df_url = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
st.dataframe(df_url)

# DataFrame desde SQLite
st.subheader("Datos desde SQLite")
conn = sqlite3.connect('estudiantes.db')
cursor = conn.cursor()
cursor.executemany("INSERT INTO estudiantes VALUES (?, ?)", [("Ana", 90), ("Luis", 85), ("María", 95)])
conn.commit()
df_sqlite = pd.read_sql_query("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)
conn.close()

# DataFrame desde NumPy
st.subheader("Datos desde NumPy")
data = np.random.randint(1, 100, size=(4, 3))
df_numpy = pd.DataFrame(data, columns=["A", "B", "C"])
st.dataframe(df_numpy)
