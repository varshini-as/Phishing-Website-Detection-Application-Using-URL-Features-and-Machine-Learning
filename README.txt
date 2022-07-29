Files that are required to run this project are listed below:

- phishing_dataset_final.csv (dataset)
This is the dataset required to train the classifier

- dataset_creation.py
This is the python program to extract required columns from dataset and generate another csv file. The generated dataset is phishing_dataset_final.csv

- database.py
This python file extracts only Phishy URLs from dataset in order to create a mongoDB database

- data_visualization.py
This python file is used for creating graphs for analyzing the data

- feature_extraction.py
This python program extracts URL features from the input URL

- train_model.py
This python program is used to train the ML model

- RandomForestClassifier.sav
This is the saved trained classifier having the accuracy of approximately 92.5%

- predictor.py
This program combines both the ML classifier and mongoDB database to predict the validity of the URL

- main.py
This is the main program which needs to be run in order to get the URL of the application which needs to be opened in the browser. The user needs to enter the required website and the result will be displayed.

The templated directory consists of the html pages that are used to design web application
- about.html
This is the homepage of the application

- catch_phish.html
This is the catch phish page where the user needs to enter the URL

- results.html
This is the result page

- The static directory consists of the style.css which is used for styling the webpages 

- The img directory inside static, consists of the images that are used to design the web application