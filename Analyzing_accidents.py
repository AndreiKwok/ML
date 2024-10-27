import os,sys
import folium.map
import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt # type: ignore








script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'Archives', 'cat_acidentes.csv')
print(file_path)

df = pd.read_csv(str(file_path), sep=";")
df = df.dropna(subset=["latitude", "longitude"], how="any")
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df_year = df["data"].dt.year.value_counts()
df_year = df_year.drop(2202)
# df_year = pd.DataFrame(df_year, columns=["data"])

#MAPA DE CALOR
map = folium.Map(location=[-30.1,-51.15],zoom_start=11)
coord = list(zip(df.latitude, df.longitude))
map_temp = HeatMap(coord,radius=9,blur=10)
map.add_child(map_temp)

#MAPA COM PONTOS 
map = folium.Map(location=[-30.1,-51.15], zoom_start=11)
map_cluster = MarkerCluster(coord)  #fun MarkCluster gera pontos com a quantidade de acidentes 
map.add_child(map_cluster)

#GRAFICO COM BARRAS
info = df_year / float(df_year.max())
print("info",info)
color = plt.cm.Blues(info)
plt.bar(df_year.index,df_year.values,color= color) #Cria um grafico de barras x sendo os anos e y a quantidade de acidentes
plt.show()