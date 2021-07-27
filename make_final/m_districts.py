import os
import pandas as pd
import matplotlib.pyplot as plot
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import xarray as xr
import rioxarray as rx

t2mean_mo = {}
t2range_mo = {}
t2br_mean_mo = {}
t2ega_mean_mo = {}
t2egfe_mean_mo = {}
t2mor_max_mo = {}
t2mor_min_mo = {}
t2mosdev_mean_mo = {}
t2oa_mean_mo = {}
t2vec_mean_mo = {}
t2diurnal_risk_mo = {}

precmean_mo = {}
precstd_mo = {}
precmin_mo = {}
precmax_mo = {}
DpMth_0 = {}
DpMth_1_25 = {}
DpMth_25_50 = {}
DpMth_50_100 = {}
DpMth_100_200 = {}
DpMth_200_300 = {}
DpMth_300_400 = {}
DpMth_400_500 = {}
DpMth_500_600 = {}
DpMth_600_700 = {}
DpMth_700_800 = {}
DpMth_800_900 = {}
DpMth_900_1000 = {}
DpMth_1000 = {}

hummean_mo = {}
humstd_mo = {}
humrisk_mo = {}
mean_Hum_High = {}
mean_Hum_Low = {}
min_Hum_High = {}
min_Hum_Low = {}
humrange_mo = {}



districts = gpd.read_file('/home/s1987119/Diss_data/Final/Final_Products/DISTRICTS_2018_UTM_36N.shp')


ms_temp = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/Monthly_temperature.nc', decode_coords='all')
ms_prec = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/precipitation/monthly_total_precip.nc', decode_coords='all')

ms_hum = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/humidity/humidity_monthly.nc', decode_coords='all')

ms_temp_br = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_biterate_transmiss.nc', decode_coords='all')
ms_temp_ega = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_ega_transmiss.nc', decode_coords='all')
ms_temp_egfe = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_egfe_transmiss.nc', decode_coords='all')
ms_temp_mor = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_mor_transmiss.nc', decode_coords='all')
ms_temp_mosdev = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_mosdev_transmiss.nc', decode_coords='all')
ms_temp_vec = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_vec_transmiss.nc', decode_coords='all')
ms_temp_oa = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_oa_transmiss.nc', decode_coords='all')

ms_temp_diu = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/monthly_diurnal_temp.nc', decode_coords='all')

ms_prec_risk = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/precipitation/monthlyprecip_risk.nc',decode_coords ='all')

districts = districts.to_crs('epsg:4326')



ms_temp = ms_temp.rio.write_crs(4326)
ms_temp_br = ms_temp_br.rio.write_crs(4326)
ms_temp_ega = ms_temp_ega.rio.write_crs(4326)
ms_temp_egfe = ms_temp_egfe.rio.write_crs(4326)
ms_temp_mor = ms_temp_mor.rio.write_crs(4326)
ms_temp_mosdev = ms_temp_mosdev.rio.write_crs(4326)
ms_temp_oa = ms_temp_oa.rio.write_crs(4326)
ms_temp_vec = ms_temp_vec.rio.write_crs(4326)
ms_temp_diu = ms_temp_diu.rio.write_crs(4326)

ms_prec = ms_prec.rio.write_crs(4326)
ms_prec_risk = ms_prec_risk.rio.write_crs(4326)

ms_hum = ms_hum.rio.write_crs(4326)


