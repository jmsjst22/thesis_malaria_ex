import netCDF4 as nc
import numpy as np
import xarray as xr
import os
import argparse
import pandas as pd

'''

Intent

Characterises different facets of malaria between daily peak, minimum and maximum with straight line formulae for lines
from the first to the second two, respectively (generated automatically using excel or scipy).

The peak, minimum and maximum temperature values are from Villena et al's (2020) literature review
on known temperature features for mosquito developement, bite rate, fertility, maturation, competence
as a vector and survival rate.

Major output is risk relative to each of these temperature features.

Requirement

Takes single netCDF file with temperature in Kelvin, conversion can be removed.
At least resampled 7 layers are made requiring storage of at least 50 percent of the original file in addition.

'''

#Open dataset
da = xr.open_dataset('/home/s1987119/Diss_data/Final/Temperature/Process/temp_2004_2019.nc')

#Resample hourly to daily with summary statistics and conversion from Kelvin to degrees celsius
daily_mean = (da.resample(time= '1D').reduce(np.mean) - 273.15).t2m
daily_min = (da.resample(time= '1D').reduce(np.min) - 273.15).t2m
daily_max = (da.resample(time= '1D').reduce(np.max) - 273.15).t2m
daily_median = (da.resample(time= '1D').reduce(np.median) - 273.15).t2m

# Characterise mosquito development minimum to peak with regression from peak
mosdevmin_min = xr.where((daily_min >= 13.85)&(daily_min <= 29),(0.066*(daily_min) -0.9142),0)
mosdevmax_min = xr.where((daily_max >= 13.85)&(daily_max <= 29),(0.066*(daily_max) -0.9142),0)
mosdevmedian_min = xr.where((daily_median >= 13.85)&(daily_median <= 29),(0.066*(daily_median) -0.9142),0)
mosdevmean_min = xr.where((daily_mean >= 13.85)&(daily_mean <= 29),(0.066*(daily_mean) -0.9142),0)

print(mosdevmin_min)

#Characterise mosquito development maximum to peak
mosdevmin_max = xr.where((daily_min >= 29)&(daily_min <= 35.95),(-0.1439*(daily_min) + 5.1727),0)
mosdevmax_max = xr.where((daily_max >= 29)&(daily_max <= 35.95),(-0.1439*(daily_max) + 5.1727),0)
mosdevmedian_max = xr.where((daily_median >= 29)&(daily_median <= 35.95),(-0.1439*(daily_median) + 5.1727),0)
mosdevmean_max = xr.where((daily_mean >= 29)&(daily_mean <= 35.95),(-0.1439*(daily_mean) + 5.1727),0)

#Sum mosquito development minimum, peak and peak maximum to normalised indicator of 0 to 1.
mosdevminsum = mosdevmin_min+ mosdevmin_max
mosdevmaxsum = mosdevmax_min+mosdevmax_max
mosdevmediansum = mosdevmedian_min+mosdevmedian_max
mosdevmeansum = mosdevmean_min+mosdevmean_max



#Build netCDF with summarised mosquito development risk indicators for daily
mosdev = xr.Dataset({'Mos_dev_daily_minimum': mosdevminsum, 'Mos_dev_daily_maximum':mosdevmaxsum,'Mos_dev_daily_median':mosdevmediansum,'Mos_dev_daily_mean':mosdevmeansum})
mosdev.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/mosdev_transmiss.nc')



#Monthly mean and sum resampling of mosquito development risk
monthly_m_mosdevminsum = (mosdevminsum.resample(time= '1M').reduce(np.mean))
monthly_m_mosdevmaxsum = (mosdevmaxsum.resample(time= '1M').reduce(np.mean))
monthly_m_mosdevmediansum = (mosdevmediansum.resample(time= '1M').reduce(np.mean))
monthly_m_mosdevmeansum = (mosdevmeansum.resample(time= '1M').reduce(np.mean))

monthly_s_mosdevminsum = (mosdevminsum.resample(time= '1M').reduce(np.sum))
monthly_s_mosdevmaxsum = (mosdevmaxsum.resample(time= '1M').reduce(np.sum))
monthly_s_mosdevmediansum = (mosdevmediansum.resample(time= '1M').reduce(np.sum))
monthly_s_mosdevmeansum = (mosdevmeansum.resample(time= '1M').reduce(np.sum))

