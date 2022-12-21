from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import json
import pandas as pd

def prepare_data(organization,page_number) :
    url_repos = 'https://api.github.com/orgs/'+ organization +'/repos?page=1'
    request_gitapi_repos = Request(url_repos, headers={
                                    "authorization": "Bearer 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"})
    url = urlopen(request_gitapi_repos)
    data = json.load(url)

    for i in range (2,page_number) :
        url_repos = 'https://api.github.com/orgs/'+ organization+'/repos?page='+str(i)
        request_gitapi_repos = Request(url_repos, headers={
                                    "authorization": "Bearer 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"})
        url = urlopen(request_gitapi_repos)
        data = data+json.load(url)
    return data

def extract_repos(data):
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

extract_repos(prepare_data('Mirantis',9)).to_csv('./repos_extraction/Mirantis_repos_extraction')
extract_repos(prepare_data('openstack',27)).to_csv('./repos_extraction/openstack_repos_extraction')
extract_repos(prepare_data('wikimedia',85)).to_csv('./repos_extraction/wikimedia_repos_extraction')

