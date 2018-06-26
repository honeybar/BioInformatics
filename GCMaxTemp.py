import numpy as np

import pandas as panda

# ML Algo
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from numpy.polynomial.polynomial import polyfit
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def getGenus(traindata, genus):
    traindata["Genus"] = traindata["GenusSTR"].map(genus)
    traindata = traindata.drop(["GenusSTR"], 1)
    return traindata

def convertTemp(traindata): # convert temperature data into integer and average the range temperature
    traindata["Temp"] = traindata["Temp"].map(lambda x: str(x))
    traindata['Temp'] = traindata["Temp"].map(lambda x: sum(map(int, (str(x).split("-")))) / len(str(x).split("-")))
    return traindata

#get the training and test data from file
train_df = panda.read_csv("Bacteria_list.csv")
test_df = panda.read_csv("Bacteria_test.csv")

# get all types of genus
genus = {}
train_df["GenusSTR"] = train_df["Bacteria"].str.split(" ").str[0]
gencode = 1  # code for mapping each genus to a number for random forest

for index, row in train_df.iterrows():
    if row["GenusSTR"] not in genus:  # find all the available genus in the training data
        genus[row["GenusSTR"]] = gencode
        gencode += 1

train_df = getGenus(train_df, genus) # convert all genus to a numerical data
train_df = convertTemp(train_df) # convert temperature data into integer

test_df["GenusSTR"] = test_df["Bacteria"].str.split(" ").str[0]
test_df = getGenus(test_df, genus)
test_df = convertTemp(test_df)


#setting up training and test data using features like G-C content and genus to predict optimum temperature
X_train = train_df[["Temp", "Genus"]]
Y_train = train_df["GC Content"]

X_test = test_df[["Temp", "Genus"]]
Y_test = test_df["GC Content"]

#Training data using RandomForest
random_forest = RandomForestRegressor()
random_forest.fit(X_train, Y_train)
print "accuracy score for Random Forest Regressor (temperature, genus vs GC content): ", random_forest.score(X_test, Y_test)

# Find out the importance of each feature
importances = panda.DataFrame({'feature':X_train.columns,'importance':np.round(random_forest.feature_importances_,3)})
#plt.figure()
#plt.title("Feature importances")
#plt.bar(np.arange(len(importances["feature"])), importances["importance"], align="center")
#plt.xticks(np.arange(len(importances["feature"])), importances["feature"])
#importances = importances.sort_values('importance',ascending=False).set_index('feature')
print importances.head(15), "\n"


#Checking correlation between GC content and temperature
#print "correlation between GC content and temperature: ", train_df.corr()
print "correlation between GC content and temperature: ", pearsonr(train_df["Temp"], train_df["GC Content"])
print "number of genus: ", len(genus)

plt.plot(train_df["Temp"], train_df["GC Content"], ".")
plt.plot(train_df["Temp"], np.poly1d(np.polyfit(train_df["Temp"], train_df["GC Content"], 1))(train_df["Temp"]))
plt.ylabel("GC content")
plt.xlabel("Temperature (C)")
plt.figure()
plt.show()



