import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd
import os
from scipy import interpolate
import sys
from scipy.interpolate import griddata
from scipy.interpolate import Rbf

# Load the NetCDF files
SST_clim1 = Dataset('pacific_test.nc', "r+", format = "NETCDF4")
SST_clim2 = Dataset('pacific2_test.nc', "r+", format = "NETCDF4")

# Get the latitude, longitude, and time variables
lon1 = np.array(SST_clim1.variables['lon'][:])
lat1 = np.array(SST_clim1.variables['lat'][:])
time1 = np.array(SST_clim1.variables['time'][:])

lon2 = np.array(SST_clim2.variables['lon'][:])
lat2 = np.array(SST_clim2.variables['lat'][:])
time2 = np.array(SST_clim2.variables['time'][:])

# Define the island names
islands1 = ["VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam", "Tarawa", "Pohnpei", "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"]
islands2 = ["Tahiti", "Upolu", "Tongatapu", "Rarotonga", "Wallis", "Niue"]

# Create a dictionary to store the average SST for each island
all_data = {}
for island in islands1 + islands2:
    all_data[island] = []

# Reshape the islands1 array to have a shape of (4138, 1)
islands1 = np.array(islands1).reshape((4138, 1))

# Append 3132 empty strings to the islands2 array
islands2.extend([""] * 3132)

# Reshape the islands2 array to have a shape of (4138, 1)
islands2 = np.array(islands2).reshape((4138, 1))

# Find the indices of the latitude and longitude values that match the island locations
island_lat_indices = np.where(lat1 == islands1)[0]
island_lon_indices = np.where(lon1 == islands1)[0]

# Calculate the average SST for each island
for t in range(len(time1)):
    for i in range(len(island_lat_indices)):
        all_data[islands1[i][0]].append(np.mean(SST_clim1.variables['analysed_sst'][t, island_lat_indices[i], island_lon_indices[i]]) - 273.15)

island_lat_indices = np.where(lat2 == islands2)[0]
island_lon_indices = np.where(lon2 == islands2)[0]

for t in range(len(time2)):
    for i in range(len(island_lat_indices)):
        all_data[islands2[i][0]].append(np.mean(SST_clim2.variables['analysed_sst'][t, island_lat_indices[i], island_lon_indices[i]]) - 273.15)

# Save the average SST for each island to a CSV file
all_data = pd.DataFrame(all_data)
all_data.to_csv('2021_data.csv', index=False, header=islands1 + islands2)