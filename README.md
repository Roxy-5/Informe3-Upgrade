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
