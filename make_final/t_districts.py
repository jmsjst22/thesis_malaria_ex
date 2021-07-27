import os
import pandas as pd
import geopandas as gpd
import xarray as xr
import rioxarray as rx

districts = gpd.read_file('/home/s1987119/Diss_data/Final/Final_Products/DISTRICTS_2018_UTM_36N.shp')


ms_temp = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/Monthly_temperature.nc', decode_coords='all', )
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

ms_temp = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/Monthly_temperature.nc', decode_coords='all', )
ms_prec = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/precipitation/monthly_total_precip.nc', decode_coords='all')

ms_hum = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/humidity/humidity_monthly.nc', decode_coords='all')

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



ys_temp = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/Yearly_temperature.nc', decode_coords='all')
ys_prec = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/precipitation/yearly_total_precip.nc', decode_coords='all')
ys_hum = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/humidity/humidity_yearly.nc', decode_coords='all')
ys_lucac = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/anych.nc', decode_coords='all')

ys_lucfl = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/forestloss.nc', decode_coords='all')
ys_difnat = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/diffnattest.nc', decode_coords='all')
ys_devnat = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/devnat.nc', decode_coords='all')
ys_mdevmnat = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/mdevmnat.nc', decode_coords='all')
ys_mwet2mdry = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/mwet2mdry.nc', decode_coords='all')
ys_mdry2mwet = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/mdry2mwet.nc', decode_coords='all')

ys_temp_br = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_biterate_transmiss.nc', decode_coords='all')
ys_temp_ega = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_ega_transmiss.nc', decode_coords='all')
ys_temp_egfe = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_egfe_transmiss.nc', decode_coords='all')
ys_temp_mor = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_mor_transmiss.nc', decode_coords='all')
ys_temp_mosdev = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_mosdev_transmiss.nc', decode_coords='all')
ys_temp_vec = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_vec_transmiss.nc', decode_coords='all')
ys_temp_oa = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_oa_transmiss.nc', decode_coords='all')

ys_temp_diu = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_diurnal_temp.nc', decode_coords='all')

ys_prec_risk = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/precipitation/yearlyprecip_risk.nc',decode_coords ='all')

districts = districts.to_crs('epsg:4326')

ys_temp = ys_temp.rio.write_crs(4326)
ys_temp_br = ys_temp_br.rio.write_crs(4326)
ys_temp_ega = ys_temp_ega.rio.write_crs(4326)
ys_temp_egfe = ys_temp_egfe.rio.write_crs(4326)
ys_temp_mor = ys_temp_mor.rio.write_crs(4326)
ys_temp_mosdev = ys_temp_mosdev.rio.write_crs(4326)
ys_temp_oa = ys_temp_oa.rio.write_crs(4326)
ys_temp_vec = ys_temp_vec.rio.write_crs(4326)
ys_temp_diu = ys_temp_diu.rio.write_crs(4326)

ys_prec = ys_prec.rio.write_crs(4326)
ys_prec_risk = ys_prec_risk.rio.write_crs(4326)

ys_hum = ys_hum.rio.write_crs(4326)

ys_lucac = ys_lucac.rio.write_crs(4326)
ys_lucfl = ys_lucfl.rio.write_crs(4326)
ys_mdevmnat = ys_mdevmnat.rio.write_crs(4326)
ys_mwet2mdry = ys_mwet2mdry.rio.write_crs(4326)
ys_mdry2mwet = ys_mdry2mwet.rio.write_crs(4326)
ys_devnat = ys_devnat.rio.write_crs(4326)
ys_difnat = ys_difnat.rio.write_crs(4326)

t2mean = {}
t2range = {}
t2br_mean_y = {}
t2ega_mean_y = {}
t2egfe_mean_y = {}
t2mor_max_y = {}
t2mor_min_y = {}
t2mosdev_mean_y = {}
t2oa_mean_y = {}
t2vec_mean_y = {}
t2diurnal_risk = {}

precmean = {}
precstd = {}
precmin = {}
precmax = {}
DpYear_0 = {}
DpYear_1_25 = {}
DpYear_25_50 = {}
DpYear_50_100 = {}
DpYear_100_200 = {}
DpYear_200_300 = {}
DpYear_300_400 = {}
DpYear_400_500 = {}
DpYear_500_600 = {}
DpYear_600_700 = {}
DpYear_700_800 = {}
DpYear_800_900 = {}
DpYear_900_1000 = {}
DpYear_1000 = {}

