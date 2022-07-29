import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

#Reading the csv file and storing it in a dataframe
data = pd.read_csv("dataset_phishing.csv")
print(data)

#Viewing the statistical details of the data
print(data.describe())

#Determining the datatypes of data in each column
print(data.dtypes)

#Total null values in the dataset
print(data.isnull().sum())

sns.heatmap(data.isnull())
plt.show()

# Creating a new dataframe with selected columns
df = pd.DataFrame(data,columns=['url','length_url','ip','nb_dots','nb_hyphens','nb_at','nb_qm','nb_and','nb_eq','nb_percent','nb_slash','nb_colon','nb_semicolumn','nb_www','nb_com','nb_dslash','https_token','prefix_suffix','phish_hints','shortening_service','submit_email','whois_registered_domain','status'])
print(df)

#Replacing the categorical values
df["status"].replace({"legitimate":0,"phishing":1},inplace=True)
print(df)


#Convert dataframe into csv file
df.to_csv('phishing_dataset.csv',index=False)