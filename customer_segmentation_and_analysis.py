# -*- coding: utf-8 -*-
"""customer segmentation and analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MH3FKWF8I2i6FWYHh5-9byndn8VYxWq4
"""

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('/content/OnlineRetail.csv', encoding='latin1')

print(df.head())

print(df.describe())

features = df[['Quantity', 'UnitPrice', 'CustomerID']]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

df.isnull().sum()

plt.xlabel('CustomerID')
plt.ylabel('Quantity')
plt.figure(figsize=(10, 6))
plt.plot( df['Quantity'] , df['CustomerID'])
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantity', y='CustomerID', data=df)
plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)