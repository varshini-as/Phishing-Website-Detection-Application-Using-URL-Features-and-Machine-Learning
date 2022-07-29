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

print(rfc.predict([[32, 0, 1, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1096, 544502]]))
