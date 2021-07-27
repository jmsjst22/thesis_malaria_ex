import xarray
import zipfile
import os

'''

Intent

Extracting and clipping netcdf file to unified extent

Requirements

Zip files containing netcdf format, which can be identified by prefix. Folders
can be renamed at zip_file variable.

Warning

Errors at extent caused by precision accuracy will require that all data clipped
will also need to be regridded with a designated tolerance before analysis


'''



#define folders to be unzipped
zip_file = "download.zip"
#define file suffix to be searched for when unzipping
endswith = ".nc"

try:
    with zipfile.ZipFile(zip_file) as z: #create list to populate z variable
        for file in z.namelist(): #loop through list
            if file.endswith(endswith): # introduce suffix
                z.extract(file) # extract
        print("Extracted all ", endswith)
except:
    print("Invalid file") # test for extraction and error


dirname = "" # directory name to be defined depending on variable and location
for files in os.listdir(dirname): # list all files in directory
    if files.endswith(endswith): # select if ends with .nc suffix
        xds = xarray.open_dataset(files)  #open data set with xarray
        xds = xds.where((xds.lon > 29)&(xds.lon < 35.2)&(xds.lat > -2)&(xds.lat < 4.295), drop=True)
        xds.to_netcdf((str(files)[:3])+'clipped.nc') # rewrite netcdf, rename discarding suffix and introducing new designating clipped
    else:
        continue