hummean_y = {}
humstd_y = {}
hummax_y = {}
hummin_y = {}
humrange_y = {}

mean_Hum_High_y = {}
mean_Hum_Low_y = {}
min_Hum_High_y = {}
min_Hum_Low_y = {}


any_ch_lu = {}
fl_lu = {}
mdevmnat_lu = {}
mwet2mdry_lu = {}
mdry2mwet_lu = {}
devnat_lu = {}
difnat_lu = {}

LUC_dict = {}
fl_dict = {}
mdevmnat_dict = {}
mwet2mdry_dict = {}
mdry2mwet_dict = {}
devnat_dict = {}
difnat_lu = {}


for idx,district in districts.iterrows():
   t2mean[district.DName2018]=ys_temp.yearly_mean.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2range[district.DName2018]=ys_temp.yearly_range.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2br_mean_y[district.DName2018]=ys_temp_br.biterate_yearly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2ega_mean_y[district.DName2018]=ys_temp_ega.ega_yearly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2egfe_mean_y[district.DName2018]=ys_temp_egfe.egfe_yearly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2mor_max_y[district.DName2018]=ys_temp_mor.mor_yearly_maximum_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2mor_min_y[district.DName2018]=ys_temp_mor.mor_yearly_minimum_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2mosdev_mean_y[district.DName2018]=ys_temp_mosdev.Mos_dev_yearly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2oa_mean_y[district.DName2018]=ys_temp_oa.oa_yearly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2vec_mean_y[district.DName2018]=ys_temp_vec.vec_yearly_mean_m.rio.clip([district.geometry]).mean(dim=['x','y']).values
   t2diurnal_risk[district.DName2018]=ys_temp_diu.Mean_yearly_risk.rio.clip([district.geometry]).mean(dim=['x','y']).values


   precmean[district.DName2018]=ys_prec.yearly_mean_prec.rio.clip([district.geometry]).mean(dim=['x','y']).values
   precstd[district.DName2018]=ys_prec.yearly_std.rio.clip([district.geometry]).max(dim=['x','y']).values
   precmin[district.DName2018]=ys_prec.yearly_min.rio.clip([district.geometry]).mean(dim=['x','y']).values
   precmax[district.DName2018]=ys_prec.yearly_max.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_0[district.DName2018]=ys_prec_risk.DpYear_0.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_1_25[district.DName2018] = ys_prec_risk.DpYear_1_25.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_25_50[district.DName2018] = ys_prec_risk.DpYear_25_50.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_50_100[district.DName2018] = ys_prec_risk.DpYear_50_100.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_100_200[district.DName2018] = ys_prec_risk.DpYear_100_200.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_200_300[district.DName2018] = ys_prec_risk.DpYear_200_300.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_300_400[district.DName2018] = ys_prec_risk.DpYear_300_400.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_400_500[district.DName2018] = ys_prec_risk.DpYear_400_500.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_500_600[district.DName2018] = ys_prec_risk.DpYear_500_600.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_600_700[district.DName2018] = ys_prec_risk.DpYear_600_700.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_700_800[district.DName2018] = ys_prec_risk.DpYear_700_800.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_800_900[district.DName2018] = ys_prec_risk.DpYear_800_900.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_900_1000[district.DName2018] = ys_prec_risk.DpYear_900_1000.rio.clip([district.geometry]).mean(dim=['x','y']).values
   DpYear_1000[district.DName2018] = ys_prec_risk.DpYear1000_.rio.clip([district.geometry]).mean(dim=['x','y']).values

   hummean_y[district.DName2018]=ys_hum.yearly_mean.rio.clip([district.geometry]).mean(dim=['x','y']).values
   humstd_y[district.DName2018]=ys_hum.yearly_std.rio.clip([district.geometry]).mean(dim=['x','y']).values
   hummax_y[district.DName2018]=ys_hum.yearly_max.rio.clip([district.geometry]).mean(dim=['x','y']).values
   hummin_y[district.DName2018]=ys_hum.yearly_min.rio.clip([district.geometry]).mean(dim=['x','y']).values
   humrange_y[district.DName2018]=ys_hum.yearly_range.rio.clip([district.geometry]).mean(dim=['x','y']).values

   mean_Hum_High_y[district.DName2018]=ys_hum.high_days_mean.rio.clip([district.geometry]).mean(dim=['x','y']).values
   mean_Hum_Low_y[district.DName2018]=ys_hum.low_days_mean.rio.clip([district.geometry]).mean(dim=['x','y']).values
   min_Hum_High_y[district.DName2018]=ys_hum.high_days_min.rio.clip([district.geometry]).mean(dim=['x','y']).values
   min_Hum_Low_y[district.DName2018]=ys_hum.low_days_min.rio.clip([district.geometry]).mean(dim=['x','y']).values

