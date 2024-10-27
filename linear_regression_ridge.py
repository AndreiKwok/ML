import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'Archives', 'kc_house_data.csv')
print(file_path)


df = pd.read_csv(file_path)
pd.set_option('future.no_silent_downcasting', True)
#pd.set_option("display.max_columns",21)#Exibe todas as columns

df = df.drop("id",axis=1).dropna().drop("date",axis=1).drop("zipcode",axis=1).drop("lat",axis=1)
df = df.drop("long",axis=1)

y = df["price"] #Alvo(Terget) 
x = df.drop("price",axis=1) #All data, less column price(Preditora)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=14)#def o result default

model = LinearRegression()
model.fit(x_train,y_train)

response = model.score(x_test, y_test)
print("R2:", response)

model_ridge = Ridge()
model_ridge = Ridge(alpha=1)
model_ridge.fit(x_train,y_train)
response_ridge = model_ridge.score(x_test,y_test)
print("resultado ridge",response_ridge)