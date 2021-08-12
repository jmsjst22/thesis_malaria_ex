import os
import pandas as pd
import geopandas as gpd
import xarray as xr
import rioxarray as rx

'''

Summarising for yearly data 

Similar issue as monthly - code is repetitive and could be condensed into loops and lists using glob and explicit variable definition.

'''

# Import Uganda Districts Shapefile

districts = gpd.read_file('/home/s1987119/Diss_data/Final/Final_Products/DISTRICTS_2018_UTM_36N.shp')

# Import all netcdf data to variable

ys_temp = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/Yearly_temperature.nc', decode_coords='all')
ys_prec = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/precipitation/yearly_total_precip.nc', decode_coords='all')
ys_hum = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/humidity/humidity_yearly.nc', decode_coords='all')
ys_lucac = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/anych.nc', decode_coords='all', masked=True)

ys_lucfl = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/forestloss.nc', decode_coords='all',masked=True)
ys_difnat = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/diffnattest.nc', decode_coords='all',masked=True)
ys_devnat = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/devnat.nc', decode_coords='all',masked=True)
ys_mdevmnat = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/mdevmnat.nc', decode_coords='all',masked=True)
ys_mwet2mdry = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/mwet2mdry.nc', decode_coords='all',masked=True)
ys_mdry2mwet = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/luc/mdry2mwet.nc', decode_coords='all',masked=True)

ys_temp_br = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_biterate_transmiss.nc', decode_coords='all')
ys_temp_ega = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_ega_transmiss.nc', decode_coords='all')
ys_temp_egfe = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_egfe_transmiss.nc', decode_coords='all')
ys_temp_mor = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_mor_transmiss.nc', decode_coords='all')
ys_temp_mosdev = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_mosdev_transmiss.nc', decode_coords='all')
ys_temp_vec = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_vec_transmiss.nc', decode_coords='all')
ys_temp_oa = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_oa_transmiss.nc', decode_coords='all')

ys_temp_diu = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/temperature/yearly_diurnal_temp.nc', decode_coords='all')

ys_prec_risk = rx.open_rasterio('/home/s1987119/Diss_data/Final/Final_Products/precipitation/yearlyprecip_risk.nc',decode_coords ='all')

# Set CRS of all data

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

# Make empty dictionaries to populate with data of variables from dataset variables (netCDF)

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

# Loop through districts index of each dataset and clip with districts geometry extracting out summary statistics (mainly mean) of area.

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

   
# Make empty dataframe for variable data with geographies
LUC_any_dataframe = pd.DataFrame()
# Make an empty list for variable keys of datasets if meeting criteria
keylist = []
# Define key list as all variables and dimensions of dataset
luckeys = ys_lucac.variables.keys()
# Loop through keys
for k in luckeys:
    # Select only keys with data (not dimensions or metadata variables)
    if k.startswith('ANY'):
        # Append this to initial empty keylist
        keylist.append(k)
        # Loop through districts
        for idx,district in districts.iterrows():
            # Clip all data by districts of each variable in the dataset
            any_ch_lu[district.DName2018]=ys_lucac[k].rio.clip([district.geometry]).sum(dim=['x','y']).values
        # Append all data from above  clipping loop to single dataset
        LUC_any_dataframe=LUC_any_dataframe.append(any_ch_lu, ignore_index=True)
# Keylist is index         
idx  = pd.Index(keylist)
# Set index
LUC_any_dataframe = LUC_any_dataframe.set_index(idx)
#Transpose for rows as districts, variable data as columns
LUC_any_dataframe = LUC_any_dataframe.T

LUC_fl_dataframe = pd.DataFrame()
fkeylist = []
fluckeys = ys_lucfl.variables.keys() # keys of the netcdf for each variable
for fk in fluckeys: # loop through the variables
    if fk.startswith('loss'): #check its the right one (so I don't get latitude and longitude in my data)
        fkeylist.append(fk)
        for idx,district in districts.iterrows(): # as before, looping through the districts
            fl_lu[district.DName2018]=ys_lucfl[fk].rio.clip([district.geometry]).sum(dim=['x','y']).values
        LUC_fl_dataframe=LUC_fl_dataframe.append(fl_lu,ignore_index=True)
