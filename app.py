import streamlit as st
from PIL import Image
import pandas as pd

# Título y descripción
st.set_page_config(page_title="Explorador Brutalista", layout="wide")
st.title("Explorador de Arquitectura Brutalista 🇬🇧🧱")
st.markdown(
    "En este microblog puedes descubrir edificios emblemáticos del movimiento brutalista, dejar tus notas y calificar lo que más te llama la atención. Ideal para estudiantes y curiosos de la arquitectura.")

# Sidebar: selección y filtros
with st.sidebar:
    st.header("Buscar edificio")
    edificio = st.selectbox("Selecciona un edificio:",
                            ("Unidad Habitacional de Marsella", "Biblioteca Nacional de Buenos Aires", "Barbican Centre", "Torre de Concreto (ejemplo)")
                            )
    mostrar_filtros = st.checkbox("Mostrar filtros avanzados")
    if mostrar_filtros:
        año = st.slider("Año de construcción aproximado", 1900, 2030, 1970)
        tipo = st.radio("Tipo:", ("Residencial", "Cultural", "Mixto", "Oficinas"))

# Imagen y breve ficha técnica
st.subheader(edificio)
col1, col2 = st.columns([1, 2])
with col1:
    # intenta abrir una imagen local con nombre basado en la selección, si no existe muestra un marcador
    try:
        img = Image.open(edificio.replace(" ", "_") + ".jpg")
        st.image(img, caption=edificio, use_column_width=True)
    except Exception:
        st.image("https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg", caption="Imagen no disponible", width=250)

with col2:
    if edificio == "Unidad Habitacional de Marsella":
        st.write("**Arquitecto:** Le Corbusier")
        st.write("**Ubicación:** Marsella, Francia")
        st.write("**Año:** 1952")
        st.write("**Descripción:** Concreto visto, soluciones de vivienda social y patios interiores. Ejemplo clásico del brutalismo con principios funcionales.")
    elif edificio == "Biblioteca Nacional de Buenos Aires":
        st.write("**Arquitecto:** Clorindo Testa")
        st.write("**Ubicación:** Buenos Aires, Argentina")
        st.write("**Año:** 1992 (inauguración parcial)")
        st.write("**Descripción:** Volumen escultórico, uso expresivo del hormigón y escalas monumentales.")
    elif edificio == "Barbican Centre":
        st.write("**Arquitecto:** Chamberlin, Powell and Bon")
        st.write("**Ubicación:** Londres, Reino Unido")
        st.write("**Año:** 1982")
        st.write("**Descripción:** Complejo cultural y residencial: pasarelas, patios y texturas de concreto.")
    else:
        st.write("Ficha técnica básica disponible. Añade una imagen local con el nombre del edificio para más detalle.")

# Interacción: dejar nota y calificar
st.markdown("---")
st.subheader("Tu valoración")
nota = st.text_input("Deja una nota rápida sobre este edificio:", "Me encanta por...")
calificacion = st.slider("¿Qué calificación le das?", 0, 10, 7)

# Checkbox para mostrar datos interesantes
if st.checkbox("Mostrar datos curiosos"):
    st.info("El término 'brutalismo' no viene de 'brutal' en sentido común, sino de 'béton brut' (hormigón crudo en francés).")

# Dos columnas con aspectos positivos y negativos
c1, c2 = st.columns(2)
with c1:
    st.markdown("**Aspectos que me gustan**")
    favoritos = st.multiselect("Elige elementos:", ["Textura de hormigón", "Volumen escultural", "Patios interiores", "Uso funcional"]) 
with c2:
    st.markdown("**Aspectos que me incomodan**")
    molestias = st.multiselect("Elige molestias:", ["Escala monumental", "Falta de ornamentación", "Clima interior frío", "Mantenimiento costoso"])

# Botón para guardar la entrada en la sesión
if 'entradas' not in st.session_state:
    st.session_state['entradas'] = []

if st.button("Guardar mi valoración"):
    entrada = {
        'edificio': edificio,
        'nota': nota,
        'calificacion': calificacion,
        'favoritos': ", ".join(favoritos),
        'molestias': ", ".join(molestias)
    }
    st.session_state['entradas'].append(entrada)
    st.success("Valoración guardada en la sesión ✔️")

# Mostrar entradas guardadas
st.subheader("Valoraciones guardadas (sesión)")
if st.session_state['entradas']:
    df = pd.DataFrame(st.session_state['entradas'])
    st.dataframe(df)
else:
    st.write("Aún no hay valoraciones guardadas. Guarda la primera para verla aquí.")

