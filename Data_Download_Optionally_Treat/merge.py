import argparse
import xarray as xr

'''

Intent

Merge either precipitation or temperature data based on selection.

Requires exactly 100% more storage than original. A clause can be added to the code
to optionally delete original files post merge to spare storage.

Requires all files to be in netCDF and have same identical spatial dimensions.
This requirement is met only by precipitation and temperature data because of
their identical grids and manual- spatial specific download method.

'''

dirprec = '/home/s1987119/Diss_data/Final/Precipitation/Raw_Data/'
dirtem ='/home/s1987119/Diss_data/Final/Temperature/Raw_Data/'


def comparse():
    '''
    Function to enable command line arguments in order to specify data variable desired.
    '''
    # Short description of module
    prs = argparse.ArgumentParser(description=("Module merging optionally temperature or precipitation netCDF, adapt for period and filename only."))
    # command line argument which can be optionally added to control logical flow to precipitation, script defaults at temperature
    prs.add_argument("--prec", dest="prec", type=bool, default=False, help="Defines the dataset which to merge")
    #Assign to a variable that can be used in other functions
    cmdargs = prs.parse_args()
    return cmdargs

#Initiate comparse argument parsing function
cm = comparse()

#Designate if precipitation is true and therefore the required dataset
if cm.prec == True:
    #Open netCDF dataset
    prec4 = xr.open_dataset(dirprec+'tot_prec_04_14_clipped.nc')
    prec14 = xr.open_dataset(dirprec+'tot_prec_15_20_clipped.nc')
    #Concatenate datasets covering area of interest, can be modified to accept any, but only two
    concat = xr.concat([prec4,prec14], dim='time')
    #Build netCDF from concatenated datasets
    concat.to_netcdf('/home/s1987119/Diss_data/Final/Precipitation/Process/precip_2004_2019.nc')
else:
    #Process same for temperature
    temp4 = xr.open_dataset(dirtem+'2m_temp_04_14.nc')
    temp14 = xr.open_dataset(dirtem+'2m_temp_15_21.nc')
    concat = xr.concat([temp4,temp14], dim='time')
    concat.to_netcdf('/home/s1987119/Diss_data/Final/Temperature/Process/temp_2004_2019.nc')
pass
