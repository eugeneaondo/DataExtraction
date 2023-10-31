import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd

# Load the NetCDF files
SST_clim1 = Dataset('pacific_test.nc', "r+", format="NETCDF4")
SST_clim2 = Dataset('pacific2_test.nc', "r+", format="NETCDF4")

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

# Create arrays of shape (4138, 1) with island names
n_islands1 = len(islands1)
n_islands2 = len(islands2)

islands1 = np.array(islands1 * (4138 // n_islands1) + islands1[:4138 % n_islands1]).reshape((4138, 1))
islands2 = np.array(islands2 * (4138 // n_islands2) + islands2[:4138 % n_islands2]).reshape((4138, 1))

# Create a dictionary to store the average SST for each island
all_data = {}
for island in islands1[:, 0].tolist() + islands2[:, 0].tolist():
    all_data[island] = []

# Find the indices of the latitude and longitude values that match the island locations
island_lat_indices1 = np.where(lat1 == islands1)[0]
island_lon_indices1 = np.where(lon1 == islands1)[0]

# Calculate the average SST for each island (SST_clim1)
for t in range(len(time1)):
    for i in range(len(island_lat_indices1)):
        lat_idx = island_lat_indices1[i]
        lon_idx = island_lon_indices1[i]
        
        if 0 <= lat_idx < lat1.shape[0] and 0 <= lon_idx < lon1.shape[0]:
            all_data[islands1[i][0]].append(np.mean(SST_clim1.variables['analysed_sst'][t, lat_idx, lon_idx]) - 273.15)

# Find the indices of the latitude and longitude values that match the island locations (SST_clim2)
island_lat_indices2 = np.where(lat2 == islands2)[0]
island_lon_indices2 = np.where(lon2 == islands2)[0]

# Calculate the average SST for each island (SST_clim2)
for t in range(len(time2)):
    for i in range(len(island_lat_indices2)):
        lat_idx = island_lat_indices2[i]
        lon_idx = island_lon_indices2[i]
        
        if 0 <= lat_idx < lat2.shape[0] and 0 <= lon_idx < lon2.shape[0]:
            all_data[islands2[i][0]].append(np.mean(SST_clim2.variables['analysed_sst'][t, lat_idx, lon_idx]) - 273.15)

# Save the average SST for each island to a CSV file
all_data = pd.DataFrame(all_data)
all_data.to_csv('2021_data3.csv', index=False)
