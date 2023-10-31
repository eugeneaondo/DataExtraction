# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:10:09 2023

@author: J
"""


import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd
import os
from scipy import interpolate
import sys
from scipy.interpolate import griddata
from scipy.interpolate import Rbf


SST_clim1 = Dataset('pacific_test.nc',"r+", format = "NETCDF4")  
lon1 = np.array(SST_clim1.variables['lon'][:])
lat1 = np.array(SST_clim1.variables['lat'][:])
time1 = np.array(SST_clim1.variables['time'][:])
#sst = np.array(SST_clim1.variables['analysed_sst'][:]-273.15)


SST_clim2 = Dataset('pacific2_test.nc',"r+", format = "NETCDF4")  
lon2 = np.array(SST_clim2.variables['lon'][:])
lat2 = np.array(SST_clim2.variables['lat'][:])
time2 = np.array(SST_clim2.variables['time'][:])
#sst2 = np.array(SST_clim2.variables['analysed_sst'][:]-273.15)

ond_final = []
ond_final2 = []

#ylat = [-18.27,-8.35,-14.71,-21.62,13.23,0.38,7.01,15.14,7.08,7.33,-8.53,-0.54,-17.6,-13.99,-21.07,-21.19,-13.29,-18.95]
#xlon = [177.82,160.53,166.52,165.29,144.74,173.95,158.16,145.79,171.39,134.6,179.22,166.91,210.73,188.04,184.63,200.17,183.7,190.05]


ylat = np.array([-18.27,-8.35,-14.71,-21.62,13.23,0.38,7.01,15.14,7.08,7.33,-8.53,-0.54])
ylat2 = np.array([-17.6,-13.99,-21.07,-21.19,-13.29,-18.95])
#-18.27,-8.35,-14.71,-21.62,13.23,0.38,7.01,15.14,7.08,7.33,-8.53,-0.54
#-17.6,-13.99,-21.07,15.14,7.08,7.33,-8.53,-0.54

# longitude1 = np.array([177.74,161.0,156.55,165.55,144.7,173.89,158.12,145.9,171.16,134.55,179.2,166.86])
# longitude2 = np.array([-149.47,-171.52,-184.68,-159.84,-176.21,-169.8])
xlon = np.array([177.82,160.53,166.52,165.29,144.74,173.95,158.16,145.79,171.39,134.6,179.22,166.91])
xlon2 = np.array([-149.27,-171.96,-175.37,-159.83,-176.3,-169.95])

#islands = {'Viti Levu','Malaita','Espirito Santo','Grande Terre','Guam','Tarawa','PohnPei','Saipan','Majuro','Babeldaob','Tuvalu','Nauru','Tahiti','Upolu','Tongatapu','Rarotonga','Wallis','Niue'}

islands1 = ["VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam", "Tarawa", "Pohnpei",  "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"]
islands2 = ["Tahiti", "Upolu", "Tongatapu", "Rarotonga", "Wallis", "Niue"]



for d in range (len(islands1)):
    globals()[f"ond_{islands1[d]}"] = []
    
for e in range (len(islands2)):
    globals()[f"ond2_{islands2[e]}"] = []

#sst_1 = []
#sst_2 = []
for d in range (len(islands1)):
    globals()[f"sst_{islands1[d]}"] = []
    
for e in range (len(islands2)):
    globals()[f"sst2_{islands2[e]}"] = []



for x in range(len(islands1)):
    for i in range(len(ylat)):
        for j in range(len(xlon)):
            #i1= np.where(lat1 == i)
            #i2 = np.where(lon1 == j)
            #for x in range(len(islands1)):
                #for t in np.arange(0,time1.shape[0]):
        #for t in np.arange(0,time1.shape[0]):
                #for x in range(len(islands1)):
            #for i in ylat:
                #for j in xlon:
                #for t in np.arange(0,time1.shape[0]):
            i1= np.where(lat1 == ylat[i])
            i2 = np.where(lon1 == xlon[j])
             
            globals()[f"sst_{islands1[x]}"] = np.array(SST_clim1.variables['analysed_sst'][:,i1,i2]-273.15)
            globals()[f"ond_{islands1[x]}"] = globals()[f"sst_{islands1[x]}"].tolist()
                
                
#                 globals()[f"sst1_seas{t}"] = np.array(SST3[t,i1,i2])
#             globals()[f"SSTs{t}_final"].append(globals()[f"sst1_seas{t}"])            
            
for y in range(len(islands2)):            
    for k in range(len(ylat2)):
        for l in range(len(xlon2)):
            #i1= np.where(lat1 == i)
            #i2 = np.where(lon1 == j)
            #for x in range(len(islands1)):
                #for t in np.arange(0,time1.shape[0]):
        #for t in np.arange(0,time1.shape[0]):
                #for x in range(len(islands1)):
            #for i in ylat:
                #for j in xlon:
                #for t in np.arange(0,time1.shape[0]):
            j1= np.where(lat2 == ylat2[k])
            j2 = np.where(lon2 == xlon2[l])
                
            globals()[f"sst2_{islands2[y]}"] = np.array(SST_clim2.variables['analysed_sst'][:,j1,j2]-273.15)
            globals()[f"ond2_{islands2[y]}"] = globals()[f"sst2_{islands2[y]}"].tolist()
# for a in range(len(islands2)):            
# #for t in np.arange(0,time2.shape[0]):
#     for b in np.arange(0,time2.shape[0]):
#     #for x in range(len(islands2)):
#         for c in ylat2:
#             for h in xlon2:
#                 f1= np.where(lat2 == c)
#                 f2 = np.where(lon2 == h)
#                 globals()[f"sst2_{a}"] = np.array(sst2[b,f1,f2])
#         globals()[f"ond2_{islands2[a]}"].append(globals()[f"sst2_{a}"])                
               
#ond_final = [i[0] for i in ond_final]
#ond_final2 = [i[0] for i in ond_final2]


#%%
# year1=[]
# year2=[]
# for y in range (21):
#       year1_list = f'SSTy{y}_final'
#       year1.append(year1_list)
#       year2_list = f'SST2y{y}_final'
#       year2.append(year2_list)
     
# year1 = ', '.join(year1)
# year2 = ', '.join(year2)

# month1=[]
# month2=[]

# for w in range (12):
#       month1_list = f'SSTm{w}_final'
#       month1.append(month1_list)
#       month2_list = f'SST2m{w}_final'
#       month2.append(month2_list)
     
# month1 = ', '.join(month1)
# month2 = ', '.join(month2)
    
# mydata1 = zip(latitude1, longitude1, SST1_final, SSTs0_final, SSTs1_final, SSTs2_final, SSTs3_final, SSTy0_final, SSTy1_final, SSTy2_final, SSTy3_final, SSTy4_final, SSTy5_final, SSTy6_final, SSTy7_final, SSTy8_final, SSTy9_final, SSTy10_final, SSTy11_final, SSTy12_final, SSTy13_final, SSTy14_final, SSTy15_final, SSTy16_final, SSTy17_final, SSTy18_final, SSTy19_final, SSTy20_final,SSTm0_final, SSTm1_final, SSTm2_final, SSTm3_final, SSTm4_final, SSTm5_final, SSTm6_final, SSTm7_final, SSTm8_final, SSTm9_final, SSTm10_final, SSTm11_final)
# mydata2 = zip(latitude2, longitude2, SST2_final, SST2s0_final, SST2s1_final, SST2s2_final, SST2s3_final, SST2y0_final, SST2y1_final, SST2y2_final, SST2y3_final, SST2y4_final, SST2y5_final, SST2y6_final, SST2y7_final, SST2y8_final, SST2y9_final, SST2y10_final, SST2y11_final, SST2y12_final, SST2y13_final, SST2y14_final, SST2y15_final, SST2y16_final, SST2y17_final, SST2y18_final, SST2y19_final, SST2y20_final,SST2m0_final, SST2m1_final, SST2m2_final, SST2m3_final, SST2m4_final, SST2m5_final, SST2m6_final, SST2m7_final, SST2m8_final, SST2m9_final, SST2m10_final, SST2m11_final)
# head = ["Latitude", "Longitude", "SST Clim", "Season 1", "Season 2", "Season 3", "Season 4", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
mydata = zip(ond_EspiritoSanto, ond_GrandeTerre, ond_Guam, ond_Koror, ond_Majuro, ond_Malaita, ond_Nauru, ond_Pohnpei, ond_Saipan, ond_Tarawa, ond_Tuvalu, ond_VitiLevu, ond2_Rarotonga, ond2_Tahiti, ond2_Tongatapu, ond2_Upolu, ond2_Wallis)
head=["Espirito Santo", "Grande Terre", "Guam", "Babeldaob", "Majuro", "Malaita", "Nauru", "Pohnpei", "Saipan", "Tarawa", "Tuvalu", "Viti Levu", "Rarotonga", "Tahiti", "Tongatapu", "Upolu", "Wallis"]
my_df=pd.DataFrame(mydata)
my_df.to_csv('2021_data.csv', index=False, header=head)
# my_df1=pd.DataFrame(mydata1)

# my_df2=pd.DataFrame(mydata2)



# my_df1.to_csv('SST1_climatologies.csv', index=False, header=head)
# my_df2.to_csv('SST2_climatologies.csv', index=False, header=head)