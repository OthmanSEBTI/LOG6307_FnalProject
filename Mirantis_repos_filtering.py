from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import json
import pandas as pd

def extract_repos(Organization):
    url_repos = 'https://api.github.com/orgs/'+ Organization +'/repos'
    f1 = open('./Mirantis_repos/Mirantis_repos_extraction', "w", encoding='utf-8')
    request_gitapi_repos = Request(url_repos, headers={
                             "authorization": "#githubapitoken"})
    url = urlopen(request_gitapi_repos)
    data = json.load(url)
    id=[]
    name=[]
    full_name=[]
    private=[]
    fork=[]
    language=[]
    puppet_percentage=[]
    for x in data:
        #f1.write(x["id"])
        id.append(x["id"])
        name.append(x["name"])
        full_name.append(x["full_name"])
        private.append(x["private"])
        fork.append(x["fork"])
        language.append(x["language"])
        url_reposlanguages = 'https://api.github.com/repos/'+str(x["full_name"])+'/languages'
        request_gitapi_reposlanguages = Request(url_reposlanguages, headers={
                             "authorization": "Bearer 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"})
        data1 = json.load(urlopen(request_gitapi_reposlanguages))
        if 'Puppet' in data1.keys():
            puppet_percentage.append(100*(data1['Puppet']/sum(data1.values())))
        else:
            puppet_percentage.append(0)
    dataframe = pd.DataFrame({'Id':id,'Name':name,'Full_name':full_name,'Private':private, 'Fork':fork,'Language':language,'Puppet_percentage':puppet_percentage}, columns = ['Id','Name', 'Full_name', 'Private', 'Fork','Language','Puppet_percentage'])
    return dataframe

def filtering(df):
    fiter_criteria1=df.loc[df['Private'] == False]
    fiter_criteria2 = fiter_criteria1.loc[df['Puppet_percentage'] > 11]

    return fiter_criteria2

# rslt_df = dataframe.loc[dataframe['Language'] == 'Puppet']
print(print(filtering(extract_repos('Mirantis'))))