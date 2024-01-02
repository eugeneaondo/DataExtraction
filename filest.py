
import netCDF4 as nc

def write_nc_structure_to_txt(file_path, output_file):
    # Open the NetCDF file
    with nc.Dataset(file_path, 'r') as nc_file:
        # Write the structure information to the text file
        with open(output_file, 'w') as output_txt:
            # Write global attributes
            output_txt.write("Global Attributes:\n")
            for attr_name in nc_file.ncattrs():
                output_txt.write(f"{attr_name}: {getattr(nc_file, attr_name)}\n")

            # Write dimensions
            output_txt.write("\nDimensions:\n")
            for dim_name, dim in nc_file.dimensions.items():
                output_txt.write(f"{dim_name}: {len(dim)}\n")

            # Write variables and their attributes
            output_txt.write("\nVariables:\n")
            for var_name, var in nc_file.variables.items():
                output_txt.write(f"{var_name} (Shape: {var.shape}, Type: {var.dtype})\n")
                for attr_name in var.ncattrs():
                    output_txt.write(f"  {attr_name}: {getattr(var, attr_name)}\n")

if __name__ == "__main__":
    # Replace 'your_file.nc' with the actual file path
    file_path = 'argo-profiles-5900905.nc'
    
    # Replace 'output_structure.txt' with the desired output text file name
    output_file = 'output_structure.txt'
    
    write_nc_structure_to_txt(file_path, output_file)