luckeys = ys_lucac.variables.keys()
t = 0
for k in luckeys:
    k=k
    if k.startswith('ANY'):
        for idx,district in districts.iterrows():
            any_ch_lu[district.DName2018]=ys_lucac[k].rio.clip([district.geometry]).sum(dim=['x','y']).values
            LUC_dict[k]=any_ch_lu
LUC_any_dataframe = pd.DataFrame(LUC_dict)

fluckeys = ys_lucfl.variables.keys()
for fk in fluckeys:
    fk=fk
    if fk.startswith('loss'):
        for idx,district in districts.iterrows():
            fl_lu[district.DName2018]=ys_lucfl[fk].rio.clip([district.geometry]).sum(dim=['x','y']).values
            fl_dict[fk]=fl_lu
LUC_fl_dataframe = pd.DataFrame(fl_dict)

mdevkeys = ys_mdevmnat.variables.keys()
for mdk in mdevkeys:
    mdk=mdk
    if mdk.startswith('N2D'):
        for idx,district in districts.iterrows():
            mdevmnat_lu[district.DName2018]=ys_mdevmnat[mdk].rio.clip([district.geometry]).sum(dim=['x','y']).values
            mdevmnat_dict[mdk]=mdevmnat_lu
LUC_mdevmnat_dataframe = pd.DataFrame(mdevmnat_dict)


devkeys = ys_devnat.variables.keys()
for dk in devkeys:
    dk=dk
    if dk.startswith('N2D'):
        for idx,district in districts.iterrows():
            devnat_lu[district.DName2018]=ys_devnat[dk].rio.clip([district.geometry]).sum(dim=['x','y']).values
            devnat_dict[dk]=devnat_lu
LUC_devnat_dataframe = pd.DataFrame(devnat_dict)

for idx,district in districts.iterrows():
    difnat_lu[district.DName2018]=ys_difnat.rio.clip([district.geometry]).mean(dim=['x','y']).values
    LUC_difnat_dataframe = pd.DataFrame(difnat_lu).T

mwetkeys = ys_mwet2mdry.variables.keys()
for mwk in mwetkeys:
    mwk=mwk
    if mwk.startswith('D_'):
        for idx,district in districts.iterrows():
            mwet2mdry_lu[district.DName2018]=ys_mwet2mdry[mwk].rio.clip([district.geometry]).sum(dim=['x','y']).values
            mwet2mdry_dict[mwk]= mwet2mdry_lu
LUC_mwet2mdry_dataframe = pd.DataFrame(mwet2mdry_dict)

mdrykeys = ys_mdry2mwet.variables.keys()
for mdk in mdrykeys:
    mdk=mdk
    if mdk.startswith('IIF'):
        for idx,district in districts.iterrows():
            mdry2mwet_lu[district.DName2018]=ys_mdry2mwet[mdk].rio.clip([district.geometry]).sum(dim=['x','y']).values
            mdry2mwet_dict[mdk]= mdry2mwet_lu
LUC_mdry2mwet_dataframe = pd.DataFrame(mdry2mwet_dict)


t2datamean = pd.DataFrame(t2mean,index=(ys_temp.time)).T
t2datarange = pd.DataFrame(t2range,index=(ys_temp.time)).T
t2br_data_meany = pd.DataFrame(t2br_mean_y,index=(ys_temp_br.time)).T
t2ega_data_meany = pd.DataFrame(t2ega_mean_y,index=(ys_temp_ega.time)).T
t2egfe_data_meany = pd.DataFrame(t2egfe_mean_y,index=(ys_temp_egfe.time)).T
t2mor_data_miny = pd.DataFrame(t2mor_min_y,index=(ys_temp_mor.time)).T
t2mor_data_maxy = pd.DataFrame(t2mor_max_y,index=(ys_temp_mor.time)).T
t2mosdev_data_meany = pd.DataFrame(t2mosdev_mean_y,index=(ys_temp_mosdev.time)).T
t2oa_data_meany = pd.DataFrame(t2oa_mean_y,index=(ys_temp_oa.time)).T
t2vec_data_meany = pd.DataFrame(t2vec_mean_y,index=(ys_temp_vec.time)).T
t2diurnal_data_risk = pd.DataFrame(t2diurnal_risk,index=(ys_temp_diu.time)).T

