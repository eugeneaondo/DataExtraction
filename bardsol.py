import netCDF4
import pandas as pd
import os

#  the .nc files
file_dir = "path/to/your/nc/files"


for filename in os.listdir(file_dir):
    if filename.endswith(".nc"):
        file_path = os.path.join(file_dir, filename)

        try:
           
            with netCDF4.Dataset(file_path, "r") as nc:

                
                latitude = nc.variables["LATITUDE"][:]
                longitude = nc.variables["LONGITUDE"][:]
                temperature = nc.variables["TEMP"][:]  
                salinity = nc.variables["PSAL"][:] 
                

                # pandas DataFrame
                df = pd.DataFrame({
                    "latitude": latitude,
                    "longitude": longitude,
                    "temperature": temperature,
                    "salinity": salinity,
                    # Add columns for other variables
                })

                
                csv_filename = os.path.splitext(filename)[0] + ".csv"
                df.to_csv(csv_filename, index=False)

        except Exception as e:
            print(f"Error processing {filename}: {e}")
