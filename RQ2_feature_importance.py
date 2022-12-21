import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import statistics

dataframe_mir=pd.read_csv('./data/IST_WIK.csv')

X=dataframe_mir.drop('defect_status',axis=1).drop('file_',axis=1).drop('org',axis=1)
y=dataframe_mir['defect_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

rf= RandomForestClassifier()
rf.fit(X_train, y_train)

y_predict=rf.predict(X_test)

accuracy_score(y_test,y_predict)

properties=X.columns
importances=[]
for f in properties:
    temp=[]
    for i in range (0,10):
        feature_importances = pd.DataFrame(rf.feature_importances_, index=X_train.columns, columns =['importance'])
        temp.append(round(feature_importances['importance'][f],2))
    importances.append(statistics.median(temp))

print(feature_importances)
print(len(properties))
df=pd.DataFrame({'properties':properties,'openstack':importances}).sort_values('openstack', ascending= False)
print(df)