#Build netCDF for monthly resampled risk for mosquito development
month_mosdev = xr.Dataset({'Mos_dev_monthly_minimum_s': monthly_s_mosdevminsum, 'Mos_dev_monthly_maximum_s': monthly_s_mosdevmaxsum,
                            'Mos_dev_monthly_median_s': monthly_s_mosdevmediansum, 'Mos_dev_monthly_mean_s': monthly_s_mosdevmeansum,
                            'Mos_dev_monthly_minimum_m': monthly_m_mosdevminsum, 'Mos_dev_monthly_maximum_m': monthly_m_mosdevmaxsum,
                            'Mos_dev_monthly_median_m': monthly_m_mosdevmediansum, 'Mos_dev_monthly_mean_m': monthly_m_mosdevmeansum})

month_mosdev.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_mosdev_transmiss.nc')

#Yearly mean and sum resampling of mosquito development risk
yearly_m_mosdevminsum = (mosdevminsum.resample(time= '1Y').reduce(np.mean))
yearly_m_mosdevmaxsum = (mosdevmaxsum.resample(time= '1Y').reduce(np.mean))
yearly_m_mosdevmediansum = (mosdevmediansum.resample(time= '1Y').reduce(np.mean))
yearly_m_mosdevmeansum = (mosdevmeansum.resample(time= '1Y').reduce(np.mean))

yearly_s_mosdevminsum = (mosdevminsum.resample(time= '1Y').reduce(np.sum))
yearly_s_mosdevmaxsum = (mosdevmaxsum.resample(time= '1Y').reduce(np.sum))
yearly_s_mosdevmediansum = (mosdevmediansum.resample(time= '1Y').reduce(np.sum))
yearly_s_mosdevmeansum = (mosdevmeansum.resample(time= '1Y').reduce(np.sum))

#Build netCDF for yearly resampled risk for mosquito development
year_mosdev = xr.Dataset({'Mos_dev_yearly_minimum_s': yearly_s_mosdevminsum, 'Mos_dev_yearly_maximum_s': yearly_s_mosdevmaxsum,
                            'Mos_dev_yearly_median_s': yearly_s_mosdevmediansum, 'Mos_dev_yearly_mean_s': yearly_s_mosdevmeansum,
                            'Mos_dev_yearly_minimum_m': yearly_m_mosdevminsum, 'Mos_dev_yearly_maximum_m': yearly_m_mosdevmaxsum,
                            'Mos_dev_yearly_median_m': yearly_m_mosdevmediansum, 'Mos_dev_yearly_mean_m': yearly_m_mosdevmeansum})

year_mosdev.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_mosdev_transmiss.nc')

