from datetime import datetime
import os
import pandas as pd


def filter_criteria3 (organization):
    for f in os.listdir('./commits/'+organization):
        print(f)
        file = open('./commits/'+organization+'/'+f,'r',encoding="utf-8")
        lines=file.readlines()
        sha = []
        message = []
        date = []
        a=datetime.strptime(lines[0].split('|')[len(lines[0].split('|'))-2], "%a, %d %b %Y %H:%M:%S %z")
        delta_date=[]
        for line in lines :
            tab = line.split('|')
            sha.append(tab[0])
            message.append(tab[1])
            date.append(datetime.strptime(tab[len(tab)-2], "%a, %d %b %Y %H:%M:%S %z"))
            delta_date.append(datetime.strptime(tab[len(tab)-2], "%a, %d %b %Y %H:%M:%S %z")-a)
            a=datetime.strptime(tab[len(tab)-2], "%a, %d %b %Y %H:%M:%S %z")
        
        df= pd.DataFrame({'sha':sha,'message':message,'date':date,'delta_date':delta_date})
        
        print(df)

filter_criteria3('Mirantis')