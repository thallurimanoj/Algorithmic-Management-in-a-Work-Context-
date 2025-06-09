import numpy as np
import pandas as pd
from sklearn import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('workset.csv')
df["Dev_Aspect1"] = df["Dev_Aspect1"].map({'EmployeesSatisfied':1 ,'EmployeesNotSatisfied':0})
df["Dev_Aspect2"] = df["Dev_Aspect2"].map({'ManagersSatisfied':1 ,'ManagersNotSatisfied':0})
df["Dev_Aspect3"] = df["Dev_Aspect3"].map({'CostinLimits':1 ,'CostExceeds':0})
df["Dev_Aspect4"] = df["Dev_Aspect4"].map({'CustomersSatisfied':1 ,'CustomersNotSatisfied':0})
df["Dev_Aspect5"] = df["Dev_Aspect5"].map({'OntimeDelivery':1 ,'DelayedDelivery':0})
df["Quality_Aspect1"] = df["Quality_Aspect1"].map({'UnitTestingOK':1 ,'UnitTestingNotOK':0})
df["Quality_Aspect2"] = df["Quality_Aspect2"].map({'IntTestingSatisfied':1 ,'IntTestingNotSatisfied':0})
df["Quality_Aspect3"] = df["Quality_Aspect3"].map({'RegrTestingOntime':1 ,'RegrTestingNotOntime':0})
df["Quality_Aspect4"] = df["Quality_Aspect4"].map({'SystemTestingOk':1 ,'SystemTestingNotOk':0})
df["Quality_Aspect5"] = df["Quality_Aspect5"].map({'UATSatisfied':1 ,'UATNotsatisfied':0})
df["Effectiveness"] = df["Effectiveness"].map({'Effective':1 ,'InEffective':0})
data = df[["Dev_Aspect1","Dev_Aspect2","Dev_Aspect3","Dev_Aspect4","Dev_Aspect5","Quality_Aspect1","Quality_Aspect2","Quality_Aspect3","Quality_Aspect4","Quality_Aspect5","Effectiveness"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:500]
training_outputs = outputs[:500]
testing_inputs = inputs[500:]
testing_outputs = outputs[500:]
classifier = RandomForestClassifier()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of RF Classifier on testing data is: " + str(accuracy))
testSet = [[0,0,1,0,0,0,1,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('RFC prediction on the first test set is:',predictions)
testSet = [[0,0,1,0,1,1,1,1,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('RFC prediction on the second test set is:',predictions)
