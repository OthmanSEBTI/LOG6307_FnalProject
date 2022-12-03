import pandas as pd

dataframe_mir=pd.read_csv('./data/IST_MIR.csv')
dataframe_moz=pd.read_csv('./data/IST_MOZ.csv')
dataframe_ost=pd.read_csv('./data/IST_OST.csv')
dataframe_wik=pd.read_csv('./data/IST_WIK.csv')

property=dataframe_mir.columns[2:14]
mirantis=[]
mozilla=[]
openstack=[]
wikimedia=[]

for x in property :
    mirantis.append([sum(dataframe_mir[x])/len(dataframe_mir[x]),max(dataframe_mir[x])])
    mozilla.append([sum(dataframe_moz[x])/len(dataframe_moz[x]),max(dataframe_moz[x])])
    openstack.append([sum(dataframe_ost[x])/len(dataframe_ost[x]),max(dataframe_moz[x])])
    wikimedia.append([sum(dataframe_wik[x])/len(dataframe_ost[x]),max(dataframe_wik[x])])



df=pd.DataFrame({'property':property,'mirantis':mirantis,'mozilla':mozilla,'openstack':openstack,'wikimedia':wikimedia})
df.to_csv('table6')
