import netCDF4 as nc
import numpy as np
import xarray as xr
import os
import pandas as pd

'''

Intent

Characterise malaria risk as a factor of diurnal temperature range and  daily mean temperature combination, via their
effect on the reproduction rate of malaria parasites in mosquito blood

Temperature thresholds and diurnal ranges effecting malaria are taken from Paajimans et al, 2009.

Requirements

This code accepts single files and therefore requires that the netCDF are concatenated for the period beforehand.
The acceptable download limit for approximately 7 years of hourly data in a space slightly excess of Uganda coverage.

'''

#Open netCDF data format
da = xr.open_dataset('/home/s1987119/Diss_data/Final/Temperature/Process/temp_2004_2019.nc')

#.t2m suffix gives all new data arrays attributes, dimensions and other specifics of t2m data array of pre-analysis dataset

#Daily resampled summary statistics for temperature following conversion from Kelvin to degrees celsius
daily_mean = (da.resample(time= '1D').reduce(np.mean) - 273.15).t2m
daily_range = (da.resample(time= '1D').reduce(np.max) - da.resample(time= '1D').reduce(np.min)).t2m
daily_std = (da.resample(time= '1D').reduce(np.std)).t2m
daily_min = (da.resample(time= '1D').reduce(np.min) - 273.15).t2m
daily_max = (da.resample(time= '1D').reduce(np.max) - 273.15).t2m

#Monthly resampled summary statistics for temperature following conversion from Kelvin to degrees celsius
monthly_mean = (da.resample(time= '1M').reduce(np.mean) - 273.15).t2m
monthly_range = (da.resample(time= '1M').reduce(np.max) - da.resample(time= '1M').reduce(np.min)).t2m
monthly_std = (da.resample(time= '1M').reduce(np.std)).t2m
monthly_min = (da.resample(time= '1M').reduce(np.min) - 273.15).t2m
monthly_max = (da.resample(time= '1M').reduce(np.max) - 273.15).t2m

#Yearly resampled summary statistics for temperature following conversion from Kelvin to degrees celsius
yearly_mean = (da.resample(time= '1Y').reduce(np.mean) - 273.15).t2m
yearly_range = (da.resample(time= '1Y').reduce(np.max) - da.resample(time= '1Y').reduce(np.min)).t2m
yearly_std = (da.resample(time= '1Y').reduce(np.std)).t2m
yearly_min = (da.resample(time= '1Y').reduce(np.min) - 273.15).t2m
yearly_max = (da.resample(time= '1Y').reduce(np.max) - 273.15).t2m

#Build netCDF dataset for year timestep data arrays
mye = xr.Dataset({'monthly_mean':monthly_mean,'monthly_range':monthly_range,'monthly_std':monthly_std,'monthly_min':monthly_min,'monthly_max':monthly_max})
mye.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/Monthly_temperature.nc')

#Build netCDF dataset for year timestep data arrays
dye = xr.Dataset({'daily_mean':daily_mean,'daily_range':daily_range,'daily_std':daily_std,'daily_min':daily_min,'daily_max':daily_max})
dye.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/Daily_temperature.nc')

#Build netCDF dataset for year timestep data arrays
tye = xr.Dataset({'yearly_mean':yearly_mean,'yearly_range':yearly_range,'yearly_std':yearly_std,'yearly_min':yearly_min,'yearly_max':yearly_max})
tye.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/Yearly_temperature.nc')

#Create variable risktrue to characterise diurnal temperature risk and mean together into post graphical matrix.
#Use daily mean and range in order to characterise this risk per day with criteria checked with "logical and"

#Assign highest risk block
risktrue = xr.where((0 <= daily_range)&(daily_range < 2)&(daily_mean >= 18)&(daily_mean <= 19),1,0)
risktrue = xr.where((2 <= daily_range)&(daily_range <= 10)&(daily_mean < 20)&(daily_mean >= 18), 1, risktrue) #characterise as risktrue to avoid overwrite.
risktrue = xr.where((daily_range > 10)&(daily_mean < 20)&(daily_mean >= 18), 1,risktrue)

#Assign second highest risk block
risktrue = xr.where((daily_mean >= 20)&(daily_mean <= 25)&(daily_range >= 0)&(daily_range <= 6), 0.6, risktrue)
risktrue = xr.where((daily_mean >= 20)&(daily_mean <= 25)&(daily_range >= 0)&(daily_range <= 6), 0.6, risktrue)
risktrue = xr.where((daily_mean >= 20)&(daily_mean < 23)&(daily_range > 10)&(daily_range <= 14), 0.6, risktrue)
risktrue = xr.where((daily_mean >= 20)&(daily_mean <= 22)&(daily_range > 14), 0.6, risktrue)


#Assign third highest risk block
risktrue = xr.where((daily_mean >= 25)&(daily_mean < 27)&(daily_range >= 0)&(daily_range <= 10), 0.1, risktrue)

#Assign net 0 in risk
risktrue = xr.where((daily_mean > 22)&(daily_mean < 23)&(daily_range > 14), 0, risktrue)
risktrue = xr.where((daily_mean >= 23)&(daily_mean < 26)&(daily_range > 10), 0, risktrue)

#Assign negative net risk
risktrue = xr.where((daily_mean >= 27)&(daily_range >= 0)&(daily_range <= 10), -0.3, risktrue)

risktrue = xr.where((daily_mean >= 26)&(daily_range > 10)&(daily_range <= 14), -0.3, risktrue)

risktrue = xr.where((daily_mean >= 26)&(daily_range > 14), -0.5, risktrue)

#Resample daily risk figure to monthly at total and mean.
riskmonthtot = (risktrue.resample(time= '1M').reduce(np.sum))
riskmonthmean = (risktrue.resample(time= '1M').reduce(np.mean))

#Resample daily risk figure to monthly at total and mean.
riskyeartot = (risktrue.resample(time= '1Y').reduce(np.sum))
riskyearmean = (risktrue.resample(time= '1Y').reduce(np.mean))

#Build datasets from data arrays as variables
tmo = xr.Dataset({'Total_monthly_risk': riskmonthtot, 'Mean_monthly_risk':riskmonthmean, 'monthly_max':monthly_max,'monthly_min':monthly_min,'monthly_std':monthly_std,'monthly_range':monthly_range,'monthly_mean':monthly_mean})
tda = xr.Dataset({'daily_mean':daily_mean,'daily_range': daily_range, 'risk_score': risktrue,'daily_mean': daily_mean,'daily_std':daily_std,'daily_min':daily_min,'daily_max':daily_max})
tye = xr.Dataset({'Total_yearly_risk': riskyeartot, 'Mean_yearly_risk': riskyearmean})

#Write to netCDF4
tmo.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_diurnal_temp.nc')
tda.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/daily_diurnal_temp.nc')
tye.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_diurnal_temp.nc')
