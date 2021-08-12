import xarray

import zipfile

import os

# assign name to file for download

zip_file = "download.zip"

# create variable for searching for all netcdf files

endswith = ".nc"

# try and except strategy for choosing netcdf files from zipped file

try:
    with zipfile.ZipFile(zip_file) as z:
        for file in z.namelist():
            if file.endswith(endswith):
                z.extract(file)
        print("Extracted all ", endswith)
except:
    print("Invalid file")

ext = ".nc"

# function to reclip data and create new file with name upon reclipping

dirname = "M:\Diss_data\Final\Humidity\Raw_Data\"
change = 1
for files in os.listdir(dirname):
    if files.endswith(ext):
        xds = xarray.open_dataset(files)
        xds = xds.where((xds.lon > 29)&(xds.lon < 35.2)&(xds.lat > -2)&(xds.lat < 4.295), drop=True)
        change = change + 1
        xds.to_netcdf(str(files)+str(change)+'clipped.nc')
    else:
        continue
