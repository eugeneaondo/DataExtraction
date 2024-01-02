import netCDF4
import pandas as pd


file_path = "argo-profiles-5900905.nc"  

try:

    with netCDF4.Dataset(file_path, "r") as nc:

        
        latitude = nc.variables["LATITUDE"][:]
        if len(latitude.shape) > 1:
            latitude = latitude.flatten()

        longitude = nc.variables["LONGITUDE"][:]
        if len(longitude.shape) > 1:
            longitude = longitude.flatten()

        temperature = nc.variables["TEMP"][:]
        salinity = nc.variables["PSAL"][:]
        
        df = pd.DataFrame({
            "latitude": latitude,
            "longitude": longitude,
            "temperature": temperature,
            "salinity": salinity,
            # Add columns for other variables
        })

        # CSV file
        csv_filename = "extracted_data.csv"  
        df.to_csv(csv_filename, index=False)

except Exception as e:
    print(f"Error processing {file_path}: {e}")
