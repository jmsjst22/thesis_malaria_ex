import xarray as xr
import glob
import numpy as np

'''

Intent

Characterisation of humidity risk at day, month and year temporal resolution.
Summaries of relative humidity in literature-based thresholds, with single layer characterising all humidity risk.
Summary statistics on daily, yearly and monthly trends are also collected.

Requirements

Fully processed single humidity netCDF file, with all previous manualled processing steps completed.
All indices and statistics are downsampled and mostly kept in no more than 3 files, meaning that this analysis will
require less than a quarter of the output storage of the original files

'''

#Open single netCDF file
hmd = xr.open_dataset('/home/s1987119/Diss_data/Final/Humidity/Process/humidity_all.nc')

#Summary statistics resampled for daily data for mean, range and standard deviation of relative humidity.
daily_mean = (hmd.resample(time= '1D').reduce(np.mean).relative_humidity)
daily_std = (hmd.resample(time= '1D').reduce(np.std).relative_humidity)
daily_range = (hmd.resample(time= '1D').reduce(np.max) - hmd.resample(time= '1D').reduce(np.min)).relative_humidity
daily_min = (hmd.resample(time= '1D').reduce(np.min)).relative_humidity

#Summary statistics resampled for monthly data for mean, range and standard deviation of relative humidity.
monthly_mean = (hmd.resample(time= '1M').reduce(np.mean).relative_humidity)
monthly_std = (hmd.resample(time= '1M').reduce(np.std).relative_humidity)
monthly_range = (hmd.resample(time= '1M').reduce(np.max) - hmd.resample(time= '1M').reduce(np.min)).relative_humidity

#Summary statistics for resampled yearly relative humidity with mean, standard deviation, maximum, minimum and range
yearly_mean = (hmd.resample(time= '1Y').reduce(np.mean).relative_humidity)
yearly_std = (hmd.resample(time= '1Y').reduce(np.std).relative_humidity)
yearly_max = (hmd.resample(time= '1Y').reduce(np.max).relative_humidity)
yearly_min = (hmd.resample(time= '1Y').reduce(np.min).relative_humidity)
yearly_range = (hmd.resample(time= '1Y').reduce(np.max) - hmd.resample(time= '1Y').reduce(np.min)).relative_humidity

#Build netCDF for yearly statistics in relative humidity.
yearly_stats = xr.Dataset({'yearly_mean':yearly_mean,'yearly_std':yearly_std,'yearly_max':yearly_max,'yearly_min':yearly_min, 'yearly_range': yearly_range})
yearly_stats.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/humidity_yearly.nc')

#Characterise humidity risk bands at monthly temporal resolution. Characteristic daily variation would soften trends and therefore risk differentiation.
hmdrisk = xr.where((monthly_mean>=0)&(monthly_mean<10),0,0)
hmdrisk = xr.where((monthly_mean>=10)&(monthly_mean<20),0.25,hmdrisk)
hmdrisk = xr.where((monthly_mean>=20)&(monthly_mean<40),0.5,hmdrisk)
hmdrisk = xr.where((monthly_mean>=40)&(monthly_mean<60),0.75,hmdrisk)
hmdrisk = xr.where((monthly_mean>=60)&(monthly_mean<=100),1,hmdrisk)


#Characterise daily risk above major threshold of 100 % risk and declining risk thereafter
hmhighmean = xr.where((daily_mean>=60)&(daily_mean<=100),int(1),int(0))
hmlowmean = xr.where((daily_mean>=60)&(daily_mean<=100),0,1)

hmhighmin = xr.where((daily_min>=60)&(daily_min<=100),int(1),int(0))
hmlowmin = xr.where((daily_min>=60)&(daily_min<=100),0,1)

#Summarise risk as featured by binary test into monthly resolution.
hmhighmean = (hmhighmean.resample(time= '1M').reduce(np.sum))
hmlowmean = (hmlowmean.resample(time= '1M').reduce(np.sum))

hmhighmin = (hmhighmin.resample(time= '1M').reduce(np.sum))
hmlowmin = (hmlowmin.resample(time= '1M').reduce(np.sum))

hmhighmeany = (hmhighmean.resample(time= '1Y').reduce(np.sum))
hmlowmeany = (hmlowmean.resample(time= '1Y').reduce(np.sum))

hmhighminy = (hmhighmin.resample(time= '1Y').reduce(np.sum))
hmlowminy = (hmlowmin.resample(time= '1Y').reduce(np.sum))

#Build netCDF at daily resolution risk
humday = xr.Dataset({'Daily_mean_hum': daily_mean, 'Daily_standard_dev_hum': daily_std, 'Daily_range_hum': daily_range})
humday.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/humidity_daily.nc')

yearly_stats = xr.Dataset({'yearly_mean':yearly_mean,'yearly_std':yearly_std,'yearly_max':yearly_max,'yearly_min':yearly_min, 'yearly_range': yearly_range, 'high_days_mean': hmhighmeany, 'high_days_min': hmhighminy, 'low_days_mean': hmlowmeany, 'low_days_min':hmlowminy})
yearly_stats.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/humidity_yearly.nc')

#Build netCDF at monthly resolution risk
hummonth = xr.Dataset({'Monthly_mean_hum':monthly_mean,'Monthly_Standard_deviation_hum':monthly_std,'Humidity_risk':hmdrisk,
                      'mean_Hum_High_risk_days':hmhighmean,'mean_Hum_lower_risk_days':hmlowmean, 'min_Hum_High_risk_days':hmhighmin,'min_Hum_lower_risk_days':hmlowmin, 'Monthly_range':monthly_range})
hummonth.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/humidity_monthly.nc')