for idx,district in districts.iterrows():
    t2mean_mo[district.DName2018]=ms_temp.monthly_mean.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2range_mo[district.DName2018]=ms_temp.monthly_range.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2br_mean_mo[district.DName2018]=ms_temp_br.biterate_monthly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2ega_mean_mo[district.DName2018]=ms_temp_ega.ega_monthly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2egfe_mean_mo[district.DName2018]=ms_temp_egfe.egfe_monthly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2mor_max_mo[district.DName2018]=ms_temp_mor.mor_monthly_maximum_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2mor_min_mo[district.DName2018]=ms_temp_mor.mor_monthly_minimum_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2mosdev_mean_mo[district.DName2018]=ms_temp_mosdev.Mos_dev_monthly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2oa_mean_mo[district.DName2018]=ms_temp_oa.oa_monthly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2vec_mean_mo[district.DName2018]=ms_temp_vec.vec_monthly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
    t2diurnal_risk_mo[district.DName2018]=ms_temp_diu.Mean_monthly_risk.rio.clip([district.geometry]).mean(dim=['x','y']).values


    precmean_mo[district.DName2018]=ms_prec.monthly_mean_prec.rio.clip([district.geometry]).mean(dim=['x','y']).values
    precstd_mo[district.DName2018]=ms_prec.monthly_std.rio.clip([district.geometry]).max(dim=['x','y']).values
    precmin_mo[district.DName2018]=ms_prec.monthly_min.rio.clip([district.geometry]).mean(dim=['x','y']).values
    precmax_mo[district.DName2018]=ms_prec.monthly_max.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_0[district.DName2018]=ms_prec_risk.DpMth_0.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_1_25[district.DName2018] = ms_prec_risk.DpMth_1_25.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_25_50[district.DName2018] = ms_prec_risk.DpMth_25_50.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_50_100[district.DName2018] = ms_prec_risk.DpMth_50_100.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_100_200[district.DName2018] = ms_prec_risk.DpMth_100_200.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_200_300[district.DName2018] = ms_prec_risk.DpMth_200_300.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_300_400[district.DName2018] = ms_prec_risk.DpMth_300_400.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_400_500[district.DName2018] = ms_prec_risk.DpMth_400_500.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_500_600[district.DName2018] = ms_prec_risk.DpMth_500_600.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_600_700[district.DName2018] = ms_prec_risk.DpMth_600_700.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_700_800[district.DName2018] = ms_prec_risk.DpMth_700_800.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_800_900[district.DName2018] = ms_prec_risk.DpMth_800_900.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_900_1000[district.DName2018] = ms_prec_risk.DpMth_900_1000.rio.clip([district.geometry]).mean(dim=['x','y']).values
    DpMth_1000[district.DName2018] = ms_prec_risk.DpMth1000_.rio.clip([district.geometry]).mean(dim=['x','y']).values

    hummean_mo[district.DName2018]=ms_hum.Monthly_mean_hum.rio.clip([district.geometry]).mean(dim=['x','y']).values
    humrisk_mo[district.DName2018]=ms_hum.Humidity_risk.rio.clip([district.geometry]).mean(dim=['x','y']).values
    humstd_mo[district.DName2018]=ms_hum.Monthly_Standard_deviation_hum.rio.clip([district.geometry]).max(dim=['x','y']).values
    mean_Hum_High[district.DName2018]=ms_hum.mean_Hum_High_risk_days.rio.clip([district.geometry]).max(dim=['x','y']).values
    mean_Hum_Low[district.DName2018]=ms_hum.mean_Hum_lower_risk_days.rio.clip([district.geometry]).max(dim=['x','y']).values
    min_Hum_High[district.DName2018]=ms_hum.min_Hum_High_risk_days.rio.clip([district.geometry]).max(dim=['x','y']).values
    min_Hum_Low[district.DName2018]=ms_hum.min_Hum_lower_risk_days.rio.clip([district.geometry]).max(dim=['x','y']).values
    humrange_mo[district.DName2018]=ms_hum.Monthly_range.rio.clip([district.geometry]).max(dim=['x','y']).values


t2datamean_mo = pd.DataFrame(t2mean_mo,index=(ms_temp.time)).T
t2datarange_mo = pd.DataFrame(t2range_mo,index=(ms_temp.time)).T
t2br_data_mean_mo = pd.DataFrame(t2br_mean_mo,index=(ms_temp_br.time)).T
t2ega_data_mean_mo = pd.DataFrame(t2ega_mean_mo,index=(ms_temp_ega.time)).T
t2egfe_data_mean_mo = pd.DataFrame(t2egfe_mean_mo,index=(ms_temp_egfe.time)).T
t2mor_data_min_mo = pd.DataFrame(t2mor_min_mo,index=(ms_temp_mor.time)).T
t2mor_data_max_mo = pd.DataFrame(t2mor_max_mo,index=(ms_temp_mor.time)).T
t2mosdev_data_mean_mo = pd.DataFrame(t2mosdev_mean_mo,index=(ms_temp_mosdev.time)).T
t2oa_data_mean_mo = pd.DataFrame(t2oa_mean_mo,index=(ms_temp_oa.time)).T
t2vec_data_mean_mo = pd.DataFrame(t2vec_mean_mo,index=(ms_temp_vec.time)).T
t2diurnal_data_risk_mo = pd.DataFrame(t2diurnal_risk_mo,index=(ms_temp_diu.time)).T

