import pandas as pd
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import os
from os.path import isfile, join
from sklearn.svm import SVC
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

directory = "C:\\Users\\Sk7w4tch3r\\Desktop\\Fifth One\\Numerical Linear Algebra\\Project\\NYU Dataset"

# feature patameters

closeness = directory + "\\closeness\\"
degree = directory + "\\degree\\"
cluster = directory + "\\clusteringcoeff\\"
between = directory + "\\betweenness\\"
allFeatures = directory + "\\allfeatures\\"

label = pd.DataFrame()
Phenotypic = pd.read_csv("C:\\Users\\Sk7w4tch3r\\Desktop\\Fifth One\\Numerical Linear Algebra\\Project\\Phenotypic_V1_0b_preprocessed1.csv")

label = Phenotypic[['FILE_ID','DX_GROUP']]
data = pd.DataFrame()
for filename in os.listdir(cluster):
	temp = pd.read_csv(cluster + "\\" + filename)
	file = open(cluster + "\\" + filename, "r")
	temp2 = file.readline()
	temp = temp.transpose()
	temp['FILE_ID'] = filename[0:11]
	data = data.append(temp)
data = pd.merge(data, label, on='FILE_ID', how='inner')



def REPORT(val,pred):
	print ("*****************************************************")
	print ("Classification Report: ")
	print (classification_report(val, pred))

	print ("")
	print ("Accuracy Score: ", accuracy_score(val, pred))
	print ("*****************************************************\n\n")


# def PREDICT(D):


# def TRAIN(D):


X = data.drop(['FILE_ID' , 'DX_GROUP'], axis = 1)
scaler = StandardScaler()
scaler.fit(X)
svm = scaler.transform(X)
# print(X)
pca = PCA(n_components=20)
pca.fit(svm)
svm = pca.transform(svm)
# print(X)
y = data.DX_GROUP
train_x, val_x, train_y, val_y = train_test_split(svm, y, test_size=0.25)
clf = SVC()
clf.fit(train_x,train_y)
pred_y = clf.predict(val_x)
print("SVC")
REPORT(val_y, pred_y)

train_x, val_x, train_y, val_y = train_test_split(X, y, test_size=0.25)
models = []
models.append(("LR",LogisticRegression(solver="lbfgs")))
models.append(("NB",GaussianNB()))
models.append(("RF",RandomForestClassifier()))
# models.append(("SVC",SVC()))
models.append(("Dtree",DecisionTreeClassifier()))
models.append(("KNN",KNeighborsClassifier(4)))
for name,model in models:
# 	kfold = KFold(n_splits=2, random_state=22)
# 	cv_result = cross_val_score(model,X_train,y_train, cv = kfold,scoring = "f1")
# 	print(name, cv_result)
	clf = model
	clf.fit(train_x,train_y)
	pred_y = clf.predict(val_x)
	print(name)
	REPORT(val_y, pred_y)








