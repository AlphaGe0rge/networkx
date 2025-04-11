import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dataset base
data = {
    'Estacion': ["Portal Norte", "Calle 187", "Calle 170", "Calle 142", "Heroes", 
                 "Calle 100", "Calle 72", "Av. Jimenez", "Portal Sur", "Venecia", "Restrepo"],
    'Usuarios_por_dia': [1200, 1000, 800, 750, 1500, 1300, 900, 1100, 700, 600, 650],
    'Tiempo_Espera': [4, 3, 5, 4, 2, 3, 6, 4, 5, 7, 6]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Calcular usuarios por hora
df['Usuarios_por_hora'] = df['Usuarios_por_dia'] / 18  # jornada de 5 am a 11 pm (18 horas)

# Selección de columnas para clustering
X = df[['Usuarios_por_dia', 'Tiempo_Espera']]

# Aplicar modelo KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Mostrar resultados
print(df)

# Visualización
plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'blue']
for i in range(3):
    cluster = df[df['Cluster'] == i]
    plt.scatter(cluster['Usuarios_por_dia'], cluster['Tiempo_Espera'], 
                color=colors[i], label=f'Cluster {i}', s=100)

# Etiquetas de estaciones
for idx, row in df.iterrows():
    plt.text(row['Usuarios_por_dia'] + 10, row['Tiempo_Espera'], row['Estacion'], fontsize=9)

plt.xlabel('Usuarios por Día')
plt.ylabel('Tiempo de Espera (minutos)')
plt.title('Clustering de Estaciones de Transmilenio')
plt.legend()
plt.grid(True)
plt.show()