precmean_mo = pd.DataFrame(precmean_mo,index=(ms_prec.time)).T
precstd_mo = pd.DataFrame(precstd_mo,index=(ms_prec.time)).T
precmin_mo = pd.DataFrame(precmin_mo,index=(ms_prec.time)).T
precmax_mo = pd.DataFrame(precmax_mo,index=(ms_prec.time)).T
DpMth_0 = pd.DataFrame(DpMth_0,index=(ms_prec_risk.time)).T
DpMth_1_25 = pd.DataFrame(DpMth_1_25,index=(ms_prec_risk.time)).T
DpMth_25_50 = pd.DataFrame(DpMth_25_50,index=(ms_prec_risk.time)).T
DpMth_50_100 = pd.DataFrame(DpMth_50_100,index=(ms_prec_risk.time)).T
DpMth_100_200 = pd.DataFrame(DpMth_100_200,index=(ms_prec_risk.time)).T
DpMth_200_300 = pd.DataFrame(DpMth_200_300,index=(ms_prec_risk.time)).T
DpMth_300_400 = pd.DataFrame(DpMth_300_400,index=(ms_prec_risk.time)).T
DpMth_400_500 = pd.DataFrame(DpMth_400_500,index=(ms_prec_risk.time)).T
DpMth_500_600 = pd.DataFrame(DpMth_500_600,index=(ms_prec_risk.time)).T
DpMth_600_700 = pd.DataFrame(DpMth_600_700,index=(ms_prec_risk.time)).T
DpMth_700_800 = pd.DataFrame(DpMth_700_800,index=(ms_prec_risk.time)).T
DpMth_800_900 = pd.DataFrame(DpMth_800_900,index=(ms_prec_risk.time)).T
DpMth_900_1000 = pd.DataFrame(DpMth_900_1000,index=(ms_prec_risk.time)).T
DpMth_1000 = pd.DataFrame(DpMth_1000,index=(ms_prec_risk.time)).T

hummean_mo = pd.DataFrame(hummean_mo,index=(ms_hum.time)).T
humrisk_mo = pd.DataFrame(humrisk_mo,index=(ms_hum.time)).T
humstd_mo = pd.DataFrame(humstd_mo,index=(ms_hum.time)).T
mean_Hum_High = pd.DataFrame(mean_Hum_High,index=(ms_hum.time)).T
mean_Hum_Low = pd.DataFrame(mean_Hum_Low,index=(ms_hum.time)).T
min_Hum_High = pd.DataFrame(min_Hum_High,index=(ms_hum.time)).T
min_Hum_Low = pd.DataFrame(min_Hum_Low,index=(ms_hum.time)).T
humrange_mo  = pd.DataFrame(humrange_mo,index=(ms_hum.time)).T

t2datamean_mo = t2datamean_mo.add_suffix('_monthly_temp_mean')
t2datarange_mo = t2datarange_mo.add_suffix('_monthly_temp_range')
t2br_data_mean_mo = t2br_data_mean_mo.add_suffix('_monthly_temp_br4mean')
t2ega_data_mean_mo = t2ega_data_mean_mo.add_suffix('_monthly_temp_ega4mean')
t2egfe_data_mean_mo = t2egfe_data_mean_mo.add_suffix('_monthly_temp_egfe4mean')
t2mor_data_min_mo = t2mor_data_min_mo.add_suffix('_monthly_temp_mor4min')
t2mor_data_max_mo = t2mor_data_max_mo.add_suffix('_monthly_temp_mor4max')
t2mosdev_data_mean_mo = t2mosdev_data_mean_mo.add_suffix('_monthly_temp_mosdev4mean')
t2oa_data_mean_mo = t2oa_data_mean_mo.add_suffix('_monthly_temp_oa4mean')
t2vec_data_mean_mo = t2vec_data_mean_mo.add_suffix('monthly_temp_vec4mean')
t2diurnal_data_risk_mo = t2diurnal_data_risk_mo.add_suffix('_monthly_temp_diurnal')

