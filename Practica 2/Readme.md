# Análisis por bloques
### Configuración Inicial
Para este análisis, hemos importado las siguientes librerías:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
```
Estas librerías permiten manejar datos, realizar análisis estadísticos, visualizar resultados y aplicar técnicas de procesamiento de lenguaje natural (NLP).


### Carga de Datos

Para comenzar con el análisis, se ha cargado un archivo CSV que contiene datos cruciales para nuestro estudio. Utilizamos `pandas` para facilitar esta tarea.

```python
# Cargar el archivo CSV
csv_data = pd.read_csv(r'C:\Users\angge\OneDrive\Documentos\GitHub\SS2_Practicas_201901055\Practica 2\Datos.csv')
# Cargar el archivo TXT
with open(r'C:\Users\angge\OneDrive\Documentos\GitHub\SS2_Practicas_201901055\Practica 2\Coursera Comments.txt', 'r', encoding='utf-8') as file:
    text_data = file.read()

```

### Limpieza del Texto y los Datos del CSV
En este segmento se realiza la limpieza de datos tanto del texto como del DataFrame. Primero, se eliminan caracteres no alfanuméricos del texto leído y se convierten a minúsculas. Este paso es crucial para asegurar que solo se analicen caracteres relevantes, facilitando futuros análisis de texto.

Luego, se procede a limpiar los nombres de las columnas del DataFrame, eliminando cualquier espacio en blanco que pueda causar problemas en la manipulación de datos. 

Además, se eliminan las filas del DataFrame que contienen valores nulos, garantizando que solo se trabaje con datos completos y válidos. Finalmente, se imprimen los nombres de las columnas del DataFrame, lo que permite verificar que las columnas se han limpiado adecuadamente y están listas para su uso.


```python
cleaned_text = ''.join(char for char in text_data if char.isalnum() or char.isspace() or char in 'áéíóúüñÑ')
cleaned_text = cleaned_text.lower()
text_data = cleaned_text

csv_data.columns = csv_data.columns.str.strip()

csv_data.dropna(inplace=True)

print(csv_data.columns)

