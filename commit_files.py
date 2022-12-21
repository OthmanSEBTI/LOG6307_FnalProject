from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import pandas as pd
import json
import os

def commit_files(organization):
    for f in ['puppet-ceph', 'puppet-cinder', 'puppet-designate', 'puppet-ec2api', 'puppet-glance', 'puppet-gnocchi', 'puppet-heat', 'puppet-horizon', 'puppet-ironic', 'puppet-keystone', 'puppet-magnum', 'puppet-manila', 'puppet-mistral', 'puppet-murano', 'puppet-neutron', 'puppet-nova', 'puppet-octavia', 'puppet-openstack-cookiecutter', 'puppet-openstack-integration', 'puppet-openstacklib', 'puppet-openstack_extras', 'puppet-oslo', 'puppet-pacemaker', 'puppet-rally', 'puppet-sahara', 'puppet-swift', 'puppet-tempest', 'puppet-tripleo', 'puppet-trove', 'puppet-vitrage', 'puppet-vswitch', 'puppet-zaqar']:
        file = open('./commits/'+organization+'/'+f, "r", encoding='utf-8')
        lines = file.readlines()
        sha=[]
        message=[]
        for line in lines :
            sha.append(line.split('|')[0])
            message.append(line.split('|')[1])

        dataframe =pd.DataFrame({'sha':sha,'message':message})

        url = 'https://api.github.com/repos/'+organization+'/'+f+'/commits/'
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
        dataframe.to_csv('./commits_files/'+organization+'/'+f)

# commit_files('Mirantis')
commit_files('openstack')
# commit_files('wikimedia')




        

