#!/usr/bin/env python
# coding: utf-8

# # PRUEBA A/B CASO DE ESTUDIO COOKIE CATS

# En este caso de estudio vamos a analizar cual es la forma más adecuada de poner las puertas en el juego cookie cats. 

# In[1]:


#Import libreries
import pandas as pd
import numpy as np
from datetime import datetime
import re


# Carga de los datos
# Descripción de los datos:
# 
# *UserID: El id del usuario
# 
# *Version: Puerta puede ser en el nivel 30 o 40
# 
# *Sum_gamerounds: Jugadas
# 
# *Retention_1: Si el jugador regresó el dia 1
# 
# *Retention_7: Si el jugador regresó el dia 7

# In[2]:


#Load the data set

df = pd.read_csv(r'C:\Users\52669\Desktop\COKIE CATS\cookie_cats.csv\cookie_cats.csv')
df.head(10)


# In[3]:


description = df.iloc[0].to_dict()
description


# In[4]:


# Información general
df.dtypes


# **Información general de la base de datos**

# In[5]:


## Variables cuantitativas
df.describe()


# In[6]:


# Número de términos únicos por variable
df.nunique()


# In[7]:


#Tipo de informacion en las columnas 
df


# In[8]:


# Game rounds 
print("- Los rounds van  {0} hasta {1}.".format(df.sum_gamerounds.unique().min(), df.sum_gamerounds.unique().max()))


# In[9]:


#Jugadores en la prueba AB 
df["userid"].nunique()


# El nuero de usuarios en esta muestra es 90189 usuarios

# In[10]:


#Version de la puerta por usario en el juego 

df.groupby("version")[["userid"]].nunique()


# **3.- Missing values**

# In[11]:


# Cuantos nulos tenemos 

df.isnull().sum()


# **4.- impieza de datos**

# In[12]:


df.head(5)


# In[13]:


# Se borra la columna USER ID ya que no representa nada para el estudio

df.drop(columns=["userid"], inplace=True)

# Tambien se edita la columna de Version para que nos muestre en lugar de gate_30 A y B segun el caso

df.rename(columns={"version": "group"},inplace=True)
df["group"] = np.where(df.group == "gate_30", "A", "B")
df.loc[:,"group"]=df.group.astype("category")

# Ahora la tabla se ve diferente 
df.head()


# In[14]:


# Información general
df.dtypes


# In[15]:


#Busqueda de datos atipicos
df.sum_gamerounds.sort_values(ascending = False).head()


# Podemos asumir que un solo jugador no pudo jugar 49854 veces, o quiza sí pero de todas formas es un dato muy alejado de los otros datos

# In[25]:


import matplotlib.pyplot as plt

green_diamond = dict(markerfacecolor='g', marker='D')
fig, ax = plt.subplots()
ax.set_title('Boxplot por Rounds jugados')
ax.boxplot(df.sum_gamerounds, flierprops=green_diamond, labels=["Rounds"])


# In[26]:


import matplotlib.pyplot as plt
plt.boxplot(df.sum_gamerounds, vert=False)
plt.title("Detecting outliers using Boxplot")
plt.xlabel('Rounds')


# In[27]:


#Borramos el valor atipico, y damos margen de menos de 5k rounds
df= df[df["sum_gamerounds"] < 5000]


# In[28]:


#Ahora probamos como queda el grafico 
import matplotlib.pyplot as plt
plt.boxplot(df.sum_gamerounds, vert=False)
plt.title("Detecting outliers using Boxplot")
plt.xlabel('Rounds')


# In[29]:


#Volviendo a checar los datos 

df.sum_gamerounds.sort_values(ascending = False).head(5)


# In[30]:


#Cuantas veces han jugado los usuarios 
df.sum_gamerounds.value_counts().head()


# Se puede decir que hay usuarios que solo descargaron el juego pero jamas lo usaron, esto tambien se considera un dato que no es relevante para el estudio ya que jamas jugaron. Para furturas investigaciones queda abierta la pregunta, de las razones por las que 3994 usuarios nunca jugaron.

# In[31]:


df["sum_gamerounds"].describe([0.95,0.99])


# In[34]:


from pathlib import Path  
filepath = Path(r'C:\Users\52669\Desktop\COKIE CATS\outs.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  


# In[ ]:




