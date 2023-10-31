import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd

# Load the NetCDF files
SST_clim1 = Dataset('pacific_test.nc', "r+", format="NETCDF4")
SST_clim2 = Dataset('pacific2_test.nc', "r+", format="NETCDF4")

# Define the island names and their coordinates
islands = {
    "VitiLevu": {"lat": -18.27, "lon": 177.82},
    "Malaita": {"lat": -8.35, "lon": 160.53},
    "EspiritoSanto": {"lat": -14.71, "lon": 166.52},
    "GrandeTerre": {"lat": -21.62, "lon": 165.29},
    "Guam": {"lat": 13.23, "lon": 144.74},
    "Tarawa": {"lat": 0.38, "lon": 173.95},
    "Pohnpei": {"lat": 7.01, "lon": 158.16},
    "Saipan": {"lat": 15.14, "lon": 145.79},
    "Majuro": {"lat": 7.08, "lon": 171.39},
    "Koror": {"lat": 7.33, "lon": 134.6},
    "Tuvalu": {"lat": -8.53, "lon": 179.22},
    "Nauru": {"lat": -0.54, "lon": 166.91}
}

islands2 = {
    "Tahiti": {"lat": -17.6, "lon": -149.27},
    "Upolu": {"lat": -13.99, "lon": -171.96},
    "Tongatapu": {"lat": -21.07, "lon": -175.37},
    "Rarotonga": {"lat": -21.19, "lon": -159.83},
    "Wallis": {"lat": -13.29, "lon": -176.3},
    "Niue": {"lat": -18.95, "lon": -169.95}
}

# Create dictionaries to store data for each island
island_data1 = {}
island_data2 = {}

# Extract data for SST_clim1
for island, coords in islands.items():
    lat = coords["lat"]
    lon = coords["lon"]

    # Extract data using lat and lon
    i1 = np.where(SST_clim1.variables['lat'][:] == lat)
    i2 = np.where(SST_clim1.variables['lon'][:] == lon)

    # Replace this line with your data extraction logic
    island_data1[island] = SST_clim1.variables['analysed_sst'][:, i1[0], i2[0]].squeeze() - 273.15

# Extract data for SST_clim2
for island, coords in islands2.items():
    lat = coords["lat"]
    lon = coords["lon"]

    # Extract data using lat and lon
    j1 = np.where(SST_clim2.variables['lat'][:] == lat)
    j2 = np.where(SST_clim2.variables['lon'][:] == lon)

    # Replace this line with your data extraction logic
    island_data2[island] = SST_clim2.variables['analysed_sst'][:, j1[0], j2[0]].squeeze() - 273.15

# Create a DataFrame for SST_clim1
df1 = pd.DataFrame(island_data1)

# Create a DataFrame for SST_clim2
df2 = pd.DataFrame(island_data2)

# Save the data to CSV files
df1.to_csv('SST_clim1_data.csv', index=False)
df2.to_csv('SST_clim2_data.csv', index=False)