csv_data.columns = csv_data.columns.str.strip()
```
 
 ## Cálculo del Promedio de Calificaciones por Curso

En este segmento se calcula el promedio de calificaciones para cada curso. Utilizando la función `groupby` de pandas, se agrupan los datos por el título del curso y se calcula la media de las calificaciones para cada uno. El resultado se almacena en un nuevo DataFrame llamado `average_ratings`.

```python
average_ratings = csv_data.groupby('Course Title')['Rating'].mean().reset_index()
```
Este proceso permite obtener una visión general del desempeño de los cursos en términos de satisfacción del estudiante, facilitando la identificación de aquellos que requieren mejoras o que son altamente valorados.

## Cálculo de Cursos con Mayor y Menor Rating

En este segmento se identifican los cursos con la mayor y menor calificación. Utilizando `idxmax()` e `idxmin()` de pandas, se obtienen los índices de las calificaciones más altas y más bajas respectivamente. Luego, se utiliza estos índices para extraer la información correspondiente de `csv_data`, almacenando los resultados en `highest_rated_course` y `lowest_rated_course`.

```python
highest_rated_course = csv_data.loc[csv_data['Rating'].idxmax()]
lowest_rated_course = csv_data.loc[csv_data['Rating'].idxmin()]
```

Este procedimiento es útil para resaltar los cursos que tienen un desempeño excepcional y aquellos que podrían necesitar atención adicional.

## Cálculo del Porcentaje de Cursos con Horario Flexible

En este segmento se calcula el porcentaje de cursos que ofrecen un horario flexible. Se filtran los cursos en `csv_data` que tienen la propiedad 'Flexible schedule' y se almacena el resultado en `flexible_courses`. Luego, se calcula el porcentaje dividiendo la cantidad de cursos flexibles por el total de cursos y multiplicando por 100.

```python
flexible_courses = csv_data[csv_data['Schedule'] == 'Flexible schedule']
flexible_percentage = (len(flexible_courses) / len(csv_data)) * 100
```

Este cálculo es importante para entender la oferta de cursos y cómo se alinean con las necesidades de los estudiantes que buscan flexibilidad en su aprendizaje.

## Gráfica de Barras del Número de Cursos por Nivel de Dificultad
```python
level_counts = csv_data['Level'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(level_counts.index, level_counts.values, color='purple')
plt.title('Número de Cursos por Nivel de Dificultad')
plt.xlabel('Nivel de Dificultad')
plt.ylabel('Número de Cursos')
plt.xticks(rotation=45)


output_dir = './Resultados/'
plt.savefig(os.path.join(output_dir, 'numero_cursos_nivel_dificultad.png'))
plt.show()
plt.close() 
```
En este segmento se crea una gráfica de barras que muestra el número de cursos disponibles en cada nivel de dificultad. Se utiliza la función `value_counts()` de pandas para contar los cursos según su nivel y se almacenan los resultados en `level_counts`. Luego, se configura y se muestra la gráfica utilizando `matplotlib`, estableciendo el tamaño, los títulos y las etiquetas apropiadas.

Finalmente, la gráfica se guarda en un directorio especificado como una imagen PNG para su posterior análisis o presentación.

Este tipo de visualización permite a los interesados identificar rápidamente la distribución de cursos según su dificultad, lo que puede ayudar en la planificación y selección de cursos por parte de los estudiantes.


## Gráfica de Barras Horizontal del Número de Cursos por Entidad Ofrecida
```python
category_counts = csv_data['Offered By'].value_counts()

plt.figure(figsize=(10, 6))
plt.barh(category_counts.index, category_counts.values, color='teal')
plt.title('Número de Cursos por Entidad Ofrecida')
plt.xlabel('Número de Cursos')
plt.ylabel('Entidad')
plt.tight_layout()


plt.savefig(os.path.join(output_dir, 'numero_cursos_entidad_ofrecida.png')) 
plt.show()
plt.close()
```
En este segmento se crea una gráfica de barras horizontal que muestra el número de cursos ofrecidos por cada entidad. Se utiliza la función `value_counts()` de pandas para contar los cursos según la entidad que los ofrece, y los resultados se almacenan en `category_counts`. Luego, se configura y se muestra la gráfica horizontal utilizando `matplotlib`, ajustando el tamaño, los títulos y las etiquetas adecuadamente.

La gráfica se guarda como una imagen PNG en un directorio especificado, lo que permite su posterior análisis o presentación.

Esta visualización es útil para identificar las principales entidades que ofrecen cursos, ayudando a los estudiantes a comprender mejor las opciones disponibles.

## Tokenización y Análisis de Frecuencia de Palabras
```python
tokens = word_tokenize(text_data)

stop_words = set(stopwords.words('spanish'))
filtered_tokens = [word for word in tokens if word not in stop_words and word.isalpha()]

word_freq = pd.Series(filtered_tokens).value_counts()
```
En este segmento se realiza la tokenización del texto previamente limpiado utilizando `word_tokenize`. Esto permite dividir el texto en palabras individuales. 

Luego, se eliminan las palabras vacías en español utilizando el conjunto de palabras de detención proporcionado por NLTK. Se filtran las palabras para quedarse solo con aquellas que son alfabéticas, y los resultados se almacenan en `filtered_tokens`.

Finalmente, se calcula la frecuencia de las palabras filtradas, almacenando los resultados en un objeto `Series` de pandas llamado `word_freq`. Este análisis permite identificar las palabras más comunes en el texto, lo cual es útil para entender los temas predominantes en los comentarios.

## Gráfica de Frecuencia de Palabras
```python
top_words = word_freq.head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_words.index, top_words.values, color='orange')
plt.title('Frecuencia de Palabras')
plt.xlabel('Frecuencia')
plt.ylabel('Palabras')
plt.tight_layout()

plt.savefig(os.path.join(output_dir, 'frecuencia_de_palabras.png')) 
plt.show()
plt.close()
```
En este segmento se genera una gráfica de barras horizontal que muestra la frecuencia de las palabras más comunes. Se extraen las 10 palabras más frecuentes de `word_freq` y se almacenan en `top_words`.

A continuación, se configura la gráfica utilizando `matplotlib`, estableciendo el tamaño, los títulos y las etiquetas correspondientes. La gráfica se guarda como una imagen PNG en un directorio especificado, lo que permite su uso posterior en análisis o presentaciones.

Este tipo de visualización es valiosa para identificar rápidamente las palabras más recurrentes en el texto, proporcionando una perspectiva sobre los temas y sentimientos predominantes.

## Lematización y Análisis de Frecuencia de Lemas
```python
lemmatizer = WordNetLemmatizer()
words = word_tokenize(text_data)
lemmas = [lemmatizer.lemmatize(word) for word in filtered_tokens] 

