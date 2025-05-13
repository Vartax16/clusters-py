#Carga, limpieza y transformación del dataset

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

'''print(df.head())

print(df.info())

print(df.describe())


# Eliminar columnas innecesarias
df = df.drop(columns=["ID", "Unnamed: 0"], errors='ignore')

# Convertir fechas
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Verificar valores nulos
print(df.isnull().sum())

# Eliminar o imputar nulos si hay
df = df.dropna()'''

df = pd.read_csv(r'd:\maestria en bd y bi\Data mining con R\tarea1-datamining\retail_sales_dataset.csv')


X = df[['Quantity', 'Price per Unit', 'Total Amount']]

# Escalar los datos para que todas las variables tengan igual peso
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualizar los resultados: Ventas vs. Monto Total
plt.figure(figsize=(10, 6))
plt.scatter(df['Quantity'], df['Total Amount'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.title('Segmentación de clientes por KMeans')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()

