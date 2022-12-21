import pandas as pd
import re
import os

pattern_list=['.pp','conf','func','.yaml','.yml','Modulefile']
def commit_iac_script(organization):
    for f in os.listdir('./commits_files/'+organization):
        df= pd.read_csv('./commits_files/'+organization+'/'+f).drop('Unnamed: 0',axis=1)
        for i in range(0,df.shape[0]) :
            Bool=False
            for pattern in pattern_list : Bool=Bool or bool(re.search(pattern,df['files'][i]))
            if Bool == False :
                df.drop(i,inplace=True)
        df.to_csv('./commits_iac_scripts/'+organization+'/'+f)

commit_iac_script('Mirantis')
commit_iac_script('openstack')
#   commit_iac_script('wikimedia')






