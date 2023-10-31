import numpy as np
import netCDF4 as nc
import pandas as pd

# Load the NetCDF files
SST_clim1 = nc.Dataset('pacific_test.nc', "r", format="NETCDF4")
SST_clim2 = nc.Dataset('pacific2_test.nc', "r", format="NETCDF4")

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

# Create a dictionary to store data for each island
all_data = {}  # Dictionary to store SST data for each island

# Extract data for SST_clim1
for island, coords in islands.items():
    lat = coords["lat"]
    lon = coords["lon"]
    lat_index = np.where(SST_clim1.variables['lat'][:] == lat)[0][0]
    lon_index = np.where(SST_clim1.variables['lon'][:] == lon)[0][0]
    sst_data = SST_clim1.variables['analysed_sst'][:, lat_index, lon_index] - 273.15
    all_data[island] = sst_data

# Extract data for SST_clim2
for island, coords in islands2.items():
    lat = coords["lat"]
    lon = coords["lon"]
    lat_index = np.where(SST_clim2.variables['lat'][:] == lat)[0][0]
    lon_index = np.where(SST_clim2.variables['lon'][:] == lon)[0][0]
    sst_data = SST_clim2.variables['analysed_sst'][:, lat_index, lon_index] - 273.15
    all_data[island] = sst_data

# Create a DataFrame for all island data
all_data_df = pd.DataFrame(all_data)

# Save the data to a single CSV file
all_data_df.to_csv('data2.csv', index=False)