precmean_mo = precmean_mo.add_suffix('_monthly_precmean')
precstd_mo = precstd_mo.add_suffix('_monthly_precstd')
precmin_mo = precmin_mo.add_suffix('_monthly_precmin')
precmax_mo = precmax_mo.add_suffix('_monthly_precmax')
DpMth_0 = DpMth_0.add_suffix('_0_dly_prec_month')
DpMth_1_25 = DpMth_1_25.add_suffix('_0_dly_prec_month')
DpMth_25_50 = DpMth_25_50.add_suffix('_25_50dly_prec_month')
DpMth_50_100 = DpMth_50_100.add_suffix('_50_100dly_prec_month')
DpMth_100_200 = DpMth_100_200.add_suffix('_100_200dly_prec_month')
DpMth_200_300 = DpMth_200_300.add_suffix('_200_300dly_prec_month')
DpMth_300_400 = DpMth_300_400.add_suffix('_300_400dly_prec_month')
DpMth_400_500 = DpMth_400_500.add_suffix('_400_500dly_prec_month')
DpMth_500_600 = DpMth_500_600.add_suffix('_500_600dly_prec_month')
DpMth_600_700 = DpMth_600_700.add_suffix('_600_700dly_prec_month')
DpMth_700_800 = DpMth_700_800.add_suffix('_700_800dly_prec_month')
DpMth_800_900 = DpMth_800_900.add_suffix('_800_900dly_prec_month')
DpMth_900_1000 = DpMth_900_1000.add_suffix('_900_1000dly_prec_month')
DpMth_1000 = DpMth_1000.add_suffix('_1000_dly_prec_month')


hummean_mo= hummean_mo.add_suffix('_monthly_hum_mean')
humrisk_mo= humrisk_mo.add_suffix('_monthly_hum_risk')
humstd_mo= humstd_mo.add_suffix('_monthly_hum_std')
mean_Hum_High= mean_Hum_High.add_suffix('_monthly_hum_MeIH')
mean_Hum_Low= mean_Hum_Low.add_suffix('_monthly_hum_MeIL')
min_Hum_High= min_Hum_High.add_suffix('_monthly_hum_MiIH')
min_Hum_Low= min_Hum_Low.add_suffix('_monthly_hum_MiIL')
humrange_mo= humrange_mo.add_suffix('_monthly_hum_range')

data = [t2datarange_mo,t2datamean_mo,precmean_mo,precstd_mo,precmin_mo,precmax_mo, t2br_data_mean_mo, t2ega_data_mean_mo, t2egfe_data_mean_mo, t2mor_data_max_mo,
        t2mor_data_min_mo, t2mosdev_data_mean_mo, t2oa_data_mean_mo, t2vec_data_mean_mo,
        DpMth_0,DpMth_1_25,DpMth_25_50,DpMth_50_100,DpMth_100_200,DpMth_200_300,DpMth_300_400,
        DpMth_400_500,DpMth_500_600,DpMth_600_700,DpMth_700_800,DpMth_800_900,DpMth_900_1000,DpMth_1000,
        hummean_mo, humrisk_mo,humstd_mo,mean_Hum_High,mean_Hum_Low
        ,min_Hum_High,min_Hum_Low,humrange_mo]

datamo = pd.concat(data,axis=1, sort=False, join='inner')

years = [2005,2006,2008,2009,2010,2011,2013,2014,2015,2016,2017,2018]

for year in years:
    filter_col = [col for col in datamo if col.startswith(str(year))]
    data = datamo[filter_col]
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('env_csv/'+str(year)+'_env_month.csv')



#data = pd.merge(t2datamean,t2datarange,on='DName2018',how='inner').T

#print(mean.head())

#bigger loop automated for each variable
#validate the clip








#print(district.geometry, district.DName2018)