'''
# Characterise bite rate risk minimum to peak with regression from peak
biteratemin_min = xr.where((daily_min >= 16.95)&(daily_min <= 34.6),(0.0567*(daily_min) -0.9603),0)
biteratemax_min = xr.where((daily_max >= 16.95)&(daily_max <= 34.6),(0.0567*(daily_max) -0.9603),0)
biteratemedian_min = xr.where((daily_median >= 16.95)&(daily_median <= 34.6),(0.0567*(daily_median) -0.9603),0)
biteratemean_min = xr.where((daily_mean >= 16.95)&(daily_mean <= 34.6),(0.0567*(daily_mean) -0.9603),0)

# Characterise bite rate risk peak to maximum with regression from peak
biteratemin_max = xr.where((daily_min >= 34.6)&(daily_min <= 43.55),(-0.1117*(daily_min) + 4.8659),0)
biteratemax_max = xr.where((daily_max >= 34.6)&(daily_max <= 43.55),(-0.1117*(daily_max) + 4.8659),0)
biteratemedian_max = xr.where((daily_median >= 34.6)&(daily_median <= 43.55),(-0.1117*(daily_median) + 4.8659),0)
biteratemean_max = xr.where((daily_mean >= 34.6)&(daily_mean <= 43.55),(-0.1117*(daily_mean) + 4.8659),0)

#Sum bite rate minimum, peak and peak maximum to normalised indicator of 0 to 1.
biterateminsum = biteratemin_min+biteratemin_max
biteratemaxsum = biteratemax_max+biteratemax_min
biteratemediansum = biteratemedian_min+biteratemedian_max
biteratemeansum = biteratemean_min+biteratemean_max

#Build netCDF with summarised bite rate risk indicators for daily diurnal range and mean
biterate = xr.Dataset({'Biterate_daily_minimum': biterateminsum, 'Biterate_daily_maximum':biteratemaxsum,'Biterate_daily_median':biteratemediansum,'Biterate_daily_mean':biteratemeansum})
biterate.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/biterate_transmiss.nc')

#Monthly mean and sum resampling of bite rate risk
monthly_m_biterateminsum = (biterateminsum.resample(time= '1M').reduce(np.mean))
monthly_m_biteratemaxsum = (biteratemaxsum.resample(time= '1M').reduce(np.mean))
monthly_m_biteratemediansum = (biteratemediansum.resample(time= '1M').reduce(np.mean))
monthly_m_biteratemeansum = (biteratemeansum.resample(time= '1M').reduce(np.mean))

monthly_s_biterateminsum = (biterateminsum.resample(time= '1M').reduce(np.sum))
monthly_s_biteratemaxsum = (biteratemaxsum.resample(time= '1M').reduce(np.sum))
monthly_s_biteratemediansum = (biteratemediansum.resample(time= '1M').reduce(np.sum))
monthly_s_biteratemeansum = (biteratemeansum.resample(time= '1M').reduce(np.sum))


#Build netCDF for monthly resampled risk for bite rate
month_biterate = xr.Dataset({'biterate_monthly_minimum_s': monthly_s_biterateminsum, 'biterate_monthly_maximum_s': monthly_s_biteratemaxsum,
                            'biterate_monthly_median_s': monthly_s_biteratemediansum, 'biterate_monthly_mean_s': monthly_s_biteratemeansum,
                            'biterate_monthly_minimum_m': monthly_m_biterateminsum, 'biterate_monthly_maximum_m': monthly_m_biteratemaxsum,
                            'biterate_monthly_median_m': monthly_m_biteratemediansum, 'biterate_monthly_mean_m': monthly_m_biteratemeansum})

month_biterate.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_biterate_transmiss.nc')

#Yearly mean and sum resampling of bite rate risk
yearly_m_biterateminsum = (biterateminsum.resample(time= '1Y').reduce(np.mean))
yearly_m_biteratemaxsum = (biteratemaxsum.resample(time= '1Y').reduce(np.mean))
yearly_m_biteratemediansum = (biteratemediansum.resample(time= '1Y').reduce(np.mean))
yearly_m_biteratemeansum = (biteratemeansum.resample(time= '1Y').reduce(np.mean))

yearly_s_biterateminsum = (biterateminsum.resample(time= '1Y').reduce(np.sum))
yearly_s_biteratemaxsum = (biteratemaxsum.resample(time= '1Y').reduce(np.sum))
yearly_s_biteratemediansum = (biteratemediansum.resample(time= '1Y').reduce(np.sum))
yearly_s_biteratemeansum = (biteratemeansum.resample(time= '1Y').reduce(np.sum))

#Build netCDF for yearly resampled risk for biterate
year_biterate = xr.Dataset({'biterate_yearly_minimum_s': yearly_s_biterateminsum, 'biterate_yearly_maximum_s': yearly_s_biteratemaxsum,
                            'biterate_yearly_median_s': yearly_s_biteratemediansum, 'biterate_yearly_mean_s': yearly_s_biteratemeansum,
                            'biterate_yearly_minimum_m': yearly_m_biterateminsum, 'biterate_yearly_maximum_m': yearly_m_biteratemaxsum,
                            'biterate_yearly_median_m': yearly_m_biteratemediansum, 'biterate_yearly_mean_m': yearly_m_biteratemeansum})

year_biterate.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_biterate_transmiss.nc')

# Characterise fertility minimum to peak with regression from peak
egfemin_min = xr.where((daily_min >= 15.30)&(daily_min <= 25.9),(0.0943*(daily_min) -1.4434),0)
egfemax_min = xr.where((daily_max >= 15.30)&(daily_max <= 25.9),(0.0943*(daily_max) -1.4434),0)
egfemedian_min = xr.where((daily_median >= 15.30)&(daily_median <= 25.9),(0.0943*(daily_median) -1.4434),0)
egfemean_min = xr.where((daily_mean >= 15.30)&(daily_mean <= 25.9),(0.0943*(daily_mean) -1.4434),0)


# Characterise fertility peak to maximum with regression from peak
egfemin_max = xr.where((daily_min >= 25.9)&(daily_min <= 32.70),(-0.1471*(daily_min) +4.8088),0)
egfemax_max = xr.where((daily_max >= 25.9)&(daily_max <= 32.70),(-0.1471*(daily_max) +4.8088),0)
egfemedian_max = xr.where((daily_median >= 25.9)&(daily_median <= 32.70),(-0.1471*(daily_median) +4.8088),0)
egfemean_max = xr.where((daily_mean >= 25.9)&(daily_mean <= 32.70),(-0.1471*(daily_mean) +4.8088),0)

#Sum fertility minimum, peak and peak maximum to normalised indicator of 0 to 1.
egfeminsum = egfemin_min+egfemin_max
egfemaxsum = egfemax_max+egfemax_min
egfemediansum = egfemedian_min+egfemedian_max
egfemeansum = egfemean_min+egfemean_max

#Build netCDF with summarised fertility risk indicators for daily diurnal range and mean
egfe = xr.Dataset({'Eggsp_fe_daily_minimum': egfeminsum, 'Eggsp_fe_daily_maximum':egfemaxsum,'Eggsp_fe_daily_median':egfemediansum,'Eggsp_fe_daily_mean':egfemeansum})
egfe.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/egfe_transmiss.nc')

#Monthly mean and sum resampling of mosquito fertility risk
monthly_m_egfeminsum = (egfeminsum.resample(time= '1M').reduce(np.mean))
monthly_m_egfemaxsum = (egfemaxsum.resample(time= '1M').reduce(np.mean))
monthly_m_egfemediansum = (egfemediansum.resample(time= '1M').reduce(np.mean))
monthly_m_egfemeansum = (egfemeansum.resample(time= '1M').reduce(np.mean))

monthly_s_egfeminsum = (egfeminsum.resample(time= '1M').reduce(np.sum))
monthly_s_egfemaxsum = (egfemaxsum.resample(time= '1M').reduce(np.sum))
monthly_s_egfemediansum = (egfemediansum.resample(time= '1M').reduce(np.sum))
monthly_s_egfemeansum = (egfemeansum.resample(time= '1M').reduce(np.sum))

#Build netCDF for monthly resampled risk for mosquito fertility
month_egfe = xr.Dataset({'egfe_monthly_minimum_s': monthly_s_egfeminsum, 'egfe_monthly_maximum_s': monthly_s_egfemaxsum,
                            'egfe_monthly_median_s': monthly_s_egfemediansum, 'egfe_monthly_mean_s': monthly_s_egfemeansum,
                            'egfe_monthly_minimum_m': monthly_m_egfeminsum, 'egfe_monthly_maximum_m': monthly_m_egfemaxsum,
                            'egfe_monthly_median_m': monthly_m_egfemediansum, 'egfe_monthly_mean_m': monthly_m_egfemeansum})

month_egfe.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_egfe_transmiss.nc')

#Yearly mean and sum resampling of mosquito fertility risk
yearly_m_egfeminsum = (egfeminsum.resample(time= '1Y').reduce(np.mean))
yearly_m_egfemaxsum = (egfemaxsum.resample(time= '1Y').reduce(np.mean))
yearly_m_egfemediansum = (egfemediansum.resample(time= '1Y').reduce(np.mean))
yearly_m_egfemeansum = (egfemeansum.resample(time= '1Y').reduce(np.mean))

yearly_s_egfeminsum = (egfeminsum.resample(time= '1Y').reduce(np.sum))
yearly_s_egfemaxsum = (egfemaxsum.resample(time= '1Y').reduce(np.sum))
yearly_s_egfemediansum = (egfemediansum.resample(time= '1Y').reduce(np.sum))
yearly_s_egfemeansum = (egfemeansum.resample(time= '1Y').reduce(np.sum))

#Yearly mean and sum resampling of mosquito fertility risk
year_egfe = xr.Dataset({'egfe_yearly_minimum_s': yearly_s_egfeminsum, 'egfe_yearly_maximum_s': yearly_s_egfemaxsum,
                            'egfe_yearly_median_s': yearly_s_egfemediansum, 'egfe_yearly_mean_s': yearly_s_egfemeansum,
                            'egfe_yearly_minimum_m': yearly_m_egfeminsum, 'egfe_yearly_maximum_m': yearly_m_egfemaxsum,
                            'egfe_yearly_median_m': yearly_m_egfemediansum, 'egfe_yearly_mean_m': yearly_m_egfemeansum})

year_egfe.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_egfe_transmiss.nc')

# Characterise egg to adult conversion minimum to peak with regression from peak
egamin_min = xr.where((daily_min >= 16.65)&(daily_min <= 24.80),(0.1227*(daily_min)-2.0429),0)
egamax_min = xr.where((daily_max >= 16.65)&(daily_max <= 24.80),(0.1227*(daily_max) -2.0429),0)
egamedian_min = xr.where((daily_median >= 16.65)&(daily_median <= 24.80),(0.1227*(daily_median) -2.0429),0)
egamean_min = xr.where((daily_mean >= 16.65)&(daily_mean <= 24.80),(0.1227*(daily_mean) -2.0429),0)

# Characterise mosquito mortality peak to maximum with regression from peak
egamin_max = xr.where((daily_min >= 24.80)&(daily_min <= 32.7),(-0.1266*(daily_min)+4.1392),0)
egamax_max = xr.where((daily_max >= 24.80)&(daily_max <= 32.7),(-0.1266*(daily_max)+4.1392),0)
egamedian_max = xr.where((daily_median >= 24.80)&(daily_median <= 32.7),(-0.1266*(daily_median)+4.1392),0)
egamean_max = xr.where((daily_mean >= 24.80)&(daily_mean <= 32.7),(-0.1266*(daily_mean)+4.1392),0)

#Sum mosquito eggs to adult conversion risk, peak and peak maximum to normalised indicator of 0 to 1.
egaminsum = egamin_min+egamin_max
egamaxsum = egamax_max+egamax_min
egamediansum = egamedian_min+egamedian_max
egameansum = egamean_min+egamean_max

#Build netCDF with summarised egg to adult conversion risk indicators for daily diurnal range and mean
ega = xr.Dataset({'Egg_to_ad_daily_minimum': egaminsum, 'Egg_to_ad_daily_maximum':egamaxsum,'Egg_to_ad_daily_median':egamediansum,'Egg_to_ad_daily_mean':egameansum})
ega.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/ega_transmiss.nc')

#Monthly mean and sum resampling of mosquito eggs to adult conversion risk
monthly_m_egaminsum = (egaminsum.resample(time= '1M').reduce(np.mean))
monthly_m_egamaxsum = (egamaxsum.resample(time= '1M').reduce(np.mean))
monthly_m_egamediansum = (egamediansum.resample(time= '1M').reduce(np.mean))
monthly_m_egameansum = (egameansum.resample(time= '1M').reduce(np.mean))

monthly_s_egaminsum = (egaminsum.resample(time= '1M').reduce(np.sum))
monthly_s_egamaxsum = (egamaxsum.resample(time= '1M').reduce(np.sum))
monthly_s_egamediansum = (egamediansum.resample(time= '1M').reduce(np.sum))
monthly_s_egameansum = (egameansum.resample(time= '1M').reduce(np.sum))


#Build netCDF for monthly resampled risk for mosquito eggs to adult conversion risk
month_ega = xr.Dataset({'ega_monthly_minimum_s': monthly_s_egaminsum, 'ega_monthly_maximum_s': monthly_s_egamaxsum,
                            'ega_monthly_median_s': monthly_s_egamediansum, 'ega_monthly_mean_s': monthly_s_egameansum,
                            'ega_monthly_minimum_m': monthly_m_egaminsum, 'ega_monthly_maximum_m': monthly_m_egamaxsum,
                            'ega_monthly_median_m': monthly_m_egamediansum, 'ega_monthly_mean_m': monthly_m_egameansum})

month_ega.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_ega_transmiss.nc')

#Yearly mean and sum resampling of mosquito eggs to adult conversion risk
yearly_m_egaminsum = (egaminsum.resample(time= '1Y').reduce(np.mean))
yearly_m_egamaxsum = (egamaxsum.resample(time= '1Y').reduce(np.mean))
yearly_m_egamediansum = (egamediansum.resample(time= '1Y').reduce(np.mean))
yearly_m_egameansum = (egameansum.resample(time= '1Y').reduce(np.mean))

yearly_s_egaminsum = (egaminsum.resample(time= '1Y').reduce(np.sum))
yearly_s_egamaxsum = (egamaxsum.resample(time= '1Y').reduce(np.sum))
yearly_s_egamediansum = (egamediansum.resample(time= '1Y').reduce(np.sum))
yearly_s_egameansum = (egameansum.resample(time= '1Y').reduce(np.sum))

#Build netCDF for yearly resampled risk for mosquito eggs to adult conversion risk
year_ega = xr.Dataset({'ega_yearly_minimum_s': yearly_s_egaminsum, 'ega_yearly_maximum_s': yearly_s_egamaxsum,
                            'ega_yearly_median_s': yearly_s_egamediansum, 'ega_yearly_mean_s': yearly_s_egameansum,
                            'ega_yearly_minimum_m': yearly_m_egaminsum, 'ega_yearly_maximum_m': yearly_m_egamaxsum,
                            'ega_yearly_median_m': yearly_m_egamediansum, 'ega_yearly_mean_m': yearly_m_egameansum})

year_ega.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_ega_transmiss.nc')

# Characterise mosquito mortality minimum to peak with regression from peak
mormin_min = xr.where((daily_min >= 8.45)&(daily_min <= 22.30),(0.0722*(daily_min)-0.6101),0)
mormax_min = xr.where((daily_max >= 8.45)&(daily_max <= 22.30),(-0.1266*(daily_max)-0.6101),0)
mormedian_min = xr.where((daily_median >= 8.45)&(daily_median <= 22.30),(-0.1266*(daily_median)-0.6101),0)
mormean_min = xr.where((daily_mean >= 8.45)&(daily_mean <= 22.30),(-0.1266*(daily_mean)-0.6101),0)

# Characterise mosquito mortality maximum to peak with regression from peak
mormin_max = xr.where((daily_min >= 22.30)&(daily_min <= 38.85),(-0.0604*(daily_min)+2.3474),0)
mormax_max = xr.where((daily_max >= 22.30)&(daily_max <= 38.85),(-0.0604*(daily_max)+2.3474),0)
mormedian_max = xr.where((daily_median >= 22.30)&(daily_median <= 38.85),(-0.0604*(daily_median)+2.3474),0)
mormean_max = xr.where((daily_mean >= 22.30)&(daily_mean <= 38.85),(-0.0604*(daily_mean)+2.3474),0)

#Sum mortality minimum, peak and peak, maximum risk to normalised indicator of 0 to 1.
morminsum = mormin_min+mormin_max
mormaxsum = mormax_max+mormin_min
mormediansum = mormedian_min+mormedian_max
mormeansum = mormean_min+mormean_max

#Build netCDF with summarised mosquito mortality risk indicators for daily diurnal range and mean
mor = xr.Dataset({'Mortality_daily_minimum': morminsum, 'Mortality_daily_maximum':mormaxsum,'Mortality_daily_median':mormediansum,'Mortality_daily_mean':mormeansum})
mor.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/mor_transmiss.nc')

#Monthly mean and sum resampling of mosquito mortality risk
monthly_m_morminsum = (morminsum.resample(time= '1M').reduce(np.mean))
monthly_m_mormaxsum = (mormaxsum.resample(time= '1M').reduce(np.mean))
monthly_m_mormediansum = (mormediansum.resample(time= '1M').reduce(np.mean))
monthly_m_mormeansum = (mormeansum.resample(time= '1M').reduce(np.mean))

monthly_s_morminsum = (morminsum.resample(time= '1M').reduce(np.sum))
monthly_s_mormaxsum = (mormaxsum.resample(time= '1M').reduce(np.sum))
monthly_s_mormediansum = (mormediansum.resample(time= '1M').reduce(np.sum))
monthly_s_mormeansum = (mormeansum.resample(time= '1M').reduce(np.sum))

#Build netCDF for monthly resampled risk for mosquito mortality risk
month_mor = xr.Dataset({'mor_monthly_minimum_s': monthly_s_morminsum, 'mor_monthly_maximum_s': monthly_s_mormaxsum,
                            'mor_monthly_median_s': monthly_s_mormediansum, 'mor_monthly_mean_s': monthly_s_mormeansum,
                            'mor_monthly_minimum_m': monthly_m_morminsum, 'mor_monthly_maximum_m': monthly_m_mormaxsum,
                            'mor_monthly_median_m': monthly_m_mormediansum, 'mor_monthly_mean_m': monthly_m_mormeansum})

month_mor.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_mor_transmiss.nc')

#Yearly mean and sum resampling of mosquito mortality risk
yearly_m_morminsum = (morminsum.resample(time= '1Y').reduce(np.mean))
yearly_m_mormaxsum = (mormaxsum.resample(time= '1Y').reduce(np.mean))
yearly_m_mormediansum = (mormediansum.resample(time= '1Y').reduce(np.mean))
yearly_m_mormeansum = (mormeansum.resample(time= '1Y').reduce(np.mean))

yearly_s_morminsum = (morminsum.resample(time= '1Y').reduce(np.sum))
yearly_s_mormaxsum = (mormaxsum.resample(time= '1Y').reduce(np.sum))
yearly_s_mormediansum = (mormediansum.resample(time= '1Y').reduce(np.sum))
yearly_s_mormeansum = (mormeansum.resample(time= '1Y').reduce(np.sum))

#Build netCDF for yearly resampled risk for mosquito mortality risk
year_mor = xr.Dataset({'mor_yearly_minimum_s': yearly_s_morminsum, 'mor_yearly_maximum_s': yearly_s_mormaxsum,
                            'mor_yearly_median_s': yearly_s_mormediansum, 'mor_yearly_mean_s': yearly_s_mormeansum,
                            'mor_yearly_minimum_m': yearly_m_morminsum, 'mor_yearly_maximum_m': yearly_m_mormaxsum,
                            'mor_yearly_median_m': yearly_m_mormediansum, 'mor_yearly_mean_m': yearly_m_mormeansum})

year_mor.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_mor_transmiss.nc')

# Characterise vector competence minimum to peak with regression from peak
vecmin_min = xr.where((daily_min >= 9.45)&(daily_min <= 24),(0.0687*(daily_min)-0.6495),0)
vecmax_min = xr.where((daily_max >= 9.45)&(daily_max <= 24),(0.0687*(daily_max)-0.6495),0)
vecmedian_min = xr.where((daily_median >= 9.45)&(daily_median <= 24),(0.0687*(daily_median)-0.6495),0)
vecmean_min = xr.where((daily_mean >= 9.45)&(daily_mean <= 24),(0.0687*(daily_mean)-0.6495),0)

# Characterise vector competence peak to maximum with regression from peak
vecmin_max = xr.where((daily_min >= 24)&(daily_min <= 36.15),(-0.0823*(daily_min)+2.9753),0)
vecmax_max = xr.where((daily_max >= 24)&(daily_max <= 36.15),(-0.0823*(daily_max)+2.9753),0)
vecmedian_max = xr.where((daily_median >= 24)&(daily_median <= 36.15),(-0.0823*(daily_median)+2.9753),0)
vecmean_max = xr.where((daily_mean >= 24)&(daily_mean <= 36.15),(-0.0823*(daily_mean)+2.9753),0)

#Sum vector competence minimum, peak and peak, maximum risk to normalised indicator of 0 to 1.
vecminsum = vecmin_min+vecmin_max
vecmaxsum = vecmax_max+vecmax_min
vecmediansum = vecmedian_min+vecmedian_max
vecmeansum = vecmean_min+vecmean_max

#Build netCDF with summarised mosquito vector competence risk indicators for daily diurnal range and mean
vec = xr.Dataset({'Vect_Comp_daily_minimum': vecminsum, 'Vector_comp_daily_maximum':vecmaxsum,'Vector_comp_daily_median':vecmediansum,'Vec_comp_daily_mean':vecmeansum})
vec.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/vec_transmiss.nc')

#Monthly mean and sum resampling of mosquito vector competence risk
monthly_m_vecminsum = (vecminsum.resample(time= '1M').reduce(np.mean))
monthly_m_vecmaxsum = (vecmaxsum.resample(time= '1M').reduce(np.mean))
monthly_m_vecmediansum = (vecmediansum.resample(time= '1M').reduce(np.mean))
monthly_m_vecmeansum = (vecmeansum.resample(time= '1M').reduce(np.mean))

monthly_s_vecminsum = (vecminsum.resample(time= '1M').reduce(np.sum))
monthly_s_vecmaxsum = (vecmaxsum.resample(time= '1M').reduce(np.sum))
monthly_s_vecmediansum = (vecmediansum.resample(time= '1M').reduce(np.sum))
monthly_s_vecmeansum = (vecmeansum.resample(time= '1M').reduce(np.sum))

#Build netCDF for monthly resampled risk for mosquito vector competence risk
month_vec = xr.Dataset({'vec_monthly_minimum_s': monthly_s_vecminsum, 'vec_monthly_maximum_s': monthly_s_vecmaxsum,
                            'vec_monthly_median_s': monthly_s_vecmediansum, 'vec_monthly_mean_s': monthly_s_vecmeansum,
                            'vec_monthly_minimum_m': monthly_m_vecminsum, 'vec_monthly_maximum_m': monthly_m_vecmaxsum,
                            'vec_monthly_median_m': monthly_m_vecmediansum, 'vec_monthly_mean_m': monthly_m_vecmeansum})

month_vec.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_vec_transmiss.nc')

#Yearly mean and sum resampling of mosquito vector competence risk
yearly_m_vecminsum = (vecminsum.resample(time= '1Y').reduce(np.mean))
yearly_m_vecmaxsum = (vecmaxsum.resample(time= '1Y').reduce(np.mean))
yearly_m_vecmediansum = (vecmediansum.resample(time= '1Y').reduce(np.mean))
yearly_m_vecmeansum = (vecmeansum.resample(time= '1Y').reduce(np.mean))

yearly_s_vecminsum = (vecminsum.resample(time= '1Y').reduce(np.sum))
yearly_s_vecmaxsum = (vecmaxsum.resample(time= '1Y').reduce(np.sum))
yearly_s_vecmediansum = (vecmediansum.resample(time= '1Y').reduce(np.sum))
yearly_s_vecmeansum = (vecmeansum.resample(time= '1Y').reduce(np.sum))

#Build netCDF for yearly resampled risk for mosquito mortality risk
year_vec = xr.Dataset({'vec_yearly_minimum_s': yearly_s_vecminsum, 'vec_yearly_maximum_s': yearly_s_vecmaxsum,
                            'vec_yearly_median_s': yearly_s_vecmediansum, 'vec_yearly_mean_s': yearly_s_vecmeansum,
                            'vec_yearly_minimum_m': yearly_m_vecminsum, 'vec_yearly_maximum_m': yearly_m_vecmaxsum,
                            'vec_yearly_median_m': yearly_m_vecmediansum, 'vec_yearly_mean_m': yearly_m_vecmeansum})

year_vec.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_vec_transmiss.nc')

# Characterise overall risk minimum to peak with regression from peak
oamin_min = xr.where((daily_min >= 19.1)&(daily_min <= 25),(0.1695*(daily_min)-3.2373),0)
oamax_min = xr.where((daily_max >= 19.1)&(daily_max <= 25),(0.1695*(daily_max)-3.2373),0)
oamedian_min = xr.where((daily_median >= 19.1)&(daily_median <= 25),(0.1695*(daily_median)-3.2373),0)
oamean_min = xr.where((daily_mean >= 19.1)&(daily_mean <= 25),(0.1695*(daily_mean)-3.2373),0)

# Characterise overall risk peak to maximum with regression from peak
oamin_max  = xr.where((daily_min >= 25)&(daily_min <= 30.1),(-0.1961*(daily_min)+5.902),0)
oamax_max = xr.where((daily_max >= 25)&(daily_max <= 30.1),(-0.1961*(daily_max)+5.902),0)
oamedian_max = xr.where((daily_median >= 25)&(daily_median <= 30.1),(-0.1961*(daily_median)+5.902),0)
oamean_max  = xr.where((daily_mean >= 25)&(daily_mean <= 30.1),(-0.1961*(daily_mean)+5.902),0)

#Sum overall risk minimum, peak and peak maximum to normalised indicator of 0 to 1.
oaminsum = oamin_min+oamin_max
oamaxsum = oamax_max+oamax_min
oamediansum = oamedian_min+oamedian_max
oameansum = oamean_min+oamean_max

#Build netCDF with summarised overall risk indicators for daily diurnal range and mean
oa = xr.Dataset({'Overall_Transmissivity_daily_minimum': oaminsum, 'Overall_Transmissivity_daily_maximum':oamaxsum,'Overall_Transmissivity_daily_median':oamediansum,'Overall_Transmissivity_daily_mean':oameansum})
oa.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/overall_transmiss.nc')

#Monthly mean and sum resampling of overall risk
monthly_m_oaminsum = (oaminsum.resample(time= '1M').reduce(np.mean))
monthly_m_oamaxsum = (oamaxsum.resample(time= '1M').reduce(np.mean))
monthly_m_oamediansum = (oamediansum.resample(time= '1M').reduce(np.mean))
monthly_m_oameansum = (oameansum.resample(time= '1M').reduce(np.mean))

monthly_s_oaminsum = (oaminsum.resample(time= '1M').reduce(np.sum))
monthly_s_oamaxsum = (oamaxsum.resample(time= '1M').reduce(np.sum))
monthly_s_oamediansum = (oamediansum.resample(time= '1M').reduce(np.sum))
monthly_s_oameansum = (oameansum.resample(time= '1M').reduce(np.sum))

#Build netCDF for monthly resampled risk for overall risk
month_oa = xr.Dataset({'oa_monthly_minimum_s': monthly_s_oaminsum, 'oa_monthly_maximum_s': monthly_s_oamaxsum,
                            'oa_monthly_median_s': monthly_s_oamediansum, 'oa_monthly_mean_s': monthly_s_oameansum,
                            'oa_monthly_minimum_m': monthly_m_oaminsum, 'oa_monthly_maximum_m': monthly_m_oamaxsum,
                            'oa_monthly_median_m': monthly_m_oamediansum, 'oa_monthly_mean_m': monthly_m_oameansum})

month_oa.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_oa_transmiss.nc')

#Yearly mean and sum resampling of overall risk
yearly_m_oaminsum = (oaminsum.resample(time= '1Y').reduce(np.mean))
yearly_m_oamaxsum = (oamaxsum.resample(time= '1Y').reduce(np.mean))
yearly_m_oamediansum = (oamediansum.resample(time= '1Y').reduce(np.mean))
yearly_m_oameansum = (oameansum.resample(time= '1Y').reduce(np.mean))

yearly_s_oaminsum = (oaminsum.resample(time= '1Y').reduce(np.sum))
yearly_s_oamaxsum = (oamaxsum.resample(time= '1Y').reduce(np.sum))
yearly_s_oamediansum = (oamediansum.resample(time= '1Y').reduce(np.sum))
yearly_s_oameansum = (oameansum.resample(time= '1Y').reduce(np.sum))

#Build netCDF for yearly resampled risk for overall risk
year_oa = xr.Dataset({'oa_yearly_minimum_s': yearly_s_oaminsum, 'oa_yearly_maximum_s': yearly_s_oamaxsum,
                            'oa_yearly_median_s': yearly_s_oamediansum, 'oa_yearly_mean_s': yearly_s_oameansum,
                            'oa_yearly_minimum_m': yearly_m_oaminsum, 'oa_yearly_maximum_m': yearly_m_oamaxsum,
                            'oa_yearly_median_m': yearly_m_oamediansum, 'oa_yearly_mean_m': yearly_m_oameansum})

year_oa.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_oa_transmiss.nc')
