from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import json
import pandas as pd


def filtering(df):
    fiter_criteria1=df.loc[df['Private'] == False]
    fiter_criteria2 = fiter_criteria1.loc[df['Puppet_percentage'] >= 11]

    return fiter_criteria2

# rslt_df = dataframe.loc[dataframe['Language'] == 'Puppet']

# filtering(extract_repos(prepare_data('wikimedia',84))).to_csv('./repos_filtering/wikimedia_repos_filtering')
# filtering(extract_repos(prepare_data('openstack',26))).to_csv('./repos_filtering/openstack_repos_filtering')
Mirantis_repos=pd.read_csv('./repos_extraction/Mirantis_repos_extraction').drop('Unnamed: 0',axis=1)
openstack_repos=pd.read_csv('./repos_extraction/openstack_repos_extraction').drop('Unnamed: 0',axis=1)
wikimedia_repos=pd.read_csv('./repos_extraction/wikimedia_repos_extraction').drop('Unnamed: 0',axis=1)

filtering(Mirantis_repos).to_csv('./repos_filtering/Mirantis_repos_filtering')
filtering(openstack_repos).to_csv('./repos_filtering/openstack_repos_filtering')
filtering(wikimedia_repos).to_csv('./repos_filtering/wikimedia_repos_filtering')


