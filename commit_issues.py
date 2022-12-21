import pandas as pd
import json
import re
import os 

pattern='#[0-9]*'

def commit_issues(organization):
    for f in os.listdir('./commits_iac_scripts/'+organization):
        df= pd.read_csv('./commits_iac_scripts/'+organization+'/'+f).drop('Unnamed: 0',axis=1)
        issues=[]
        messages=df['message']
        for i in range(0,df.shape[0]) :
            if bool(re.search(pattern,messages[i])) == False :
                df.drop(i,inplace=True)
            else :
                issues.append(re.findall(pattern,messages[i]))
        df['issues']=issues
        df.to_csv('./commits_issues/'+organization+'/'+f)

commit_issues('Mirantis')
commit_issues('openstack')
#commit_issues('wikimedia')



