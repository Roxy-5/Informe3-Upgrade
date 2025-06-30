![](https://github.com/Roxy-5/Informe1/blob/main/images.jpg)

### 🛸 Informe3

Análisis de datos de la tabla.

### 🌍 Cómo usar

1. Clona este repositorio.
2. Instala las dependencias necesarias.
3. Ejecuta el proyecto.

### 🪐 Autor

Rocío Ramírez

### 🌌 Proceso llevado a cabo para la limpieza y corrección:
- Se cargan los archivos CSV usando `pd.read_csv()` con `on_bad_lines='skip'` para ignorar filas problemáticas.
- Se visualizan las primeras y últimas filas con `df.head()` y `df.tail()`.
- Se revisa la estructura y tipos de datos con `df.info()`, `df.dtypes`, y `df.describe()`.
- Se cuentan filas y columnas (`df.shape`).
- Se buscan duplicados con `df.duplicated().sum()`.
- Se identifican columnas con valores nulos (`df.isna().any()`, `df.isna().sum()`).
- Se identifican columnas completamente nulas y se eliminan si es necesario.
- Se identifican columnas constantes (`nunique() == 1`) y de baja variabilidad (`nunique() < 5`).
- Se eliminan columnas irrelevantes, constantes, completamente nulas o con baja variabilidad.
- Se agrupan y resumen datos para análisis exploratorio y visualización.
- **¿Qué se corrige en este proceso?**:
  - Errores de lectura (filas corruptas).
  - Tipos de datos incorrectos (fechas, precios, categorías).
  - Columnas innecesarias o problemáticas (constantes, nulas, irrelevantes).
  - Valores nulos (relleno o eliminación).
  - Registros no válidos (precios negativos o cero).
  - Duplicados.
  - Preparación para análisis (columnas nuevas, agrupaciones).
 
### 🚀 ¡Enhorabuena por conocer tu personalidad, no todos se atreven!
No te preocupes si eres de un tipo u otro, aquí abajo te dejamos algunos consejos.
### ❄️ Si eres introvertido:
- Respeta tu necesidad de espacio: Los momentos a solas ayudan a procesar emociones, ideas y descansar de la sobreestimulación.
- Exprésate a tu ritmo: Escribir, crear o comunicarte en grupos pequeños.
- Sal de tu zona segura, poco a poco: Asistir a talleres, clubes o grupos con intereses afines.
- Observa cuándo la soledad se transforma en aislamiento: Si evitas vínculos importantes o te genera malestar persistente, es momento de buscar apoyo.

### 🔥 Ahora, si eres extrovertido:
- Recuerda que no todo se construye hacia afuera: La introspección es una herramienta que equilibra la energía con dirección.
- Aprende a leer el ritmo de los demás: Dar espacio y escuchar activamente fortalece tus relaciones.
- Practica estar contigo sin estímulos: El silencio no es tu enemigo.
- Cuida no usar la actividad para evitar emociones: Hacer pausas no te resta vitalidad, te la devuelve.
### ✨ Tanto si encuentras calma en tu mundo interior como si te recargas en la energía de los demás, recuerda que tu forma de ser no necesita corregirse, sino comprenderse y cuidarse.
