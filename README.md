# Segmentación de Clientes con KMeans – Python  
# Customer Segmentation with KMeans – Python

Este proyecto consiste en un análisis de segmentación de clientes utilizando el algoritmo de **KMeans Clustering** implementado en Python. El objetivo principal fue identificar patrones de compra en un conjunto de datos de ventas retail.  
This project is a customer segmentation analysis using the **KMeans Clustering** algorithm implemented in Python. The main goal was to identify purchase patterns in a retail sales dataset.

---

## 📂 Descripción del archivo `analisis.py`  
## 📂 Description of the `analisis.py` file

El script contiene varias secciones, algunas de las cuales están **comentadas** para facilitar su comprensión y reutilización:  
The script includes several sections, some of which are **commented** to make it easier to understand and reuse:

- **Carga y exploración del dataset**  
  (Comentado) Código para imprimir `head()`, `info()`, y `describe()`.  
- **Loading and exploring the dataset**  
  (Commented) Includes code to print `head()`, `info()`, and `describe()`.

- **Preprocesamiento**  
  Conversión de fechas, extracción de año/mes, eliminación de columnas irrelevantes y valores nulos.  
- **Preprocessing**  
  Date conversion, extraction of year/month, and removal of irrelevant columns and missing values.

- **Selección y normalización de variables**  
  Se seleccionan `Quantity`, `Price per Unit`, y `Total Amount`, luego se normalizan con `StandardScaler`.  
- **Feature selection and normalization**  
  Selected variables: `Quantity`, `Price per Unit`, and `Total Amount`, scaled using `StandardScaler`.

- **Aplicación de KMeans**  
  Segmentación en 3 clústeres usando `scikit-learn`.  
- **Applying KMeans**  
  Segmentation into 3 clusters using `scikit-learn`.

- **Visualización**  
  Gráfico de dispersión de clústeres con `matplotlib`.  
- **Visualization**  
  Scatter plot of clusters using `matplotlib`.

---

## 📊 Dataset utilizado  
## 📊 Dataset Used

El dataset se encuentra en Kaggle:  
The dataset is available on Kaggle:  
🔗 [Retail Sales Dataset – Kaggle](https://www.kaggle.com/)  
*(Se requiere una cuenta en Kaggle / Kaggle account required)*

---

## 🎯 Objetivos de la segmentación  
## 🎯 Segmentation Objectives

- Identificar tipos de clientes según volumen y valor de compra.  
- Identify customer types based on purchase volume and value.

- Detectar patrones útiles para marketing y fidelización.  
- Detect useful patterns for marketing and customer loyalty.

- Explorar cómo variables económicas definen perfiles de comportamiento.  
- Explore how economic variables define customer behavior profiles.

---

## 🛠 Tecnologías utilizadas  
## 🛠 Technologies Used

- Python 3  
- Pandas  
- Scikit-learn  
- Matplotlib  

---

## 👤 Autor  
## 👤 Author

Este proyecto fue realizado de forma individual por **Patzi Estibaliz Pérez Moquete**, como parte de la asignatura **Data Mining en R**, para la **Universidad Abierta Para Adultos (UAPA)**.  
This project was completed individually by **Patzi Estibaliz Pérez Moquete** as part of the **Data Mining in R** course at the **Universidad Abierta Para Adultos (UAPA)**.

---

## 🎥 Video explicativo  
## 🎥 Video Explanation

🔗 [Ver el video en YouTube / Watch on YouTube](https://youtu.be/K_S5yZGUbxk?si=IfdPQ4HkDqPwWiD2)
