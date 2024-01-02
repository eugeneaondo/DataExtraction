import netCDF4 as nc
import os
import csv

def extract_coordinates_from_nc(file_path, output_csv):
    # Open the NetCDF file
    with nc.Dataset(file_path, 'r') as nc_file:
        # Extract coordinates
        latitudes = nc_file.variables['LATITUDE'][:]
        longitudes = nc_file.variables['LONGITUDE'][:]

        # Write coordinates to CSV file
        with open(output_csv, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for profile_idx in range(len(latitudes)):
                lat = latitudes[profile_idx]
                lon = longitudes[profile_idx]
                csv_writer.writerow([lat, lon])

def process_all_nc_files(input_directory, output_csv):
    # Loop through all files in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".nc"):
            file_path = os.path.join(input_directory, filename)
            print(f"Processing: {file_path}")
            extract_coordinates_from_nc(file_path, output_csv)

if __name__ == "__main__":
    # Replace 'your_input_directory' with the directory containing NetCDF files
    input_directory = 'your_input_directory'
    
    # Replace 'output_coordinates.csv' with the desired output CSV file name
    output_csv = 'output_coordinates.csv'

    # Clear the existing content of the output CSV file
    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Latitude', 'Longitude'])

    # Process all NetCDF files in the specified directory
    process_all_nc_files(input_directory, output_csv)
