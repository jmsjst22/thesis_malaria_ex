import xarray as xr
import glob
import numpy as np

'''

Intent

Production of summary statistics for risk classification of purportedly non-linear
precipitation risk factor.

This is the only file in the library which does not require the linear classification of
risk as precipitation is not well enough characterised in order to associate it with a specific risk level.

All results are broad and exploratory and aim to provide detail to facilitate this only.

Requirements

Single netCDF as merged from two precipitation netCDFs, limited to around 8
years for designated area (due to download size limitations of Copernicus Data Store)

Four additional netCDFs produced at at least 0.08 the original temporal resolution
requires approximately 50% of the original data storage of original file.

'''

#Open netCDF of full study period
eda = xr.open_dataset('/home/s1987119/Diss_data/Final/Precipitation/Process/precip_2004_2019.nc')

# Generate daily summary statistics, multiplying by 1000 to standard climatic units
daily_sum = (eda.resample(time= '1D').reduce(np.sum)*1000).tp
daily_mean = (eda.resample(time= '1D').reduce(np.mean)*1000).tp
daily_std = (eda.resample(time= '1D').reduce(np.std)).tp
daily_min = (eda.resample(time= '1D').reduce(np.min)*1000).tp
daily_max = (eda.resample(time= '1D').reduce(np.max)*1000).tp

#Build netCDF from summary statistics
daily = xr.Dataset({'daily_sum':daily_sum,'daily_mean':daily_mean,'daily_standard_dev':daily_std, 'daily_min': daily_min,'daily_max':daily_max})
daily.to_netcdf('/home/s1987119/Diss_data/Final/Precipitation/Process/total_precip.nc')

#Open daily netcdf at location
Dly_sumtp = xr.open_dataset('/home/s1987119/Diss_data/Final/Precipitation/Process/total_precip.nc')

#Resample for monthly statistics
monthly_mean = (Dly_sumtp.resample(time= '1M').reduce(np.mean)).daily_sum
monthly_range = (Dly_sumtp.resample(time= '1M').reduce(np.max) - Dly_sumtp.resample(time= '1M').reduce(np.min)).daily_sum
monthly_std = (Dly_sumtp.resample(time= '1M').reduce(np.std)).daily_sum
monthly_min = (Dly_sumtp.resample(time= '1M').reduce(np.min)).daily_sum
monthly_max = (Dly_sumtp.resample(time= '1M').reduce(np.max)).daily_sum

#Build netCDF for monthly statistical summary
monthly =xr.Dataset({'monthly_mean_prec':monthly_mean,'monthly_range':monthly_range,'monthly_std':monthly_std,'monthly_min':monthly_min,'monthly_max':monthly_max})
monthly.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthly_total_precip.nc')

#Resample daily sum data to yearly resolution statistics
yearly_mean = (Dly_sumtp.resample(time= '1Y').reduce(np.mean)).daily_sum
yearly_range = (Dly_sumtp.resample(time= '1Y').reduce(np.max) - Dly_sumtp.resample(time= '1Y').reduce(np.min)).daily_sum
yearly_std = (Dly_sumtp.resample(time= '1Y').reduce(np.std)).daily_sum
yearly_min = (Dly_sumtp.resample(time= '1Y').reduce(np.min)).daily_sum
yearly_max = (Dly_sumtp.resample(time= '1Y').reduce(np.max)).daily_sum

#Build netCDF for yearly statistical summary
yearly = xr.Dataset({'yearly_mean_prec':yearly_mean,'yearly_range':yearly_range,'yearly_std':yearly_std,'yearly_min':yearly_min,'yearly_max':yearly_max})
yearly.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearly_total_precip.nc')

#Extract daily sum total precipiation data array from data set
Dly_sumtp = Dly_sumtp['daily_sum']

#Test on bins and add binary point to each variable when criteria is met. One point per location, per day is possible: days per month where daily total precipitation fits in each bin
tp0 = xr.where((Dly_sumtp == 0), 1,0)
tp1_25 = xr.where((Dly_sumtp > 0)&(Dly_sumtp < 25), 1,0)
tp25_50 = xr.where((Dly_sumtp >= 25)&(Dly_sumtp < 50), 1,0)
tp50_100 = xr.where((Dly_sumtp >= 50)&(Dly_sumtp < 100), 1,0)
tp100_200 = xr.where((Dly_sumtp >= 100)&(Dly_sumtp < 200), 1,0)
tp200_300 = xr.where((Dly_sumtp >= 200)&(Dly_sumtp < 300), 1,0)
tp300_400 = xr.where((Dly_sumtp >= 300)&(Dly_sumtp < 400), 1,0)
tp400_500 = xr.where((Dly_sumtp >= 400)&(Dly_sumtp < 500), 1,0)
tp500_600 = xr.where((Dly_sumtp >= 500)&(Dly_sumtp < 600), 1,0)
tp600_700 = xr.where((Dly_sumtp >= 600)&(Dly_sumtp < 700), 1,0)
tp700_800 = xr.where((Dly_sumtp >= 700)&(Dly_sumtp < 800), 1,0)
tp800_900 = xr.where((Dly_sumtp >= 800)&(Dly_sumtp < 900), 1,0)
tp900_1000 = xr.where((Dly_sumtp >= 900)&(Dly_sumtp < 1000), 1,0)
tp1000_ = xr.where((Dly_sumtp >= 1000), 1,0)

