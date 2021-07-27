import xarray as xr
import glob
import numpy as np

'''

Intent

Reindexing of list of netCDF files to a common grid and shape, returning files with the same name in a different directory

'''

#netCDF to regrid to opened from source code folder
regridder = xr.open_dataset('regrid.nc')
# Make list of netcdf files, designate native input folder
for file in glob.glob('*.nc'):
    # Open Dataset
    ping = xr.open_dataset(file)
    # 'Nearest' method prescribes old data value to nearest new grid coordinate pair in spatial comparison
    rehum = ping.reindex_like(regridder, method = 'nearest', tolerance= 0.4, copy = True, fill_value = -999)
    # writing to a new file of same name as origin file at different location
    rehum.to_netcdf('/home/s1987119/Diss_data/Final/Humidity/Process/rc/'+file)
     # Close origin file after process iteration complete
    ping.close()
