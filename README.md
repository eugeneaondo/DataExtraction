# Data Extraction from NetCDF File

This repository provides a Python solution for extracting specific data from NetCDF files and saving it in a structured format. The primary use case for this code is to extract Sea Surface Temperature (SST) data for a list of islands from two NetCDF files, and save the extracted data into a CSV file.

## Prerequisites

Before using this code, ensure that you have the following prerequisites:

1. Python: You need to have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

2. Required Python Libraries: You should have the following Python libraries installed:
   - `netCDF4`: A library for reading and writing NetCDF files.
   

   You can install these libraries using pip:
   ```bash
   pip install numpy netCDF4 pandas
   ```

3. NetCDF Files: You should have NetCDF files containing the data you want to extract. In this specific example, we assume the existence of two NetCDF files named 'pacific_test.nc' and 'pacific2_test.nc'.
the files were not uploaded
## Usage

1. Clone this GitHub repository to your local machine or download the code files.

2. Place your NetCDF files ('pacific_test.nc' and 'pacific2_test.nc') in the same directory as the Python scripts.

3. Modify the script to define the list of islands and their coordinates as well as other parameters if needed.

4. Run the Python script `solution1.py`. This script will read the NetCDF files, extract the SST data for each island, and save it in a single CSV file ('all_island_data.csv').

   ```bash
   alldata.py    #for all data in both .nc files combined to one csv
   ```

## Customization

You can customize the code by modifying the island names and coordinates according to your specific data and NetCDF file. You can also adapt this code to extract different data variables from the NetCDF files.

## License

This project is licensed under the MIT License

## Author

- Eugene Aondo Nyamari
