import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.ensemble import RandomForestClassifier

warnings.filterwarnings('ignore')

d=pd.read_csv("phishing_dataset_final.csv")

#Exploratory Data Analysis
plt.figure(figsize = (5 , 5))
plt.subplot(221)
sns.scatterplot(x = d["web_traffic"] , y = d["status"])
plt.xlabel("Web Traffic")
plt.ylabel("Status")
plt.subplot(222)
sns.scatterplot(x = d["domain_age"] , y = d["status"])
plt.xlabel("Domain Age")
plt.ylabel("Status")
plt.subplot(223)
sns.scatterplot(x = d["length_url"] , y = d["status"])
plt.xlabel("URL Length")
plt.ylabel("Status")
plt.subplot(224)
sns.scatterplot(x = d["nb_hyphens"] , y = d["status"])
plt.xlabel("nb_hyphens")
plt.ylabel("Status")
plt.show()

fig,ax=plt.subplots(3,3,sharey=True,figsize=(15,8))
plt.subplots_adjust(hspace=0.3)
sns.countplot(data=d,x='nb_com',hue='status',ax=ax[0,0])
sns.countplot(data=d,x='prefix_suffix',hue='status',ax=ax[0,1])
sns.countplot(data=d,x='whois_registered_domain',hue='status',ax=ax[0,2])
sns.countplot(data=d,x='nb_www',hue='status',ax=ax[1,0])
sns.countplot(data=d,x='nb_dots',hue='status',ax=ax[1,1])
sns.countplot(data=d,x='phish_hints',hue='status',ax=ax[1,2])
sns.countplot(data=d,x='ip',hue='status',ax=ax[2,0])
sns.countplot(data=d,x='nb_slash',hue='status',ax=ax[2,1])
sns.countplot(data=d,x='shortening_service',hue='status',ax=ax[2,2])
plt.show()



x=d.iloc[:,:-1]
y=d['status']
x.drop(['url'],axis=1,inplace=True)


plt.show()

rfc = RandomForestClassifier(n_estimators=10)
rfc.fit(x,y)
importances = rfc.feature_importances_
sorted_indices = np.argsort(importances)
fig,ax = plt.subplots()
ax.barh(range(len(importances)),importances[sorted_indices])
ax.set_yticks(range(len(importances)))
ax.set_yticklabels(np.array(x.columns)[sorted_indices])
plt.show()
