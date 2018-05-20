import numpy as np

import pandas as panda

# ML Algo
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

#get the training and test data from file
train_df = panda.read_csv("MLTraining.csv")
test_df = panda.read_csv("MLTest.csv")

#Seting up training and test data using G-C Content to predict optimum temperature
X_train = train_df["GC Content (%)"]
X_train = X_train.reshape(len(X_train), 1)
Y_train = train_df["Max Temp (C)"]
Y_train = Y_train.reshape(len(Y_train), 1)

#print len(X_train) == len(Y_train)
X_test = test_df["GC Content (%)"]
X_test = X_test.reshape(len(X_test), 1)
Y_test = test_df["Max Temp (C)"]
Y_test = Y_test.reshape(len(Y_test), 1)

#Training data using LinearRegression
linear = LinearRegression()
linear.fit(X_train, Y_train)
print "accuracy score for linear regression (GCC vs temperature): ", linear.score(X_test, Y_test) #Ans: -0.406938582357

#So genus matters based on the result above.

genus = {"Photorhabdus":1, "Shewanella":2, "Aliivibrio":3, "Photobacterium":4, "Vibrio": 5}

# get all types of genus and convert them to numeric data
train_df["GenusSTR"] = train_df["Organism"].str.split(" ").str[0]
train_df["Genus"] = train_df["GenusSTR"].map(genus)
train_df = train_df.drop(["GenusSTR"], 1)

test_df["GenusSTR"] = test_df["Organism"].str.split(" ").str[0]
test_df["Genus"] = test_df["GenusSTR"].map(genus)
test_df = test_df.drop(["GenusSTR"], 1)

#setting up training and test data using features like G-C content and genus to predict optimum temperature
X_train = train_df.drop(train_df.columns[[0, 1]], 1)
Y_train = train_df["Max Temp (C)"]

X_test = test_df.drop(test_df.columns[[0, 1]], 1)
Y_test = test_df["Max Temp (C)"]

#Training data using RandomForest
random_forest = RandomForestRegressor()
random_forest.fit(X_train, Y_train)

print "accuracy score for Random Forest Regressor (GCC, genus vs temperature): ", random_forest.score(X_test, Y_test)

# FInd out the importance of each feature
importances = panda.DataFrame({'feature':X_train.columns,'importance':np.round(random_forest.feature_importances_,3)})
importances = importances.sort_values('importance',ascending=False).set_index('feature')
print importances.head(15)



