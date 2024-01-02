import netCDF4 as nc
import csv

def extract_data_to_csv(file_path, output_csv):
    with nc.Dataset(file_path, 'r') as nc_file:
        
        global_attributes = nc_file.__dict__

        # Extract variables
        variables = {
            variable: nc_file.variables[variable][:] for variable in [
                'JULD', 'LATITUDE', 'LONGITUDE',
                'TEMP', 'TEMP_QC', 'TEMP_ADJUSTED', 'TEMP_ADJUSTED_QC', 'TEMP_ADJUSTED_ERROR',
                'PSAL', 'PSAL_QC', 'PSAL_ADJUSTED', 'PSAL_ADJUSTED_QC', 'PSAL_ADJUSTED_ERROR',
                'PRES', 'PRES_QC', 'PRES_ADJUSTED', 'PRES_ADJUSTED_QC', 'PRES_ADJUSTED_ERROR'
            ]
        }

        # Write to CSV
        with open(output_csv, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write global attributes to CSV
            csv_writer.writerow(['Global Attributes'])
            for key, value in global_attributes.items():
                csv_writer.writerow([key, value])

            
            csv_writer.writerow(['Variables'])
            csv_writer.writerow(variables.keys())

            
            csv_writer.writerow(['Data'])
            for i in range(len(variables['JULD'])):
                row_data = [variables[var][i] for var in variables]
                csv_writer.writerow(row_data)

if __name__ == "__main__":
    file_path = 'argo-profiles-5900905.nc'
    
    output_csv = 'samplefile_data.csv'
    
    extract_data_to_csv(file_path, output_csv)
