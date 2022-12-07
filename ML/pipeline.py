import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix



def process_data(path):
	df = pd.read_csv(path)
	dataset = df[['URL','File','Lines_of_code','Require','Ensure','Include','Attribute','Hard_coded_string','Comment','Command','File_mode','SSH_KEY','defect_status']]
	
	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 12].values
	
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.1)
	scaler = StandardScaler()
	scaler.fit(X_train)
	X_train = scaler.transform(X_train)
	X_test = scaler.transform(X_test)
	classifier = KNeighborsClassifier(n_neighbors=3)
	classifier.fit(X_train,y_train)
	y_pred = classifier.predict(X_test)

	return classification_report(y_test,y_pred)

f = open("result.txt", "w")
to_process = ['IST_MIR.csv','IST_MOZ.csv','IST_OST.csv','IST_WIK.csv']
for line in to_process:
	p = process_data(line)
	f.write(p)
	f.write('\n')
