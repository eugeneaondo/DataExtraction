import numpy as np
import netCDF4 as nc
from netCDF4 import Dataset
import pandas as pd

SST_clim1 = Dataset('pacific_test.nc', "r+", format="NETCDF4")
lon1 = np.array(SST_clim1.variables['lon'][:])
lat1 = np.array(SST_clim1.variables['lat'][:])
# time1 = np.array(SST_clim1.variables['time'][:])

SST_clim2 = Dataset('pacific2_test.nc', "r+", format="NETCDF4")
lon2 = np.array(SST_clim2.variables['lon'][:])
lat2 = np.array(SST_clim2.variables['lat'][:])
# time2 = np.array(SST_clim2.variables['time'][:])

ylat = np.array([-18.27, -8.35, -14.71, -21.62, 13.23, 0.38, 7.01, 15.14, 7.08, 7.33, -8.53, -0.54])
ylat2 = np.array([-17.6, -13.99, -21.07, -21.19, -13.29, -18.95])

xlon = np.array([177.82, 160.53, 166.52, 165.29, 144.74, 173.95, 158.16, 145.79, 171.39, 134.6, 179.22, 166.91])
xlon2 = np.array([-149.27, -171.96, -175.37, -159.83, -176.3, -169.95])

islands1 = ["VitiLevu", "Malaita", "EspiritoSanto", "GrandeTerre", "Guam", "Tarawa", "Pohnpei", "Saipan", "Majuro", "Koror", "Tuvalu", "Nauru"]
islands2 = ["Tahiti", "Upolu", "Tongatapu", "Rarotonga", "Wallis", "Niue"]

for d in range(len(islands1)):
    globals()[f"ond_{islands1[d]}"] = []

for e in range(len(islands2)):
    globals()[f"ond2_{islands2[e]}"] = []

for d in range(len(islands1)):
    for i in range(len(ylat)):
        for j in range(len(xlon)):
            i1 = np.where(lat1 == ylat[i])
            i2 = np.where(lon1 == xlon[j])

            globals()[f"sst_{islands1[d]}"] = np.array(SST_clim1.variables['analysed_sst'][:, i1[0], i2[0]].squeeze() - 273.15)
            globals()[f"ond_{islands1[d]}"] = globals()[f"sst_{islands1[d]}"].tolist()

for e in range(len(islands2)):
    for k in range(len(ylat2)):
        for l in range(len(xlon2)):
            j1 = np.where(lat2 == ylat2[k])
            j2 = np.where(lon2 == xlon2[l])

            globals()[f"sst2_{islands2[e]}"] = np.array(SST_clim2.variables['analysed_sst'][:, j1[0], j2[0]].squeeze() - 273.15)
            globals()[f"ond2_{islands2[e]}"] = globals()[f"sst2_{islands2[e]}"].tolist()

all_data = {}

for island in islands1:
    all_data[island] = globals()[f"ond_{island}"]

for island in islands2:
    all_data[island] = globals()[f"ond2_{island}"]

all_data_df = pd.DataFrame(all_data)

# Save the data to a single CSV file
all_data_df.to_csv('code1.csv', index=False)
