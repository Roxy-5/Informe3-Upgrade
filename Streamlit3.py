import streamlit as st 
import numpy as np 
import joblib 
import pandas as pd
import seaborn as sns

# Configuración de la página
st.set_page_config(
    page_title="Test de Personalidad - Rocío Ramírez y David Zafra",
    page_icon="🧠",
    layout="wide"
)

# Función para cargar datos de personality.csv con caché (adaptado a Streamlit3)
import os

@st.cache_data
def load_personality_data(usecols=None):
    """Cargar datos de Personality.csv con caché para mejor rendimiento"""
    file_path = "Personality.csv"
    if not os.path.exists(file_path):
        file_path = os.path.join(os.path.dirname(__file__), "Personality.csv")
    return pd.read_csv(file_path, usecols=usecols, on_bad_lines='skip')

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"¡Hola, {nombre}!")
st.title("Averigua si eres introvertido o extrovertido con nuestro test:")
st.image("https://raw.githubusercontent.com/Roxy-5/Informe1/main/images.jpg", use_container_width=True)
st.title("Autores")
st.write("Rocío Ramírez y David Zafra")

model_path = os.path.join(os.path.dirname(__file__), "rf_model_personality.pkl")
model = joblib.load(model_path)

with st.expander("Data Frame"):
    df = load_personality_data().head()
    st.dataframe(df)

with st.expander("Graficos Recomendados"):
    st.subheader("Mapa de Correlación")
    corr = df.corr(numeric_only=True)
    st.write("Mapa de correlación de las variables numéricas:")
    st.dataframe(corr)
    import matplotlib.pyplot as plt

    fig_corr, ax_corr = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax_corr)
    st.pyplot(fig_corr)

    st.subheader("Mapa de Cajas por Personality_mapped")
    if "Personality_mapped" in df.columns:
        num_cols = df.select_dtypes(include=np.number).columns.drop("Personality_mapped", errors="ignore")
        for col in num_cols:
            fig_box, ax_box = plt.subplots()
            sns.boxplot(x="Personality_mapped", y=col, data=df, ax=ax_box)
            ax_box.set_title(f"Boxplot de {col} por Personality_mapped")
            st.pyplot(fig_box)
    else:
        st.warning("La columna 'Personality_mapped' no está en el DataFrame.")

    st.subheader("Distribución de la variable Personality_mapped")
    if "Personality_mapped" in df.columns:
        fig_dist, ax_dist = plt.subplots()
        sns.countplot(x="Personality_mapped", data=df, ax=ax_dist)
        ax_dist.set_title("Distribución de Personality_mapped")
        st.pyplot(fig_dist)
    else:
        st.warning("La columna 'Personality_mapped' no está en el DataFrame.")

with st.expander("Predicción de Personality"):

    st.title("Personality Prediction App")

    st.divider()

    st.write("Con esta aplicación lo que queremos es que en base a unos parametros podamos predecir si la persona es Extrovertida o introvertida")

    st.divider()

    time_spent_alone_number = st.number_input("Time Spent Alone", value = 0, step = 1)
    social_event_attendance = st.number_input("Social event attendance", value = 0, step = 1)
    going_outside = st.number_input("Going outside", value = 0, step = 1)
    friends_circle_size = st.number_input("Friends circle size", value = 0, step=1)
    post_frequency = st.number_input("Post frequency",value=0,step=1)

    X = [time_spent_alone_number,social_event_attendance,going_outside,friends_circle_size,post_frequency]

    st.divider()

    prediction = st.button("Personality Estimation Button")

    st.divider
    st.divider()

    if prediction:
        x1 = np.array(X)

        prediction = model.predict([x1])[0]

        personality = prediction
        if personality == 1:
            st.write("La estimación de personalidad para la persona es: Extrovertido")
        else:
            st.write("La estimación de personalidad para la persona es: Introvertido")
    else:
        st.write("Please use the button for getting a prediction")


with st.expander("PowerBI"):
    st.subheader("Dashboard PowerBI")
    st.write("Puedes ver el dashboard interactivo en PowerBI haciendo clic en el botón de abajo:")
    
    # Crear un botón más llamativo con HTML y CSS
    st.markdown("""
    <style>
    .powerbi-button {
        display: inline-block;
        background-color: #F2C811;
        color: #323130;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        margin: 10px 0;
        border: 2px solid #F2C811;
        transition: all 0.3s ease;
    }
    .powerbi-button:hover {
        background-color: #323130;
        color: #F2C811;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(
        '<a href="https://app.powerbi.com/groups/me/reports/811f953e-6115-4b12-a994-544b5bf7e49d/e65c08d5ea181cb9504e?experience=power-bi" class="powerbi-button" target="_blank">🚀 Ver Dashboard PowerBI</a>',
        unsafe_allow_html=True
    )
st.title("¡Enhorabuena por conocer tu personalidad, no todos se atreven!")
st.write("No te preocupes si eres de un tipo u otro, aquí abajo te dejamos algunos consejos.")
st.subheader("Si eres introvertido:")
st.markdown("""
- Respeta tu necesidad de espacio: Los momentos a solas ayudan a procesar emociones, ideas y descansar de la sobreestimulación.
- Exprésate a tu ritmo: Escribir, crear o comunicarte en grupos pequeños.
- Sal de tu zona segura, poco a poco: Asistir a talleres, clubes o grupos con intereses afines.
- Observa cuándo la soledad se transforma en aislamiento: Si evitas vínculos importantes o te genera malestar persistente, es momento de buscar apoyo.
""")
st.subheader("Ahora, si eres extrovertido:")
st.markdown("""
- Recuerda que no todo se construye hacia afuera: La introspección es una herramienta que equilibra la energía con dirección.
- Aprende a leer el ritmo de los demás: Dar espacio y escuchar activamente fortalece tus relaciones.
- Practica estar contigo sin estímulos: El silencio no es tu enemigo.
- Cuida no usar la actividad para evitar emociones: Hacer pausas no te resta vitalidad, te la devuelve. 
""")

st.markdown("""
<h3 style='text-align: center;'>Tanto si encuentras calma en tu mundo interior como si te recargas en la energía de los demás, recuerda que tu forma de ser no necesita corregirse, sino comprenderse y cuidarse.</h3>
""", unsafe_allow_html=True)