#Resample above points to provide accumulated monthly risk score as caused by precipitation.
#Each bin is standardised to 0-1 to reflect non-linear nature and simply capture frequency and commonality of "bins"
tppm0= tp0.resample(time= '1M').reduce(np.sum)
tppm1_25 = tp1_25.resample(time= '1M').reduce(np.sum)
tppm25_50 = tp25_50.resample(time= '1M').reduce(np.sum)
tppm50_100 = tp50_100.resample(time= '1M').reduce(np.sum)
tppm100_200 = tp100_200.resample(time= '1M').reduce(np.sum)
tppm200_300 = tp200_300.resample(time= '1M').reduce(np.sum)
tppm300_400 = tp300_400.resample(time= '1M').reduce(np.sum)
tppm400_500 = tp400_500.resample(time= '1M').reduce(np.sum)
tppm500_600 = tp500_600.resample(time= '1M').reduce(np.sum)
tppm600_700 = tp600_700.resample(time= '1M').reduce(np.sum)
tppm700_800 = tp700_800.resample(time= '1M').reduce(np.sum)
tppm800_900 = tp800_900.resample(time= '1M').reduce(np.sum)
tppm900_1000 = tp900_1000.resample(time= '1M').reduce(np.sum)
tppm1000_ = tp1000_.resample(time= '1M').reduce(np.sum)

#Build netcdf for characterising monthly commonality of precipitation bins
mtpm = xr.Dataset({"DpMth_0":tppm0, "DpMth_1_25": tppm1_25, "DpMth_25_50": tppm25_50, "DpMth_50_100": tppm50_100,
                "DpMth_100_200": tppm100_200, "DpMth_200_300": tppm200_300, "DpMth_300_400":
                tppm300_400,"DpMth_400_500": tppm400_500,"DpMth_500_600": tppm500_600,
                "DpMth_600_700": tppm600_700,"DpMth_700_800": tppm700_800, "DpMth_800_900": tppm800_900,
                "DpMth_900_1000": tppm900_1000,"DpMth1000_":tppm1000_})

mtpm.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/monthlyprecip_risk.nc')

tppy0= tp0.resample(time= '1Y').reduce(np.sum)
tppy1_25 = tp1_25.resample(time= '1Y').reduce(np.sum)
tppy25_50 = tp25_50.resample(time= '1Y').reduce(np.sum)
tppy50_100 = tp50_100.resample(time= '1Y').reduce(np.sum)
tppy100_200 = tp100_200.resample(time= '1Y').reduce(np.sum)
tppy200_300 = tp200_300.resample(time= '1Y').reduce(np.sum)
tppy300_400 = tp300_400.resample(time= '1Y').reduce(np.sum)
tppy400_500 = tp400_500.resample(time= '1Y').reduce(np.sum)
tppy500_600 = tp500_600.resample(time= '1Y').reduce(np.sum)
tppy600_700 = tp600_700.resample(time= '1Y').reduce(np.sum)
tppy700_800 = tp700_800.resample(time= '1Y').reduce(np.sum)
tppy800_900 = tp800_900.resample(time= '1Y').reduce(np.sum)
tppy900_1000 = tp900_1000.resample(time= '1Y').reduce(np.sum)
tppy1000_ = tp1000_.resample(time= '1Y').reduce(np.sum)

#Build netcdf for characterising yearly commonality of precipitation bins
ytpm = xr.Dataset({"DpYear_0":tppy0, "DpYear_1_25": tppy1_25, "DpYear_25_50": tppy25_50, "DpYear_50_100": tppy50_100,
                "DpYear_100_200": tppy100_200, "DpYear_200_300": tppy200_300, "DpYear_300_400":
                tppy300_400,"DpYear_400_500": tppy400_500,"DpYear_500_600": tppy500_600,
                "DpYear_600_700": tppy600_700,"DpYear_700_800": tppy700_800, "DpYear_800_900": tppy800_900,
                "DpYear_900_1000": tppy900_1000,"DpYear1000_":tppy1000_})

ytpm.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/yearlyprecip_risk.nc')
