import netCDF4 as nc
import os
import csv

def extract_coordinates_and_temperature(file_path, output_csv):
    # Open the NetCDF file
    with nc.Dataset(file_path, 'r') as nc_file:
        latitudes = nc_file.variables['LATITUDE'][:]
        longitudes = nc_file.variables['LONGITUDE'][:]
        temperatures = nc_file.variables['TEMP'][:]  # Assuming temperature variable is named 'TEMP'

        with open(output_csv, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for profile_idx in range(len(latitudes)):
                lat = latitudes[profile_idx]
                lon = longitudes[profile_idx]
                temp = temperatures[profile_idx]
                csv_writer.writerow([lat, lon, temp])

def process_all_nc_files(input_directory, output_csv):
    for filename in os.listdir(input_directory):
        if filename.endswith(".nc"):
            file_path = os.path.join(input_directory, filename)
            print(f"Processing: {file_path}")
            extract_coordinates_and_temperature(file_path, output_csv)

if __name__ == "__main__":

    input_directory = 'your_input_directory'
    
    output_csv = 'output_coordinates_with_temperature.csv'
    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Latitude', 'Longitude', 'Temperature'])

    process_all_nc_files(input_directory, output_csv)
