import os
import pandas as pd
from pyproj import Proj, transform

def convert_to_utm(lon, lat):
    # Define the UTM projection (for example, UTM Zone 33N)
    utm_zone_nepal = 45
    utm_proj = Proj(proj="utm", zone=utm_zone_nepal, ellps="WGS84")

    # Convert longitude and latitude to UTM easting and northing
    easting, northing = utm_proj(lon, lat)
    return easting, northing

def convert_csv_to_utm(input_file, output_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Convert latitude and longitude to UTM coordinates
    df['Easting'], df['Northing'] = zip(*df.apply(lambda row: convert_to_utm(row['Longitude'], row['Latitude']), axis=1))

    # Save the updated DataFrame with UTM coordinates to a new CSV file
    df.to_csv(output_file, index=False)

def process_all_csv_files(root_directory):
    # Iterate through files in the root directory
    for filename in os.listdir(root_directory):
        if filename.endswith(".csv"):
            input_file = os.path.join(root_directory, filename)
            output_file = os.path.join(root_directory, f'utm_{filename}')
            convert_csv_to_utm(input_file, output_file)

# Set the root directory to the current working directory
root_dir = os.getcwd()

# Call the function to process all CSV files in the root directory
process_all_csv_files(root_dir)
