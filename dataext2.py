import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd

# Load the NetCDF files
SST_clim1 = Dataset('pacific_test.nc', "r+", format="NETCDF4")
SST_clim2 = Dataset('pacific2_test.nc', "r+", format="NETCDF4")

# Define the island names
islands = [
    "VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam",
    "Tarawa", "Pohnpei", "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"
]

islands2 = [
    "Tahiti", "Upolu", "Tongatapu", "Rarotonga", "Wallis", "Niue"
]

# Create dictionaries to store data for each island
island_data1 = {}
island_data2 = {}

# Extract data for SST_clim1
for island in islands:
    island_data1[island] = []

    # Replace this loop with your data extraction logic
    for t in range(SST_clim1.variables['analysed_sst'].shape[0]):
        island_data1[island].append(
            np.mean(SST_clim1.variables['analysed_sst'][t, :, :]) - 273.15
        )

# Extract data for SST_clim2
for island in islands2:
    island_data2[island] = []

    # Replace this loop with your data extraction logic
    for t in range(SST_clim2.variables['analysed_sst'].shape[0]):
        island_data2[island].append(
            np.mean(SST_clim2.variables['analysed_sst'][t, :, :]) - 273.15
        )

# Create DataFrames for SST_clim1 and SST_clim2
df1 = pd.DataFrame(island_data1)
df2 = pd.DataFrame(island_data2)

# Save the data to CSV files
df1.to_csv('data_ext1.csv', index=False)
df2.to_csv('data_ext2.csv', index=False)
