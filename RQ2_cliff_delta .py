import pandas as pd
import statistics
from cliffs_delta import cliffs_delta

dataframe_mir=pd.read_csv('./data/IST_MIR.csv')
dataframe_moz=pd.read_csv('./data/IST_MOZ.csv')
dataframe_ost=pd.read_csv('./data/IST_OST.csv')
dataframe_wik=pd.read_csv('./data/IST_WIK.csv')

property=dataframe_mir.columns[2:14]
mirantis=[]
mozilla=[]
openstack=[]
wikimedia=[]



# perform two-sided test. You can use 'greater' or 'less' for one-sided test
 #   d,res=cliffs_delta(D[x],ND[x])
 
for x in property :
    D=dataframe_mir[ dataframe_mir['defect_status'] ==1]
    ND=dataframe_mir[ dataframe_mir['defect_status'] ==0]
    mirantis.append(round(cliffs_delta(D[x],ND[x])[0],2))
    D=dataframe_moz[ dataframe_moz['defect_status'] ==1]
    ND=dataframe_moz[ dataframe_moz['defect_status'] ==0]
    mozilla.append(round(cliffs_delta(D[x],ND[x])[0],2))
    D=dataframe_ost[ dataframe_ost['defect_status'] ==1]
    ND=dataframe_ost[ dataframe_ost['defect_status'] ==0]
    openstack.append(round(cliffs_delta(D[x],ND[x])[0],2))
    D=dataframe_wik[ dataframe_wik['defect_status'] ==1]
    ND=dataframe_wik[ dataframe_wik['defect_status'] ==0]
    wikimedia.append(round(cliffs_delta(D[x],ND[x])[0],2))



df=pd.DataFrame({'property':property,'mirantis':mirantis,'mozilla':mozilla,'openstack':openstack,'wikimedia':wikimedia})
print(df)
df.to_csv('table8_cliffs_delta')



