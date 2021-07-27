import xarray as xr
import glob
import numpy as np



#Open original file to be regridded
ncfrm = xr.open_dataset('LUC_2019.nc')

#Build new netcdf and make values floats in order for them to be accepted by regrid algorithm
lccsfloat = ncfrm['lccs_class']+0.1
LUC = xr.Dataset({'lccs_class': lccsfloat})
LUC.to_netcdf('LUC_2019rg.nc')

LUC19 = xr.open_dataset('LUC_2019rg.nc') #Open new netCDF with float values

ncto = xr.open_dataset('2004_LUC_clippedWI.nc') #Open netCDF to be commonly gridded to

#Build new netcdf and makes values floats in order for them to be accepted by regrid algorithm
lccsfloat4 = ncto['lccs_class']+0.1
LUC4 = xr.Dataset({'lccs_class': lccsfloat4})
LUC4.to_netcdf('LUC4.nc') # make regridding netCDF

LUC04=  xr.open_dataset('LUC4.nc')

#regrid with reindex_like
reLUC = LUC19.reindex_like(LUC04, method = 'nearest', copy = True, fill_value = -999) # LUC19 will be regridded like L04
reLUC['lccs_class'] = reLUC['lccs_class'] - 0.1 # revert all values to original
reLUC.to_netcdf('/home/s1987119/Diss_data/Final/LUC/Process/regrid/regridded_LUC19.nc') # write regridded netCDF to file