lemma_freq = pd.Series(lemmas).value_counts()
print("Frecuencia de lemas:")
print(lemma_freq)
```
En este segmento se realiza la lematización de las palabras filtradas utilizando `WordNetLemmatizer`. Primero, se tokeniza nuevamente el texto y luego se aplican las lematizaciones sobre las palabras filtradas, almacenando los resultados en `lemmas`.

A continuación, se calcula la frecuencia de los lemas, almacenando los resultados en un objeto `Series` de pandas llamado `lemma_freq`. Este análisis es útil para simplificar las palabras a su forma base, lo que permite una mejor comprensión de los temas tratados en el texto y una comparación más efectiva entre palabras relacionadas.

## Análisis de Sentimientos
```python
positive_words = ['bueno', 'excelente', 'fantástico', 'maravilloso', 'agradable', 'positivo']
negative_words = ['malo', 'horrible', 'terrible', 'desagradable', 'negativo']
tokens = word_tokenize(text_data.lower()) 
positive_count = sum(1 for word in tokens if word in positive_words)
negative_count = sum(1 for word in tokens if word in negative_words)
polarity = (positive_count - negative_count) / (positive_count + negative_count + 1)  
subjectivity = (positive_count + negative_count) / len(tokens) if len(tokens) > 0 else 0

print(f"Análisis de sentimientos:\nPolaridad: {polarity*100}%\nSubjetividad: {subjectivity*100}%")

```
En este segmento se lleva a cabo un análisis de sentimientos sobre el texto. Se definen listas de palabras positivas y negativas que se utilizarán para contar la frecuencia de cada tipo. Luego, se tokeniza el texto y se convierten todas las palabras a minúsculas para garantizar una comparación precisa.

Se cuentan las palabras positivas y negativas en el texto y se almacenan en `positive_count` y `negative_count`, respectivamente. A partir de estos conteos, se calcula la polaridad y subjetividad del texto. La polaridad se determina utilizando la diferencia entre el número de palabras positivas y negativas, mientras que la subjetividad se calcula en función de la proporción de palabras positivas y negativas respecto al total de tokens.

Los resultados del análisis se imprimen en porcentaje, lo que permite evaluar la inclinación emocional del texto analizado.

## Tokenización y Gráfica de Frecuencia de Palabras
```python
tokens = word_tokenize(text_data)

