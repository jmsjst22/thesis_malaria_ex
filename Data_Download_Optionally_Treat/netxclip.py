import xarray

import zipfile

import os

zip_file = "download.zip"
endswith = ".nc"
try:
    with zipfile.ZipFile(zip_file) as z:
        for file in z.namelist():
            if file.endswith(endswith):
                z.extract(file)
        print("Extracted all ", endswith)
except:
    print("Invalid file")

ext = ".nc"

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
