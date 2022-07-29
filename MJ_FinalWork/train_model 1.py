import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# #Reading the csv file and storing it in a dataframe
# data = pd.read_csv("dataset_phishing.csv")
# print(data)

# #Viewing the statistical details of the data
# print(data.describe())

# #Determining the datatypes of data in each column
# print(data.dtypes)

# #Total null values in the dataset
# print(data.isnull().sum())

# sns.heatmap(data.isnull())
# plt.show()

#Creating a new dataframe with selected columns
# df = pd.DataFrame(data,columns=['url','length_url','ip','nb_dots','nb_hyphens','nb_at','nb_qm','nb_and','nb_eq','nb_percent','nb_slash','nb_colon','nb_semicolumn','nb_www','nb_com','nb_dslash','https_token','prefix_suffix','phish_hints','shortening_service','submit_email','whois_registered_domain','status'])
# print(df)

# #Replacing the categorical values
# df["status"].replace({"legitimate":0,"phishing":1},inplace=True)
# print(df)


# #Convert dataframe into csv file
# df.to_csv('phishing_dataset.csv',index=False)

d=pd.read_csv("phishing_dataset_final.csv")
x=d.iloc[:,:-1]
y=d['status']
x.drop(['url'],axis=1,inplace=True)
print(x)
print("\n",y)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=0)
#sc_x = StandardScaler()
#x_train = sc_x.fit_transform(x_train)
#x_test = sc_x.fit_transform(x_test)

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

rfc = RandomForestClassifier(n_estimators=10)
rfc.fit(x_train,y_train)
y_pred = rfc.predict(x_test)
print("\n",y_pred,"\n")

# Save ML model to disk in pickle file
# model_filename = "RandomForestClassifier.sav"
# saved_model = pickle.dump(rfc, open(model_filename,'wb'))

cnf_matrix=metrics.confusion_matrix(y_test,y_pred)
print(cnf_matrix)
sns.heatmap(pd.DataFrame(cnf_matrix),annot=True,fmt='g')
plt.show()

print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))
print("Precision : ",metrics.precision_score(y_test,y_pred))
print("Recall : ",metrics.recall_score(y_test,y_pred))
rfc_score_train = rfc.score(x_train,y_train)
rfc_score_test = rfc.score(x_test,y_test)
print(rfc.predict([[32, 0, 1, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1096, 544502]]))

"""
from sklearn import svm
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train_std = sc_x.fit_transform(x_train)
x_test_std = sc_x.transform(x_test)
svm = svm.SVC()
svm.fit(x_train_std,y_train)
y_test_pred = svm.predict(x_test_std)
print("Accuracy : ",metrics.accuracy_score(y_test,y_test_pred))
print("Precision : ",metrics.precision_score(y_test,y_test_pred))
print("Recall : ",metrics.recall_score(y_test,y_test_pred))


from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(x_train_std,y_train)
prediction = logmodel.predict(x_test_std)
print("Accuracy : ",metrics.accuracy_score(y_test,prediction))
print("Precision : ",metrics.precision_score(y_test,prediction))
print("Recall : ",metrics.recall_score(y_test,prediction))
"""
from sklearn.preprocessing import StandardScaler
Scaler = StandardScaler()
Scaler.fit(x_train)
x_train=Scaler.transform(x_train)
x_test=Scaler.transform(x_test)
from sklearn import svm
svm = svm.SVC()
svm.fit(x_train,y_train)
y_test_pred = svm.predict(x_test)
svm_score_train = svm.score(x_train,y_train)
svm_score_test = svm.score(x_test,y_test)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)
prediction = logmodel.predict(x_test)
lr_score_train = logmodel.score(x_train,y_train)
lr_score_test = logmodel.score(x_test,y_test)


models = pd.DataFrame({'Model':['Random Forest', 'Support Vector Machine', 'Logistic Regression'],'Train_Score':[rfc_score_train,svm_score_train,lr_score_train],'Test_Score':[rfc_score_test,svm_score_test,lr_score_test]})
models.sort_values(by='Test_Score', ascending=False)
print(models)

Model = ['Random Forest', 'Support Vector Machine', 'Logistic Regression']
Train_Score = [rfc_score_train,svm_score_train,lr_score_train]
Test_Score = [rfc_score_test,svm_score_test,lr_score_test]

x = np.arange(len(Model))
width = 0.4
fig, ax = plt.subplots()
ax.bar(x-width/2,Train_Score,width,label="Train_Score")
ax.bar(x+width/2,Test_Score,width,label="Test_Score")
ax.set_ylabel('Scores')
ax.set_xticks(x)
ax.set_xticklabels(Model)
ax.legend()
plt.show()
