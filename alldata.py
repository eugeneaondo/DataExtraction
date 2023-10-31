import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd

#  NetCDF files
SST_clim1 = Dataset('pacific_test.nc', "r+", format="NETCDF4")
SST_clim2 = Dataset('pacific2_test.nc', "r+", format="NETCDF4")

# Adding island names
islands1 = [
    "VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam",
    "Tarawa", "Pohnpei", "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"
]

islands2 = [
    "Tahiti", "Upolu", "Tongatapu", "Rarotonga", "Wallis", "Niue"
]

# Create a dictionary to store data for each island
all_data = {}

# Extract data for SST_clim1
for island in islands1:
    all_data[island] = []

    # Replace this loop with your data extraction logic
    for t in range(SST_clim1.variables['analysed_sst'].shape[0]):
        all_data[island].append(
            np.mean(SST_clim1.variables['analysed_sst'][t, :, :]) - 273.15
        )

# Extract data for SST_clim2
for island in islands2:
    all_data[island] = []

    # Replace this loop with your data extraction logic
    for t in range(SST_clim2.variables['analysed_sst'].shape[0]):
        all_data[island].append(
            np.mean(SST_clim2.variables['analysed_sst'][t, :, :]) - 273.15
        )

# Create a DataFrame for all island data
all_data_df = pd.DataFrame(all_data)

# Save the data to a single CSV file can change name to 2021_data.csv
all_data_df.to_csv('all_island_data.csv', index=False)
