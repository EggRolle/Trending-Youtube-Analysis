# -*- coding: utf-8 -*-
"""Phase 3 Task 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_fscore_support
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import  datasets
from sklearn.metrics import roc_curve, auc
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('/content/217395609-215222938-215911555—T2Class.csv')
df.drop(df.columns[[0]], axis=1, inplace=True)
#print(df)
#list_of_maps= [{0:0, 1:0, 2:0,3:0,4:0},{0:0, 1:0, 2:0,3:0,4:0}]
"""
df["label"] = df["label"].replace(0,1)
df["label"] = df["label"].replace(1,0)
df["label"] = df["label"].replace(2,0)
df["label"] = df["label"].replace(3,0)
df["label"] = df["label"].replace(4,0)

print(df)
"""
train, test = train_test_split(df, test_size=0.1, random_state=0)
feature_cols = ['likes', 'comment_count']
x_train = train.loc[:, feature_cols]
y_train = train.label

x_test = test.loc[:, feature_cols]
y_test = test.label

tree = DecisionTreeClassifier()
gnb  = GaussianNB()
kf = KFold(n_splits=3)
results_gnb = []
results_tree =[]
for train_index, test_index in kf.split(x_train):
  train_x= x_train.iloc[train_index]
  train_y= y_train.iloc[train_index]

  test_x= x_train.iloc[test_index]
  test_y= y_train.iloc[test_index]

  pred_y=gnb.fit(train_x, train_y).predict(test_x)
  results_gnb.append(precision_recall_fscore_support(test_y, pred_y, average='macro'))

  pred_y=tree.fit(train_x, train_y).predict(test_x)
  results_tree.append(precision_recall_fscore_support(test_y, pred_y, average='macro'))
  #print(train)
  #print(train_index)
  #print(test_index)
for i in range(3):
  print('naive_bayes : precision = {0} , recall = {1} , fbeta_score = {2}'.format(results_gnb[i][0],results_gnb[i][1],results_gnb[i][2]))
  print('Rule Based : precision = {0} , recall = {1} , fbeta_score = {2} \n'.format(results_tree[i][0],results_tree[i][1],results_tree[i][2]))

fpr = dict()
tpr = dict()
roc_auc = dict()

fpr1 = dict()
tpr1 = dict()
roc_auc1 = dict()
for i in range(5):
  new_value = {}
  df_temp = df
  for j in range(5):
    if i == j:
      new_value[j]= 0
    else:
      new_value[j]= 1
  tree = DecisionTreeClassifier()
  gnb  = GaussianNB()
  df_temp["label"] = df["label"].replace(new_value)
  train, test = train_test_split(df, test_size=0.1, random_state=0)

  feature_cols = ['likes', 'comment_count']
  x_train = train.loc[:, feature_cols]
  y_train = train.label
  x_test = test.loc[:, feature_cols]
  y_test = test.label
  pred_y_gne=gnb.fit(x_train, y_train).predict(x_test)
  pred_y_tree=tree.fit(x_train, y_train).predict(x_test)
  
  fpr[i], tpr[i], _ = roc_curve(pred_y_gne, y_test)
  roc_auc[i] = auc(fpr[i], tpr[i])

  fpr1[i], tpr1[i], _ = roc_curve(pred_y_tree, y_test)
  roc_auc1[i] = auc(fpr1[i], tpr1[i])

# Compute micro-average ROC curve and ROC area
#fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), tesy_y_pred.ravel())
#roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
n_classes = 2
plt.figure()
lw = 2
colors = cycle(["aqua", "darkorange", "cornflowerblue","blue","red"])
for i, color in zip(range(n_classes), colors):
    plt.plot(
        fpr[i],
        tpr[i],
        color=color,
        lw=lw,
        label="ROC curve of class {0} (area = {1:0.2f})".format(i, roc_auc[i]),
    )
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Naive_bayes Classifier")
plt.legend(loc="lower right")
plt.show()

n_classes = 2
plt.figure()
lw = 2
colors = cycle(["aqua", "darkorange", "cornflowerblue","blue","red"])
for i, color in zip(range(n_classes), colors):
    plt.plot(
        fpr1[i],
        tpr1[i],
        color=color,
        lw=lw,
        label="ROC curve of class {0} (area = {1:0.2f})".format(i, roc_auc1[i]),
    )
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Rule-Based Classifier")
plt.legend(loc="lower right")
plt.show()

"""
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total %d points : %d"
#       % (X_test.shape[0], (y_test != y_pred).sum()))
"""