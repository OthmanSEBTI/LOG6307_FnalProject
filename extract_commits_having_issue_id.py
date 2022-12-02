import pandas as pd
import json
import re

pattern='\(#[0-9]*\) '
dataframe=pd.read_csv('./commits_files/puppetlabs-openstack')
dataframe.pop('Unnamed: 0')
issues=[]
messages=dataframe['message']
for message in messages:
    issues.append(re.findall(pattern,message))
dataframe['issues']=issues
dataframe.to_csv('./commits_issues/puppetlabs-openstack')

