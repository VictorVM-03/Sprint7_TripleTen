import pandas as pd
import plotly.express as px
import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Dashboard de Anuncios de Coches", layout="wide")

# --- Encabezado de la aplicación ---
st.header('Análisis de Anuncios de Venta de Coches')
st.write('¡Bienvenido al dashboard interactivo para explorar los datos de anuncios de coches!')

# --- Carga el dataset ---
# Asegúrate de que 'vehicles_us.csv' esté en el mismo directorio que app.py
car_data = pd.read_csv('vehicles_us.csv')

# --- Casillas de verificación para visualizaciones ---
st.write('---')  # Separador visual
st.subheader('Selecciona las visualizaciones que deseas ver:')

# Casilla de verificación para Histograma
build_histogram = st.checkbox('Construir Histograma de Odómetro')

if build_histogram:  # Si la casilla de verificación del histograma está seleccionada
    # Escribir un mensaje
    st.write('Creando un histograma para la distribución del odómetro de los coches.')

    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Distribución del Odómetro")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para Gráfico de Dispersión
build_scatter = st.checkbox(
    'Construir Gráfico de Dispersión de Precio vs. Odómetro')

if build_scatter:  # Si la casilla de verificación del gráfico de dispersión está seleccionada
    # Escribir un mensaje
    st.write(
        'Creando un gráfico de dispersión para la relación entre el precio y el odómetro.')

    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Precio vs. Odómetro",
                             hover_data=['model', 'model_year', 'condition'])

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- Pie de página (opcional) ---
st.write('---')
st.markdown("Dashboard creado con Streamlit y Plotly Express.")
