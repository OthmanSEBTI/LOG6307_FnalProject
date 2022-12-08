import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,  roc_auc_score



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
	metrics = classification_report(y_test,y_pred)
	roc = roc_auc_score(y_test,y_pred)

	return metrics, roc



to_process = ['IST_MIR.csv','IST_MOZ.csv','IST_OST.csv','IST_WIK.csv']
l = ['Results/mirantis_results.txt','Results/moz_results.txt','Results/ost_results.txt','Results/wiki_results.txt']

for line in to_process:
	for v in l:
		f = open(v, "w")
		p, r = process_data(line)
		for i in range(0, 10):
			f.write(line)
			f.write('\n')
			f.write(p)
			f.write('\n')
			f.write('ROC-AUC :' + str(r))
			f.write('\n')