idx = pd.Index(fkeylist)
LUC_fl_dataframe = LUC_fl_dataframe.set_index(idx)
LUC_fl_dataframe = LUC_fl_dataframe.T

LUC_devnat_dataframe = pd.DataFrame()
dkeylist = []
devkeys = ys_devnat.variables.keys()
for dk in devkeys:
    if dk.startswith('N2D'):
        dkeylist.append(dk)
        for idx,district in districts.iterrows():
            devnat_lu[district.DName2018]=ys_devnat[dk].rio.clip([district.geometry]).sum(dim=['x','y']).values
        LUC_devnat_dataframe = LUC_devnat_dataframe.append(devnat_lu,ignore_index=True)
idx = pd.Index(dkeylist)
LUC_devnat_dataframe = LUC_devnat_dataframe.set_index(idx)
LUC_devnat_dataframe = LUC_devnat_dataframe.T


LUC_mdevmnat_dataframe = pd.DataFrame()
mdkeylist = []
mdevkeys = ys_mdevmnat.variables.keys()
for mdk in mdevkeys:
    if mdk.startswith('N2D'):
        mdkeylist.append(mdk)
        for idx,district in districts.iterrows():
            mdevmnat_lu[district.DName2018]=ys_mdevmnat[mdk].rio.clip([district.geometry]).sum(dim=['x','y']).values
        LUC_mdevmnat_dataframe = LUC_mdevmnat_dataframe.append(mdevmnat_lu,ignore_index=True)
idx = pd.Index(mdkeylist)
LUC_mdevmnat_dataframe = LUC_mdevmnat_dataframe.set_index(idx)
LUC_mdevmnat_dataframe = LUC_mdevmnat_dataframe.T


for idx,district in districts.iterrows():
    difnat_lu[district.DName2018]=ys_difnat.rio.clip([district.geometry]).sum(dim=['x','y']).values
    LUC_difnat_dataframe = pd.DataFrame(difnat_lu).T


# Add suffix to identify variables in column
   
LUC_any_dataframe = LUC_any_dataframe.add_suffix('_yearly_LUCany')
LUC_fl_dataframe = LUC_fl_dataframe.add_suffix('_yearly_LUCfl')
LUC_mdevmnat_dataframe = LUC_mdevmnat_dataframe.add_suffix('_yearly_LUC_mdevmnat')
LUC_devnat_dataframe = LUC_devnat_dataframe.add_suffix('_yearly_LUC_devnat')
LUC_difnat_dataframe = LUC_difnat_dataframe.add_suffix('_yearly_LUC_difnat')



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

# List data variables

data = [t2datarange,t2datamean,precmean,precstd,precmin,precmax,LUC_any_dataframe,LUC_fl_dataframe,
        LUC_mdevmnat_dataframe, LUC_mwet2mdry_dataframe, LUC_devnat_dataframe, LUC_difnat_dataframe,
        LUC_mdry2mwet_dataframe, t2br_data_meany, t2ega_data_meany, t2egfe_data_meany, t2mor_data_maxy,
        t2mor_data_miny, t2mosdev_data_meany, t2oa_data_meany, t2vec_data_meany,
        DpYear_0,DpYear_1_25,DpYear_25_50,DpYear_50_100,DpYear_100_200,DpYear_200_300,DpYear_300_400,
        DpYear_400_500,DpYear_500_600,DpYear_600_700,DpYear_700_800,DpYear_800_900,DpYear_900_1000,DpYear_1000,
        hummean_y,hummax_y,hummin_y,humrange_y,mean_Hum_High_y,mean_Hum_Low_y,min_Hum_Low_y,min_Hum_High_y,t2diurnal_data_risk]

# Concatenate data variables

datac = pd.concat(data,axis=1, sort=False, join='inner')

# Get selected years

years = [2008,2009,2013,2014,2015,2016,2017,2018,2019]

# Parse into individual dataset

for year in years:
    filter_col = [col for col in datac if col.startswith(str(year))]
    data = datac[filter_col]
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('env_csv/'+str(year)+'_env.csv')