precmean = pd.DataFrame(precmean,index=(ys_prec.time)).T
precstd = pd.DataFrame(precstd,index=(ys_prec.time)).T
precmin = pd.DataFrame(precmin,index=(ys_prec.time)).T
precmax = pd.DataFrame(precmax,index=(ys_prec.time)).T
DpYear_0 = pd.DataFrame(DpYear_0,index=(ys_prec_risk.time)).T
DpYear_1_25 = pd.DataFrame(DpYear_1_25,index=(ys_prec_risk.time)).T
DpYear_25_50 = pd.DataFrame(DpYear_25_50,index=(ys_prec_risk.time)).T
DpYear_50_100 = pd.DataFrame(DpYear_50_100,index=(ys_prec_risk.time)).T
DpYear_100_200 = pd.DataFrame(DpYear_100_200,index=(ys_prec_risk.time)).T
DpYear_200_300 = pd.DataFrame(DpYear_200_300,index=(ys_prec_risk.time)).T
DpYear_300_400 = pd.DataFrame(DpYear_300_400,index=(ys_prec_risk.time)).T
DpYear_400_500 = pd.DataFrame(DpYear_400_500,index=(ys_prec_risk.time)).T
DpYear_500_600 = pd.DataFrame(DpYear_500_600,index=(ys_prec_risk.time)).T
DpYear_600_700 = pd.DataFrame(DpYear_600_700,index=(ys_prec_risk.time)).T
DpYear_700_800 = pd.DataFrame(DpYear_700_800,index=(ys_prec_risk.time)).T
DpYear_800_900 = pd.DataFrame(DpYear_800_900,index=(ys_prec_risk.time)).T
DpYear_900_1000 = pd.DataFrame(DpYear_900_1000,index=(ys_prec_risk.time)).T
DpYear_1000 = pd.DataFrame(DpYear_1000,index=(ys_prec_risk.time)).T

hummean_y=pd.DataFrame(hummean_y,index=(ys_hum.time)).T
humstd_y=pd.DataFrame(humstd_y,index=(ys_hum.time)).T
hummax_y=pd.DataFrame(hummax_y,index=(ys_hum.time)).T
hummin_y=pd.DataFrame(hummin_y,index=(ys_hum.time)).T
humrange_y=pd.DataFrame(humrange_y,index=(ys_hum.time)).T

mean_Hum_High_y=pd.DataFrame(mean_Hum_High_y,index=(ys_hum.time)).T
mean_Hum_Low_y=pd.DataFrame(mean_Hum_Low_y,index=(ys_hum.time)).T
min_Hum_High_y=pd.DataFrame(min_Hum_High_y,index=(ys_hum.time)).T
min_Hum_Low_y=pd.DataFrame(min_Hum_Low_y,index=(ys_hum.time)).T

t2datamean = t2datamean.add_suffix('_yearly_temp_mean')
t2datarange = t2datarange.add_suffix('_yearly_temp_range')
t2br_data_meany = t2br_data_meany.add_suffix('_yearly_temp_br4mean')
t2ega_data_meany = t2ega_data_meany.add_suffix('_yearly_temp_ega4mean')
t2egfe_data_meany = t2egfe_data_meany.add_suffix('_yearly_temp_egfe4mean')
t2mor_data_miny = t2mor_data_miny.add_suffix('_yearly_temp_mor4min')
t2mor_data_maxy = t2mor_data_maxy.add_suffix('_yearly_temp_mor4max')
t2mosdev_data_meany = t2mosdev_data_meany.add_suffix('_yearly_temp_mosdev4mean')
t2oa_data_meany = t2oa_data_meany.add_suffix('_yearly_temp_oa4mean')
t2vec_data_meany = t2vec_data_meany.add_suffix('yearly_temp_vec4mean')
t2diurnal_data_risk = t2diurnal_data_risk.add_suffix('yearly_temp_diurnal')

