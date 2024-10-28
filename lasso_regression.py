import pandas as pd
from sklearn.linear_model import LinearRegression,Lasso
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(fr"C:\Users\ferna\Dev\Projetos\VsCodeProjects\ML\Archives\kc_house_data.csv")
pd.set_option('future.no_silent_downcasting', True)
#pd.set_option("display.max_columns",21)#Exibe todas as columns

df = df.drop("id",axis=1).dropna(how="any").drop("date",axis=1).drop("zipcode",axis=1).drop("lat",axis=1)
df = df.drop("long",axis=1)

y = df["price"] #Alvo(Terget) 
x = df.drop("price",axis=1) #All data, less column price(Preditora)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=14)#def o result default

model = LinearRegression()
model.fit(x_train,y_train)

response = model.score(x_test, y_test)
print("R2:", response)

model_lasso = Lasso()
model_lasso = Lasso(alpha=1000,max_iter=1000,tol=0.1)#tol= tolerancia
model_lasso.fit(x_train,y_train)
response_lasso = model_lasso.score(x_test,y_test)
print("modelo lasso | regularizaçao L1", response_lasso)
