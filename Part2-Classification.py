# -*- coding: utf-8 -*-
"""Project Part 2 - Task 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
   
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np
# READ THE DATA 
df = pd.read_csv("/content/100131001-100131002T5Data.csv", index_col=0)
#corr_matrix = df.corr().abs()
#print(corr_matrix)
# Remove the category column
df = df.drop('category_id', 1)

# Remove all duplicates
df = df.drop_duplicates()
# Scale your data using MinMax
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Now, we need to find the ideal number of clusters. The assignmnet suggest three and it seems a good option
# Here we use the elbow Method, you can read more about online
Sum_of_squared_distances = []
K = range(1,8)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(df_scaled)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

# Lets label the data 
kmeans = KMeans(n_clusters = 3)
kmeans.fit(df_scaled)
print(kmeans.n_features_in_)
labels = kmeans.predict(df_scaled)
df_scaled = pd.concat([df_scaled, pd.DataFrame(labels,columns=["label"])],axis=1)
df_scaled.to_csv('100131001-100131002—T6Data.csv')

# After labeling the data, we need to create the testing and tranning dataset
y = df_scaled.pop('label')
X = df_scaled
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
# We split the data 80% Trainning and 20% testing
# We use Random ForestClassifier 
clf = tree.DecisionTreeClassifier()
# Now we train the model
clf = clf.fit(X_train, y_train)
# Here we test the model
y_pred = clf.predict(X_test)

# Now we calculate the accuracy
score = accuracy_score(y_test, y_pred)

print("The accuracy score = {0}".format(score))