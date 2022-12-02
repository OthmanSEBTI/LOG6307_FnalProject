from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import pandas as pd
import json


file = open('./commits/puppetlabs-openstack', "r", encoding='utf-8')
lines = file.readlines()
sha=[]
message=[]
for line in lines :
    sha.append(line.split('|')[0])
    message.append(line.split('|')[1])

dataframe =pd.DataFrame({'sha':sha,'message':message})

url = 'https://api.github.com/repos/Mirantis/puppetlabs-openstack/commits/'
files=[]
for sha in dataframe['sha']:

    listOfFiles=[] 
    request_gitapi = Request(url + sha, headers={
                                "authorization": "Bearer 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"})
    url1 = urlopen(request_gitapi)
    data = json.load(url1)
    for file in data['files'] :
        listOfFiles.append(file['filename'])
    files.append(listOfFiles)

dataframe['files']=files
dataframe.to_csv('./commits_files/puppetlabs-openstack')



        

