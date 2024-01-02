import netCDF4
import pandas as pd
import os
import csv

def extract_coordinates_to_csv(netcdf_input, output_csv_file):

    with open(output_csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Latitude', 'Longitude'])

        if os.path.isfile(netcdf_input):
            # Process a single file
            process_netcdf_file(netcdf_input, csv_writer)
        else:
            # Process files within a directory
            for filename in os.listdir(netcdf_input):
                if filename.endswith('.nc'):
                    file_path = os.path.join(netcdf_input, filename)
                    process_netcdf_file(file_path, csv_writer)

def process_netcdf_file(netcdf_file, csv_writer):
    try:
        with netCDF4.Dataset(netcdf_file) as dataset:
            latitude = dataset.variables['latitude'][:]
            longitude = dataset.variables['longitude'][:]

            # Handle variable number of measurements
            if latitude.ndim == 1:
                latitude = latitude.reshape(-1, 1)  
                longitude = longitude.reshape(-1, 1)

            # Extract coordinates and write to CSV
            for lat, lon in zip(latitude, longitude):
                csv_writer.writerow([lat, lon])
    except Exception as e:
        print(f"Error processing {netcdf_file}: {e}")

if __name__ == '__main__':
    netcdf_input = 'argo-profiles-5900905.nc'  
    output_csv_file = 'output_coordinates.csv'  
    extract_coordinates_to_csv(netcdf_input, output_csv_file)
