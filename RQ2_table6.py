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
    mirantis.append([round(sum(dataframe_mir[x])/len(dataframe_mir[x]),2),round(max(dataframe_mir[x]),2)])
    mozilla.append([round(sum(dataframe_moz[x])/len(dataframe_moz[x]),2),round(max(dataframe_moz[x]),2)])
    openstack.append([round(sum(dataframe_ost[x])/len(dataframe_ost[x]),2),round(max(dataframe_moz[x]),2)])
    wikimedia.append([round(sum(dataframe_wik[x])/len(dataframe_ost[x]),2),round(max(dataframe_wik[x]),2)])



df=pd.DataFrame({'property':property,'mirantis':mirantis,'mozilla':mozilla,'openstack':openstack,'wikimedia':wikimedia})
print(df)
df.to_csv('table6')

