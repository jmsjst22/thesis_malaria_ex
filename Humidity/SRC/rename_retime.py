import netCDF4 as nc
import numpy as np
import xarray as xr
import os
import glob
import zipfile
import subprocess
import os

'''

Intent

Manage and analyse unzipped netCDF files as part of the Relative Humidity pre-analysis process.

Processes include renaming files, adjusting time in all files relative to their original
download name (as this is where this metadata is most consistently accessible- some files
had no metadata at download).

Requirements are limited as most directories are made upon actioning and most files are replicated,
limiting storage demands.

'''

# Designate storage management commands
command = ('mkdir /home/s1987119/Diss_data/Final_raw/humidity/unzippedhumidity/')
command1 = ('mkdir /home/s1987119/Diss_data/Final/Humidity/Process/concat/')
command2 = ('rm -r /home/s1987119/Diss_data/Final/Humidity/Process/unzippedhumidity')

#initiate with subprocess call to make command line available in python script
commander = subprocess.call(command,shell=True)
commander1 = subprocess.call(command1,shell=True)
commander2 = subprocess.call(command2,shell=True)


print(commander,commander1)
#List pre-clipped folders ending in correct suffix
for file in glob.glob('/home/s1987119/Diss_data/Final/Humidity/Raw_Data/*_clipped.zip'):
    #Extract when condition is met to generated directory
    with zipfile.ZipFile(file) as zf:
        zf.extractall('/home/s1987119/Diss_data/Final/Humidity/Process/unzippedhumidity/')

#Process check
print('unzipped')

#input directory
direc = ('/home/s1987119/Diss_data/Final/Humidity/Process/unzippedhumidity')
#output directory
newdirec = ('/home/s1987119/Diss_data/Final/Humidity/Process/concat/')

#Remove all files from sub directory to add to joint processing directory
folderlist=glob.glob(direc+'/download*')
for folder in range(len(folderlist)):
    for files in glob.glob(folderlist[folder]+'/*.nc'):
        renamer = files
        os.rename((renamer),newdirec+(renamer)[75:-20]+'.nc')

#Process check
print('renamed')
print(command2)

#List netCDF format files in new directory
for files in glob.glob(newdirec+'/*.nc'):
    #Sense check string slicing for file renaming
    print(str(files)[76:78])
    #Check if file name has expected time information, action if so
    if str(files[76:78]) == '18':
         #Open netCDF
         xds = xr.open_dataset(files)
         #Designate outgoing filename
         filenamer=(str(files[108:125]))+'_'+(str(files)[76:78])
         #Modify time variable values using information gained from title
         ((xds['time'].values[:])[0:32])=((xds['time'].values[:])[0:32])+(10000000000)*360*18
         #Rename main data variable
         xds['relative_humidity'] = xds['Relative_Humidity_2m_18h']
         #Drop old data variable alias
         xds = xds.drop(['Relative_Humidity_2m_18h'])
         #Generate netCDF file with new time and alias
         xds.to_netcdf('/home/s1987119/Diss_data/Final/Humidity/Process/rc/'+filenamer+'.nc')
         #Close current file
         xds.close()
    #Repeat process for all files with similarly designated time and name
    elif str(files[76:78]) == '06':
         xds = xr.open_dataset(files)
         filenamer=(str(files[108:125]))+'_'+(str(files)[76:78])
         ((xds['time'].values[:])[0:32])=((xds['time'].values[:])[0:32])+(10000000000)*360*6
         xds['relative_humidity'] = xds['Relative_Humidity_2m_06h']
         xds = xds.drop(['Relative_Humidity_2m_06h'])
         xds.to_netcdf('/home/s1987119/Diss_data/Final/Humidity/Process/rc/'+filenamer+'.nc')
         xds.close()
    elif str(files[76:78]) == '09':
         xds = xr.open_dataset(files)
         filenamer=(str(files[108:125]))+'_'+(str(files)[76:78])
         ((xds['time'].values[:])[0:32])=((xds['time'].values[:])[0:32])+(10000000000)*360*9
         xds['relative_humidity'] = xds['Relative_Humidity_2m_09h']
         xds = xds.drop(['Relative_Humidity_2m_09h'])
         xds.to_netcdf('/home/s1987119/Diss_data/Final/Humidity/Process/rc/'+filenamer+'.nc')
         xds.close()
    elif str(files[76:78]) == '12':
         xds = xr.open_dataset(files)
         filenamer=(str(files[108:125]))+'_'+(str(files)[76:78])
         ((xds['time'].values[:])[0:32])=((xds['time'].values[:])[0:32])+(10000000000)*360*12
         xds['relative_humidity'] = xds['Relative_Humidity_2m_12h']
         xds = xds.drop(['Relative_Humidity_2m_12h'])
         xds.to_netcdf('/home/s1987119/Diss_data/Final/Humidity/Process/rc/'+filenamer+'.nc')
         xds.close()
    elif str(files[76:78]) == '15':
         xds = xr.open_dataset(files)
         filenamer=(str(files[108:125]))+'_'+(str(files)[76:78])
         ((xds['time'].values[:])[0:32])=((xds['time'].values[:])[0:32])+(10000000000)*360*15
         xds['relative_humidity'] = xds['Relative_Humidity_2m_15h']
         xds = xds.drop(['Relative_Humidity_2m_15h'])
         xds.to_netcdf('/home/s1987119/Diss_data/Final/Humidity/Process/rc/'+filenamer+'.nc')
         xds.close()
    pass

#Process check
print('retimed and renamed')
