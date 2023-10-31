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

SST_clim2 = Dataset('pacific2_test.nc',"r+", format = "NETCDF4")
lon2 = np.array(SST_clim2.variables['lon'][:])
lat2 = np.array(SST_clim2.variables['lat'][:])
time2 = np.array(SST_clim2.variables['time'][:])

all_data = {}

ylat = np.array([-18.27,-8.35,-14.71,-21.62,13.23,0.38,7.01,15.14,7.08,7.33,-8.53,-0.54])
ylat2 = np.array([-17.6,-13.99,-21.07,-21.19,-13.29,-18.95])

for island in ["VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam", "Tarawa", "PohnPei", "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"]:
    all_data[island] = []

for t in range(len(time1)):
    for i, lat in enumerate(ylat):
        for j, lon in enumerate(xlon):
            for island in ["VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam", "Tarawa", "PohnPei", "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"]:
                if (lat, lon) == (islands1[i], islands2[j]):
                    all_data[island].append(SST_clim1.variables['analysed_sst'][t, i, j] - 273.15)

for t in range(len(time2)):
    for i, lat in enumerate(ylat2):
        for j, lon in enumerate(xlon2):
            for island in ["Tahiti", "Upolu", "Tongatapu", "Rarotonga", "Wallis", "Niue"]:
                if (lat, lon) == (islands2[i], islands2[j]):
                    all_data[island].append(SST_clim2.variables['analysed_sst'][t, i, j] - 273.15)

head = ["Espirito Santo", "Grande Terre", "Guam", "Babeldaob", "Majuro", "Malaita", "Nauru", "Pohnpei", "Saipan", "Tarawa", "Tuvalu", "Viti Levu", "Rarotonga", "Tahiti", "Tongatapu", "Upolu", "Wallis"]
my_df=pd.DataFrame(all_data)
my_df.to_csv('2021_data.csv', index=False, header=head)