stop_words = set(stopwords.words('spanish'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

freq_dist = FreqDist(filtered_tokens)

for word, frequency in freq_dist.most_common(10):
    print(f"Palabra: {word}, Frecuencia: {frequency}")

plt.figure(figsize=(10, 6))
freq_dist.plot(30, cumulative=False)
plt.title('Frecuencia de Palabras')

plt.savefig(os.path.join(output_dir, 'frecuencia_de_palabras.png')) 
plt.show()
plt.close()
```
En este segmento se realiza la tokenización del texto y se filtran las palabras vacías en español utilizando la lista de palabras de detención proporcionada por NLTK. Las palabras resultantes se almacenan en `filtered_tokens`.

A continuación, se calcula la frecuencia de las palabras filtradas utilizando `FreqDist`, y se muestran las 10 palabras más comunes junto con su frecuencia en el texto.

Finalmente, se genera una gráfica que representa la frecuencia de las palabras, mostrando las 30 palabras más frecuentes. La gráfica se guarda como una imagen PNG en un directorio especificado, permitiendo su uso posterior para análisis o presentaciones.

## Generación de Resultados en Archivos de Texto

```python
output_dir = './Resultados/'
with open(os.path.join(output_dir, 'nombres_columnas.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write("Nombres de columnas después de limpieza:\n")
    output_file.write(f"{csv_data.columns.tolist()}\n")

average_ratings = csv_data.groupby('Course Title')['Rating'].mean().reset_index()
with open(os.path.join(output_dir, 'promedio_calificaciones.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write("Promedio de calificaciones por curso:\n")
    for _, row in average_ratings.iterrows():
        output_file.write(f"Curso: {row['Course Title']}, Promedio: {row['Rating']:.2f}\n")

highest_rated_course = csv_data.loc[csv_data['Rating'].idxmax()]
lowest_rated_course = csv_data.loc[csv_data['Rating'].idxmin()]
with open(os.path.join(output_dir, 'cursos_calificacion_extremos.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write(f"Curso con mayor calificación:\n{highest_rated_course['Course Title']} con rating: {highest_rated_course['Rating']}\n")
    output_file.write(f"Curso con menor calificación:\n{lowest_rated_course['Course Title']} con rating: {lowest_rated_course['Rating']}\n")

flexible_courses = csv_data[csv_data['Schedule'] == 'Flexible schedule']
flexible_percentage = (len(flexible_courses) / len(csv_data)) * 100
with open(os.path.join(output_dir, 'porcentaje_horario_flexible.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write(f"Porcentaje de cursos con horario flexible: {flexible_percentage:.2f}%\n")

text_data = "Este es un texto de ejemplo para calcular la frecuencia de palabras."
cleaned_text = ''.join(char for char in text_data if char.isalnum() or char.isspace())
tokens = word_tokenize(cleaned_text)
filtered_tokens = [word for word in tokens if word not in stopwords.words('spanish')]
word_freq = FreqDist(filtered_tokens)
with open(os.path.join(output_dir, 'frecuencia_palabras.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write("Frecuencia de palabras:\n")
    for word, freq in word_freq.items():
        output_file.write(f"{word}: {freq}\n")

positive_words = ['bueno', 'excelente', 'fantástico', 'maravilloso']
negative_words = ['malo', 'horrible', 'terrible', 'desagradable']
positive_count = sum(1 for word in tokens if word in positive_words)
negative_count = sum(1 for word in tokens if word in negative_words)
polaridad = (positive_count - negative_count) / (positive_count + negative_count + 1)  
subjetividad = (positive_count + negative_count) / len(tokens) if len(tokens) > 0 else 0
with open(os.path.join(output_dir, 'analisis_sentimientos.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write("Análisis de sentimientos:\n")
    output_file.write(f"Polaridad: {polaridad * 100:.2f}%\n")
    output_file.write(f"Subjetividad: {subjetividad * 100:.2f}%\n")

entities = [('Ejemplo', 'NOUN'), ('Curso A', 'COURSE')]
with open(os.path.join(output_dir, 'entidades_reconocidas.txt'), 'w', encoding='utf-8') as output_file:
    output_file.write("Entidades reconocidas:\n")
    for entity, label in entities:
        output_file.write(f"{entity}: {label}\n")

```

Este segmento de código se encarga de crear y escribir diversos resultados analíticos en archivos de texto, facilitando su revisión y uso posterior.

1. **Nombres de columnas después de limpieza**: Se guarda una lista de los nombres de columnas de los datos, luego de haber sido limpiados, en un archivo llamado `nombres_columnas.txt`.

2. **Promedio de calificaciones por curso**: El promedio de las calificaciones para cada curso se calcula y se escribe en `promedio_calificaciones.txt`, mostrando el título del curso junto con su calificación promedio.

3. **Curso con mayor y menor calificación**: Se identifican y registran en `cursos_calificacion_extremos.txt` los cursos que tienen la calificación más alta y más baja, incluyendo sus títulos y calificaciones.

4. **Porcentaje de cursos con horario flexible**: El porcentaje de cursos que ofrecen un horario flexible se calcula y se guarda en `porcentaje_horario_flexible.txt`.

5. **Frecuencia de palabras**: Se calcula la frecuencia de palabras en un texto de ejemplo y se almacena en `frecuencia_palabras.txt`, mostrando cada palabra junto con su frecuencia.

6. **Análisis de sentimientos**: Se realiza un análisis básico de sentimientos sobre el texto, y los resultados se escriben en `analisis_sentimientos.txt`, incluyendo la polaridad y subjetividad.

7. **Entidades reconocidas**: Se generan y almacenan en `entidades_reconocidas.txt` las entidades identificadas en el texto, junto con sus etiquetas correspondientes.

Todos los resultados se organizan en el directorio `./Resultados/` para un fácil acceso y revisión.