precmean = precmean.add_suffix('_yearly_precmean')
precstd = precstd.add_suffix('_yearly_precstd')
precmin = precmin.add_suffix('_yearly_precmin')
precmax = precmax.add_suffix('_yearly_precmax')
DpYear_0 = DpYear_0.add_suffix('_0_dly_prec_year')
DpYear_1_25 = DpYear_1_25.add_suffix('_0_dly_prec_year')
DpYear_25_50 = DpYear_25_50.add_suffix('_25_50dly_prec_year')
DpYear_50_100 = DpYear_50_100.add_suffix('_50_100dly_prec_year')
DpYear_100_200 = DpYear_100_200.add_suffix('_100_200dly_prec_year')
DpYear_200_300 = DpYear_200_300.add_suffix('_200_300dly_prec_year')
DpYear_300_400 = DpYear_300_400.add_suffix('_300_400dly_prec_year')
DpYear_400_500 = DpYear_400_500.add_suffix('_400_500dly_prec_year')
DpYear_500_600 = DpYear_500_600.add_suffix('_500_600dly_prec_year')
DpYear_600_700 = DpYear_600_700.add_suffix('_600_700dly_prec_year')
DpYear_700_800 = DpYear_700_800.add_suffix('_700_800dly_prec_year')
DpYear_800_900 = DpYear_800_900.add_suffix('_800_900dly_prec_year')
DpYear_900_1000 = DpYear_900_1000.add_suffix('_900_1000dly_prec_year')
DpYear_1000 = DpYear_1000.add_suffix('_1000_dly_prec_year')

LUC_any_dataframe = LUC_any_dataframe.add_suffix('_yearly_LUCany')
LUC_fl_dataframe = LUC_fl_dataframe.add_suffix('_yearly_LUCfl')
LUC_mdevmnat_dataframe = LUC_mdevmnat_dataframe.add_suffix('_yearly_LUC_mdevmnat')
LUC_mwet2mdry_dataframe = LUC_mwet2mdry_dataframe.add_suffix('_yearly_LUC_mwet2mdry')
LUC_mdry2mwet_dataframe = LUC_mdry2mwet_dataframe.add_suffix('_yearly_LUC_mdry2mwet')
LUC_devnat_dataframe = LUC_devnat_dataframe.add_suffix('_yearly_LUC_devnat')
LUC_difnat_dataframe = LUC_difnat_dataframe.add_suffix('_yearly_LUC_difnat')

hummean_y=hummean_y.add_suffix('_yearly_hum_mean')
humstd_y=humstd_y.add_suffix('_yearly_hum_std')
hummax_y=hummax_y.add_suffix('_yearly_hum_max')
hummin_y=hummin_y.add_suffix('_yearly_hum_min')
humrange_y=humrange_y.add_suffix('_yearly_hum_range')

mean_Hum_High_y=mean_Hum_High_y.add_suffix('_yearly_hum_mean_hd')
mean_Hum_Low_y=mean_Hum_Low_y.add_suffix('_yearly_hum_mean_ld')
min_Hum_High_y=min_Hum_High_y.add_suffix('_yearly_hum_min_hd')
min_Hum_Low_y=min_Hum_Low_y.add_suffix('_yearly_hum_min_ld')

data = [t2datarange,t2datamean,precmean,precstd,precmin,precmax,LUC_any_dataframe,LUC_fl_dataframe,
        LUC_mdevmnat_dataframe, LUC_mwet2mdry_dataframe, LUC_devnat_dataframe, LUC_difnat_dataframe,
        LUC_mdry2mwet_dataframe, t2br_data_meany, t2ega_data_meany, t2egfe_data_meany, t2mor_data_maxy,
        t2mor_data_miny, t2mosdev_data_meany, t2oa_data_meany, t2vec_data_meany,
        DpYear_0,DpYear_1_25,DpYear_25_50,DpYear_50_100,DpYear_100_200,DpYear_200_300,DpYear_300_400,
        DpYear_400_500,DpYear_500_600,DpYear_600_700,DpYear_700_800,DpYear_800_900,DpYear_900_1000,DpYear_1000,
        hummean_y,hummax_y,hummin_y,humrange_y,mean_Hum_High_y,mean_Hum_Low_y,min_Hum_Low_y,min_Hum_High_y]

datay = pd.concat(data,axis=1, sort=False, join='inner')


data_t = [datamo,datay]

data_all =  pd.concat(data,axis=1,sort=False,join='inner')

print(data_all)
