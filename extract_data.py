import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd

# Load the NetCDF files containing SST data
SST_clim1 = Dataset('pacific_test.nc', "r+", format="NETCDF4")
SST_clim2 = Dataset('pacific2_test.nc', "r+", format="NETCDF4")

# Define the island names
islands1 = [
    "VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam",
    "Tarawa", "Pohnpei", "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"
]

islands2 = [
    "Tahiti", "Upolu", "Tongatapu", "Rarotonga", "Wallis", "Niue"
]

# Create a dictionary to store data for each island
all_data = {}  # Dictionary to store SST data for each island

# Extract data for SST_clim1
for island in islands1:
    all_data[island] = []  # List to store SST data for each island in SST_clim1

    # Replace this loop with your data extraction logic
    for t in range(SST_clim1.variables['analysed_sst'].shape[0]):
        all_data[island].append(
            np.mean(SST_clim1.variables['analysed_sst'][t, :, :]) - 273.15
        )  # Calculate the mean SST for each island in SST_clim1, subtracting 273.15 to convert from Kelvin to Celsius

# Extract data for SST_clim2
for island in islands2:
  all_data[island] = []  # List to store SST data for each island in SST_clim2

  # Replace this loop with your data extraction logic
  for t in range(SST_clim2.variables['analysed_sst'].shape[0]):
    all_data[island].append(
     np.mean(SST_clim2.variables['analysed_sst'][t, :, :]) - 273.15
        )  # Calculate the mean SST for each island in SST_clim2, subtracting 273.15 to convert from Kelvin to Celsius

# Create a DataFrame for all island data
all_data_df = pd.DataFrame(all_data)  # Create a DataFrame from the all_data dictionary

# Save the data to a single CSV file
all_data_df.to_csv('all_island_data.csv', index=False)  # Save the DataFrame to a CSV file
