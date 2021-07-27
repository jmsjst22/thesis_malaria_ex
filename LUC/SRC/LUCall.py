import xarray as xr
import numpy as np

'''

Intent
Characterises different types of change between land use classes at a yearly rate, with overall change counts characterised in study period to capture overall activity.

Main output includes land use change layers, information on land use change is explicit in variable name and file title and is not held in netCDF data variable values.

Requirements
All files in netCDF format, reindexed to unified grid, clipped to identical extents and stored in a directory per data source. It is also necessary to reproject the MODIS data
as data is in sinusoidal projection

Categorisations are correct for data downloaded 04/21. Update may be required from documentation and should be sense-checked before code
run to avoid errors

Information on categorisations and continued use and suitability of data as a means of comparing year to year change, for change of different kinds is stored at
documentation tabs for Copernicus (FAO) and Google Earth Engine (MODIS), respectively:

https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-land-cover?tab=doc
https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MCD12Q1

Classifications, to the best of the authors' ability, accommodate for errors and limitations of the datasets used, as discussed in the research and technical docuemnts.

Authored by James Tomlinson

'''

dir = '/home/s1987119/Diss_data/Final/LUC/Process/regrid/'
dir2 = '/home/s1987119/Diss_data/Final/LUC/Process/reprojectednc/'

#LUC Land Cover FAO Categorisation
natural = np.array([int(50),int(60),int(61),int(62),int(70),int(71),int(72),int(80),int(81),int(82),int(90),int(100),int(110),int(120),int(121),int(122),int(130),int(140),int(150),int(151),int(152),int(153),int(160),int(170),int(180),int(200),int(201),int(202),int(210),int(220)])
devl = [int(10),int(11),int(12),int(20),int(30),int(40),int(200),int(201),int(202),int(190)]
dry = [int(10),int(11),int(12),30,40,50,int(60),int(61),int(62),int(70),int(71),int(72),int(80),int(81),int(82),90,100,110,int(120),int(121),int(122),130,150,int(151),int(152),int(153),190,int(200),int(201),int(202)]
wet = [20,140,160,170,180,210]



#LUC Land Cover MODIS categorisation
mnatural = [1,2,3,4,5,6,7,8,9,10,11,]
mdevl = [12,13,14]
Mdisr = [16]
mdry = [1,2,3,4,5,6,7,8,9,10,12,13,14,16]
mwet = [11,17]
mdense = [1,2,3,4,5,6,8]
Msparse = [7,8,9,10,13,14,16]


#Open netCDF files and assign to variable per year, L2004 and WI2019 include change counts; FAO landuse categorisation
L2004 = xr.open_dataset(dir+'2004_LUC_clippedWI.nc')
L2005 = xr.open_dataset(dir+'regridded_LUC05.nc')
L2006 = xr.open_dataset(dir+'regridded_LUC06.nc')
L2007 = xr.open_dataset(dir+'regridded_LUC07.nc')
L2008 = xr.open_dataset(dir+'regridded_LUC08.nc')
L2009 = xr.open_dataset(dir+'regridded_LUC09.nc')
L2010 = xr.open_dataset(dir+'regridded_LUC10.nc')
L2011 = xr.open_dataset(dir+'regridded_LUC11.nc')
L2012 = xr.open_dataset(dir+'regridded_LUC12.nc')
L2013 = xr.open_dataset(dir+'regridded_LUC13.nc')
L2014 = xr.open_dataset(dir+'regridded_LUC14.nc')
L2015 = xr.open_dataset(dir+'regridded_LUC15.nc')
L2016 = xr.open_dataset(dir+'regridded_LUC16.nc')
L2017 = xr.open_dataset(dir+'regridded_LUC17.nc')
L2018 = xr.open_dataset(dir+'regridded_LUC18.nc')
L2019 = xr.open_dataset(dir+'regridded_LUC19.nc')
WI2019 = xr.open_dataset(dir+'regridded_LUC_19_wi.nc')

#Open netCDF files and assign to variable per year, L2004 and WI2019 include change counts; MODIS landuse categorisation
ML2003 = xr.open_dataset(dir2+'landcover_MODIS2003proj.nc')
ML2004 = xr.open_dataset(dir2+'landcover_MODIS2004proj.nc')
ML2005 = xr.open_dataset(dir2+'landcover_MODIS2005proj.nc')
ML2006 = xr.open_dataset(dir2+'landcover_MODIS2006proj.nc')
ML2007 = xr.open_dataset(dir2+'landcover_MODIS2007proj.nc')
ML2008 = xr.open_dataset(dir2+'landcover_MODIS2008proj.nc')
ML2009 = xr.open_dataset(dir2+'landcover_MODIS2009proj.nc')
ML2010 = xr.open_dataset(dir2+'landcover_MODIS2010proj.nc')
ML2011 = xr.open_dataset(dir2+'landcover_MODIS2011proj.nc')
ML2012 = xr.open_dataset(dir2+'landcover_MODIS2012proj.nc')
ML2013 = xr.open_dataset(dir2+'landcover_MODIS2013proj.nc')
ML2014 = xr.open_dataset(dir2+'landcover_MODIS2014proj.nc')
ML2015 = xr.open_dataset(dir2+'landcover_MODIS2015proj.nc')
ML2016 = xr.open_dataset(dir2+'landcover_MODIS2016proj.nc')
ML2017 = xr.open_dataset(dir2+'landcover_MODIS2017proj.nc')
ML2018 = xr.open_dataset(dir2+'landcover_MODIS2018proj.nc')
ML2019 = xr.open_dataset(dir2+'newer19.nc')

#Assign data of netCDF variable indicating land use class to python variable for analysis
LV2004 = L2004['lccs_class']
LV2005 = L2005['lccs_class']
LV2006 = L2006['lccs_class']
LV2007 = L2007['lccs_class']
LV2008 = L2008['lccs_class']
LV2009 = L2009['lccs_class']
LV2010 = L2010['lccs_class']
LV2011 = L2011['lccs_class']
LV2012 = L2012['lccs_class']
LV2013 = L2013['lccs_class']
LV2014 = L2014['lccs_class']
LV2015 = L2015['lccs_class']
LV2016 = L2016['lccs_class']
LV2017 = L2017['lccs_class']
LV2018 = L2018['lccs_class']
LV2019 = L2019['lccs_class']

MLV2003 = ML2003['Band1']
MLV2004 = ML2004['Band1']
MLV2005 = ML2005['Band1']
MLV2006 = ML2006['Band1']
MLV2007 = ML2007['Band1']
MLV2008 = ML2008['Band1']
MLV2009 = ML2009['Band1']
MLV2010 = ML2010['Band1']
MLV2011 = ML2011['Band1']
MLV2012 = ML2012['Band1']
MLV2013 = ML2013['Band1']
MLV2014 = ML2014['Band1']
MLV2015 = ML2015['Band1']
MLV2016 = ML2016['Band1']
MLV2017 = ML2017['Band1']
MLV2018 = ML2018['Band1']
MLV2019 = ML2019['Band1']

C2004 = L2004['change_count']
C2019 = WI2019['change_count']

#Find change occurring for all locations between 2004 and 2019 by variable subtracting (coordinate against coordinate if regridded correctly)
diffnat = C2019 - C2004

#build netcdf for overall difference layer
diffnat = xr.Dataset({'diffnat': diffnat})
diffnat.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/diffnattest.nc')

#For FAO category data: test whether element of variable indicating land use per location is identical to any land use type in "natural" (not developed or expicitly perturbed) category
nat2004 = xr.DataArray(np.in1d(LV2004,natural).reshape(LV2004.shape), dims=LV2004.dims, coords=LV2004.coords)
nat2005 = xr.DataArray(np.in1d(LV2005,natural).reshape(LV2005.shape), dims=LV2005.dims, coords=LV2005.coords)
nat2006 = xr.DataArray(np.in1d(LV2006,natural).reshape(LV2006.shape), dims=LV2006.dims, coords=LV2006.coords)
nat2007 = xr.DataArray(np.in1d(LV2007,natural).reshape(LV2007.shape), dims=LV2007.dims, coords=LV2007.coords)
nat2008 = xr.DataArray(np.in1d(LV2008,natural).reshape(LV2008.shape), dims=LV2008.dims, coords=LV2008.coords)
nat2009 = xr.DataArray(np.in1d(LV2009,natural).reshape(LV2009.shape), dims=LV2009.dims, coords=LV2009.coords)
nat2010 = xr.DataArray(np.in1d(LV2010,natural).reshape(LV2010.shape), dims=LV2010.dims, coords=LV2010.coords)
nat2011 = xr.DataArray(np.in1d(LV2011,natural).reshape(LV2011.shape), dims=LV2011.dims, coords=LV2011.coords)
nat2012 = xr.DataArray(np.in1d(LV2012,natural).reshape(LV2012.shape), dims=LV2012.dims, coords=LV2012.coords)
nat2013 = xr.DataArray(np.in1d(LV2013,natural).reshape(LV2013.shape), dims=LV2013.dims, coords=LV2013.coords)
nat2014 = xr.DataArray(np.in1d(LV2014,natural).reshape(LV2014.shape), dims=LV2014.dims, coords=LV2014.coords)
nat2015 = xr.DataArray(np.in1d(LV2015,natural).reshape(LV2015.shape), dims=LV2015.dims, coords=LV2015.coords)
nat2016 = xr.DataArray(np.in1d(LV2016,natural).reshape(LV2016.shape), dims=LV2016.dims, coords=LV2016.coords)
nat2017 = xr.DataArray(np.in1d(LV2017,natural).reshape(LV2017.shape), dims=LV2017.dims, coords=LV2017.coords)
nat2018 = xr.DataArray(np.in1d(LV2018,natural).reshape(LV2018.shape), dims=LV2018.dims, coords=LV2018.coords)
nat2019 = xr.DataArray(np.in1d(LV2019,natural).reshape(LV2019.shape), dims=LV2019.dims, coords=LV2019.coords)


#For FAO category data: test whether element of variable indicating land use per location is identical to any land use type in "developed" (developed or expicitly perturbed) category
dev2005 = xr.DataArray(np.in1d(LV2005,devl).reshape(LV2005.shape), dims=LV2005.dims, coords=LV2005.coords)
dev2006 = xr.DataArray(np.in1d(LV2006,devl).reshape(LV2006.shape), dims=LV2006.dims, coords=LV2006.coords)
dev2007 = xr.DataArray(np.in1d(LV2007,devl).reshape(LV2007.shape), dims=LV2007.dims, coords=LV2007.coords)
dev2008 = xr.DataArray(np.in1d(LV2008,devl).reshape(LV2008.shape), dims=LV2008.dims, coords=LV2008.coords)
dev2009 = xr.DataArray(np.in1d(LV2009,devl).reshape(LV2009.shape), dims=LV2009.dims, coords=LV2009.coords)
dev2010 = xr.DataArray(np.in1d(LV2010,devl).reshape(LV2010.shape), dims=LV2010.dims, coords=LV2010.coords)
dev2011 = xr.DataArray(np.in1d(LV2011,devl).reshape(LV2011.shape), dims=LV2011.dims, coords=LV2011.coords)
dev2012 = xr.DataArray(np.in1d(LV2012,devl).reshape(LV2012.shape), dims=LV2012.dims, coords=LV2012.coords)
dev2013 = xr.DataArray(np.in1d(LV2013,devl).reshape(LV2013.shape), dims=LV2013.dims, coords=LV2013.coords)
dev2014 = xr.DataArray(np.in1d(LV2014,devl).reshape(LV2014.shape), dims=LV2014.dims, coords=LV2014.coords)
dev2015 = xr.DataArray(np.in1d(LV2015,devl).reshape(LV2015.shape), dims=LV2015.dims, coords=LV2015.coords)
dev2016 = xr.DataArray(np.in1d(LV2016,devl).reshape(LV2016.shape), dims=LV2016.dims, coords=LV2016.coords)
dev2017 = xr.DataArray(np.in1d(LV2017,devl).reshape(LV2017.shape), dims=LV2017.dims, coords=LV2017.coords)
dev2018 = xr.DataArray(np.in1d(LV2018,devl).reshape(LV2018.shape), dims=LV2018.dims, coords=LV2018.coords)
dev2019 = xr.DataArray(np.in1d(LV2019,devl).reshape(LV2019.shape), dims=LV2019.dims, coords=LV2019.coords)

#For MODIS category data: test whether element of variable indicating land use per location is identical to any land use type in "natural" (not developed or expicitly perturbed) category
mnat2003 = xr.DataArray(np.in1d(MLV2003,mnatural).reshape(MLV2003.shape), dims=MLV2003.dims, coords=MLV2004.coords)
mnat2004 = xr.DataArray(np.in1d(MLV2004,mnatural).reshape(MLV2004.shape), dims=MLV2004.dims, coords=MLV2004.coords)
mnat2005 = xr.DataArray(np.in1d(MLV2005,mnatural).reshape(MLV2005.shape), dims=MLV2005.dims, coords=MLV2005.coords)
mnat2006 = xr.DataArray(np.in1d(MLV2006,mnatural).reshape(MLV2006.shape), dims=MLV2006.dims, coords=MLV2006.coords)
mnat2007 = xr.DataArray(np.in1d(MLV2007,mnatural).reshape(MLV2007.shape), dims=MLV2007.dims, coords=MLV2007.coords)
mnat2008 = xr.DataArray(np.in1d(MLV2008,mnatural).reshape(MLV2008.shape), dims=MLV2008.dims, coords=MLV2008.coords)
mnat2009 = xr.DataArray(np.in1d(MLV2009,mnatural).reshape(MLV2009.shape), dims=MLV2009.dims, coords=MLV2009.coords)
mnat2010 = xr.DataArray(np.in1d(MLV2010,mnatural).reshape(MLV2010.shape), dims=MLV2010.dims, coords=MLV2010.coords)
mnat2011 = xr.DataArray(np.in1d(MLV2011,mnatural).reshape(MLV2011.shape), dims=MLV2011.dims, coords=MLV2011.coords)
mnat2012 = xr.DataArray(np.in1d(MLV2012,mnatural).reshape(MLV2012.shape), dims=MLV2012.dims, coords=MLV2012.coords)
mnat2013 = xr.DataArray(np.in1d(MLV2013,mnatural).reshape(MLV2013.shape), dims=MLV2013.dims, coords=MLV2013.coords)
mnat2014 = xr.DataArray(np.in1d(MLV2014,mnatural).reshape(MLV2014.shape), dims=MLV2014.dims, coords=MLV2014.coords)
mnat2015 = xr.DataArray(np.in1d(MLV2015,mnatural).reshape(MLV2015.shape), dims=MLV2015.dims, coords=MLV2015.coords)
mnat2016 = xr.DataArray(np.in1d(MLV2016,mnatural).reshape(MLV2016.shape), dims=MLV2016.dims, coords=MLV2016.coords)
mnat2017 = xr.DataArray(np.in1d(MLV2017,mnatural).reshape(MLV2017.shape), dims=MLV2017.dims, coords=MLV2017.coords)
mnat2018 = xr.DataArray(np.in1d(MLV2018,mnatural).reshape(MLV2018.shape), dims=MLV2018.dims, coords=MLV2018.coords)
mnat2019 = xr.DataArray(np.in1d(MLV2019,mnatural).reshape(MLV2019.shape), dims=MLV2019.dims, coords=MLV2019.coords)

#For MODIS category data: test whether element of variable indicating land use per location is identical to any land use type in "developed" (not developed or expicitly perturbed) category
mdev2004 = xr.DataArray(np.in1d(MLV2004,mdevl).reshape(MLV2004.shape), dims=MLV2004.dims, coords=MLV2004.coords)
mdev2005 = xr.DataArray(np.in1d(MLV2005,mdevl).reshape(MLV2005.shape), dims=MLV2005.dims, coords=MLV2005.coords)
mdev2006 = xr.DataArray(np.in1d(MLV2006,mdevl).reshape(MLV2006.shape), dims=MLV2006.dims, coords=MLV2006.coords)
mdev2007 = xr.DataArray(np.in1d(MLV2007,mdevl).reshape(MLV2007.shape), dims=MLV2007.dims, coords=MLV2007.coords)
mdev2008 = xr.DataArray(np.in1d(MLV2008,mdevl).reshape(MLV2008.shape), dims=MLV2008.dims, coords=MLV2008.coords)
mdev2009 = xr.DataArray(np.in1d(MLV2009,mdevl).reshape(MLV2009.shape), dims=MLV2009.dims, coords=MLV2009.coords)
mdev2010 = xr.DataArray(np.in1d(MLV2010,mdevl).reshape(MLV2010.shape), dims=MLV2010.dims, coords=MLV2010.coords)
mdev2011 = xr.DataArray(np.in1d(MLV2011,mdevl).reshape(MLV2011.shape), dims=MLV2011.dims, coords=MLV2011.coords)
mdev2012 = xr.DataArray(np.in1d(MLV2012,mdevl).reshape(MLV2012.shape), dims=MLV2012.dims, coords=MLV2012.coords)
mdev2013 = xr.DataArray(np.in1d(MLV2013,mdevl).reshape(MLV2013.shape), dims=MLV2013.dims, coords=MLV2013.coords)
mdev2014 = xr.DataArray(np.in1d(MLV2014,mdevl).reshape(MLV2014.shape), dims=MLV2014.dims, coords=MLV2014.coords)
mdev2015 = xr.DataArray(np.in1d(MLV2015,mdevl).reshape(MLV2015.shape), dims=MLV2015.dims, coords=MLV2015.coords)
mdev2016 = xr.DataArray(np.in1d(MLV2016,mdevl).reshape(MLV2016.shape), dims=MLV2016.dims, coords=MLV2016.coords)
mdev2017 = xr.DataArray(np.in1d(MLV2017,mdevl).reshape(MLV2017.shape), dims=MLV2017.dims, coords=MLV2017.coords)
mdev2018 = xr.DataArray(np.in1d(MLV2018,mdevl).reshape(MLV2018.shape), dims=MLV2018.dims, coords=MLV2018.coords)
mdev2019 = xr.DataArray(np.in1d(MLV2019,mdevl).reshape(MLV2019.shape), dims=MLV2019.dims, coords=MLV2019.coords)

#For FAO category data: test whether element of variable indicating land use per location is identical to any land use type in "dry" (permanently not inundated or marsh) category
dry2004 = xr.DataArray(np.in1d(LV2004,dry).reshape(LV2004.shape), dims=LV2004.dims, coords=LV2004.coords)
dry2005 = xr.DataArray(np.in1d(LV2005,dry).reshape(LV2005.shape), dims=LV2005.dims, coords=LV2005.coords)
dry2006 = xr.DataArray(np.in1d(LV2006,dry).reshape(LV2006.shape), dims=LV2006.dims, coords=LV2006.coords)
dry2007 = xr.DataArray(np.in1d(LV2007,dry).reshape(LV2007.shape), dims=LV2007.dims, coords=LV2007.coords)
dry2008 = xr.DataArray(np.in1d(LV2008,dry).reshape(LV2008.shape), dims=LV2008.dims, coords=LV2008.coords)
dry2009 = xr.DataArray(np.in1d(LV2009,dry).reshape(LV2009.shape), dims=LV2009.dims, coords=LV2009.coords)
dry2010 = xr.DataArray(np.in1d(LV2010,dry).reshape(LV2010.shape), dims=LV2010.dims, coords=LV2010.coords)
dry2011 = xr.DataArray(np.in1d(LV2011,dry).reshape(LV2011.shape), dims=LV2011.dims, coords=LV2011.coords)
dry2012 = xr.DataArray(np.in1d(LV2012,dry).reshape(LV2012.shape), dims=LV2012.dims, coords=LV2012.coords)
dry2013 = xr.DataArray(np.in1d(LV2013,dry).reshape(LV2013.shape), dims=LV2013.dims, coords=LV2013.coords)
dry2014 = xr.DataArray(np.in1d(LV2014,dry).reshape(LV2014.shape), dims=LV2014.dims, coords=LV2014.coords)
dry2015 = xr.DataArray(np.in1d(LV2015,dry).reshape(LV2015.shape), dims=LV2015.dims, coords=LV2015.coords)
dry2016 = xr.DataArray(np.in1d(LV2016,dry).reshape(LV2016.shape), dims=LV2016.dims, coords=LV2016.coords)
dry2017 = xr.DataArray(np.in1d(LV2017,dry).reshape(LV2017.shape), dims=LV2017.dims, coords=LV2017.coords)
dry2018 = xr.DataArray(np.in1d(LV2018,dry).reshape(LV2018.shape), dims=LV2018.dims, coords=LV2018.coords)
dry2019 = xr.DataArray(np.in1d(LV2019,dry).reshape(LV2019.shape), dims=LV2019.dims, coords=LV2019.coords)

#For FAO category data: test whether element of variable indicating land use per location is identical to any land use type in "wet" (permanently inundated or marsh) category
wet2004 = xr.DataArray(np.in1d(LV2004,wet).reshape(LV2004.shape), dims=LV2004.dims, coords=LV2004.coords)
wet2005 = xr.DataArray(np.in1d(LV2005,wet).reshape(LV2005.shape), dims=LV2005.dims, coords=LV2005.coords)
wet2006 = xr.DataArray(np.in1d(LV2006,wet).reshape(LV2006.shape), dims=LV2006.dims, coords=LV2006.coords)
wet2007 = xr.DataArray(np.in1d(LV2007,wet).reshape(LV2007.shape), dims=LV2007.dims, coords=LV2007.coords)
wet2008 = xr.DataArray(np.in1d(LV2008,wet).reshape(LV2008.shape), dims=LV2008.dims, coords=LV2008.coords)
wet2009 = xr.DataArray(np.in1d(LV2009,wet).reshape(LV2009.shape), dims=LV2009.dims, coords=LV2009.coords)
wet2010 = xr.DataArray(np.in1d(LV2010,wet).reshape(LV2010.shape), dims=LV2010.dims, coords=LV2010.coords)
wet2011 = xr.DataArray(np.in1d(LV2011,wet).reshape(LV2011.shape), dims=LV2011.dims, coords=LV2011.coords)
wet2012 = xr.DataArray(np.in1d(LV2012,wet).reshape(LV2012.shape), dims=LV2012.dims, coords=LV2012.coords)
wet2013 = xr.DataArray(np.in1d(LV2013,wet).reshape(LV2013.shape), dims=LV2013.dims, coords=LV2013.coords)
wet2014 = xr.DataArray(np.in1d(LV2014,wet).reshape(LV2014.shape), dims=LV2014.dims, coords=LV2014.coords)
wet2015 = xr.DataArray(np.in1d(LV2015,wet).reshape(LV2015.shape), dims=LV2015.dims, coords=LV2015.coords)
wet2016 = xr.DataArray(np.in1d(LV2016,wet).reshape(LV2016.shape), dims=LV2016.dims, coords=LV2016.coords)
wet2017 = xr.DataArray(np.in1d(LV2017,wet).reshape(LV2017.shape), dims=LV2017.dims, coords=LV2017.coords)
wet2018 = xr.DataArray(np.in1d(LV2018,wet).reshape(LV2018.shape), dims=LV2018.dims, coords=LV2018.coords)
wet2019 = xr.DataArray(np.in1d(LV2019,wet).reshape(LV2019.shape), dims=LV2019.dims, coords=LV2019.coords)

#For MODIS category data: test whether element of variable indicating land use per location is identical to any land use type in "dry" (permanently not inundated or marsh) category
mdry2003 = xr.DataArray(np.in1d(MLV2003,mdry).reshape(MLV2003.shape), dims=MLV2003.dims, coords=MLV2003.coords)
mdry2004 = xr.DataArray(np.in1d(MLV2004,mdry).reshape(MLV2004.shape), dims=MLV2004.dims, coords=MLV2004.coords)
mdry2005 = xr.DataArray(np.in1d(MLV2005,mdry).reshape(MLV2005.shape), dims=MLV2005.dims, coords=MLV2005.coords)
mdry2006 = xr.DataArray(np.in1d(MLV2006,mdry).reshape(MLV2006.shape), dims=MLV2006.dims, coords=MLV2006.coords)
mdry2007 = xr.DataArray(np.in1d(MLV2007,mdry).reshape(MLV2007.shape), dims=MLV2007.dims, coords=MLV2007.coords)
mdry2008 = xr.DataArray(np.in1d(MLV2008,mdry).reshape(MLV2008.shape), dims=MLV2008.dims, coords=MLV2008.coords)
mdry2009 = xr.DataArray(np.in1d(MLV2009,mdry).reshape(MLV2009.shape), dims=MLV2009.dims, coords=MLV2009.coords)
mdry2010 = xr.DataArray(np.in1d(MLV2010,mdry).reshape(MLV2010.shape), dims=MLV2010.dims, coords=MLV2010.coords)
mdry2011 = xr.DataArray(np.in1d(MLV2011,mdry).reshape(MLV2011.shape), dims=MLV2011.dims, coords=MLV2011.coords)
mdry2012 = xr.DataArray(np.in1d(MLV2012,mdry).reshape(MLV2012.shape), dims=MLV2012.dims, coords=MLV2012.coords)
mdry2013 = xr.DataArray(np.in1d(MLV2013,mdry).reshape(MLV2013.shape), dims=MLV2013.dims, coords=MLV2013.coords)
mdry2014 = xr.DataArray(np.in1d(MLV2014,mdry).reshape(MLV2014.shape), dims=MLV2014.dims, coords=MLV2014.coords)
mdry2015 = xr.DataArray(np.in1d(MLV2015,mdry).reshape(MLV2015.shape), dims=MLV2015.dims, coords=MLV2015.coords)
mdry2016 = xr.DataArray(np.in1d(MLV2016,mdry).reshape(MLV2016.shape), dims=MLV2016.dims, coords=MLV2016.coords)
mdry2017 = xr.DataArray(np.in1d(MLV2017,mdry).reshape(MLV2017.shape), dims=MLV2017.dims, coords=MLV2017.coords)
mdry2018 = xr.DataArray(np.in1d(MLV2018,mdry).reshape(MLV2018.shape), dims=MLV2018.dims, coords=MLV2018.coords)
mdry2019 = xr.DataArray(np.in1d(MLV2019,mdry).reshape(MLV2019.shape), dims=MLV2019.dims, coords=MLV2019.coords)

#For MODIS category data: test whether element of variable indicating land use per location is identical to any land use type in "wet" (permanently inundated or marsh) category
mwet2003 = xr.DataArray(np.in1d(MLV2003,mwet).reshape(MLV2003.shape), dims=MLV2003.dims, coords=MLV2003.coords)
mwet2004 = xr.DataArray(np.in1d(MLV2004,mwet).reshape(MLV2004.shape), dims=MLV2004.dims, coords=MLV2004.coords)
mwet2005 = xr.DataArray(np.in1d(MLV2005,mwet).reshape(MLV2005.shape), dims=MLV2005.dims, coords=MLV2005.coords)
mwet2006 = xr.DataArray(np.in1d(MLV2006,mwet).reshape(MLV2006.shape), dims=MLV2006.dims, coords=MLV2006.coords)
mwet2007 = xr.DataArray(np.in1d(MLV2007,mwet).reshape(MLV2007.shape), dims=MLV2007.dims, coords=MLV2007.coords)
mwet2008 = xr.DataArray(np.in1d(MLV2008,mwet).reshape(MLV2008.shape), dims=MLV2008.dims, coords=MLV2008.coords)
mwet2009 = xr.DataArray(np.in1d(MLV2009,mwet).reshape(MLV2009.shape), dims=MLV2009.dims, coords=MLV2009.coords)
mwet2010 = xr.DataArray(np.in1d(MLV2010,mwet).reshape(MLV2010.shape), dims=MLV2010.dims, coords=MLV2010.coords)
mwet2011 = xr.DataArray(np.in1d(MLV2011,mwet).reshape(MLV2011.shape), dims=MLV2011.dims, coords=MLV2011.coords)
mwet2012 = xr.DataArray(np.in1d(MLV2012,mwet).reshape(MLV2012.shape), dims=MLV2012.dims, coords=MLV2012.coords)
mwet2013 = xr.DataArray(np.in1d(MLV2013,mwet).reshape(MLV2013.shape), dims=MLV2013.dims, coords=MLV2013.coords)
mwet2014 = xr.DataArray(np.in1d(MLV2014,mwet).reshape(MLV2014.shape), dims=MLV2014.dims, coords=MLV2014.coords)
mwet2015 = xr.DataArray(np.in1d(MLV2015,mwet).reshape(MLV2015.shape), dims=MLV2015.dims, coords=MLV2015.coords)
mwet2016 = xr.DataArray(np.in1d(MLV2016,mwet).reshape(MLV2016.shape), dims=MLV2016.dims, coords=MLV2016.coords)
mwet2017 = xr.DataArray(np.in1d(MLV2017,mwet).reshape(MLV2017.shape), dims=MLV2017.dims, coords=MLV2017.coords)
mwet2018 = xr.DataArray(np.in1d(MLV2018,mwet).reshape(MLV2018.shape), dims=MLV2018.dims, coords=MLV2018.coords)
mwet2019 = xr.DataArray(np.in1d(MLV2019,mwet).reshape(MLV2019.shape), dims=MLV2019.dims, coords=MLV2019.coords)

#For FAO category of wet and dry: test whether there has been a yearly dry to wet change to indicate natural flooding, irrigation or otherwise inundation
wetdry_0405 = xr.where((dry2004)&(wet2005),1,0)
wetdry_0506 = xr.where((dry2005)&(wet2006),1,0)
wetdry_0607 = xr.where((dry2006)&(wet2007),1,0)
wetdry_0708 = xr.where((dry2007)&(wet2008),1,0)
wetdry_0809 = xr.where((dry2008)&(wet2009),1,0)
wetdry_0910 = xr.where((dry2009)&(wet2010),1,0)
wetdry_1011 = xr.where((dry2010)&(wet2011),1,0)
wetdry_1112 = xr.where((dry2011)&(wet2012),1,0)
wetdry_1213 = xr.where((dry2012)&(wet2013),1,0)
wetdry_1314 = xr.where((dry2013)&(wet2014),1,0)
wetdry_1415 = xr.where((dry2014)&(wet2015),1,0)
wetdry_1516 = xr.where((dry2015)&(wet2016),1,0)
wetdry_1617 = xr.where((dry2016)&(wet2017),1,0)
wetdry_1718 = xr.where((dry2017)&(wet2018),1,0)
wetdry_1819 = xr.where((dry2018)&(wet2019),1,0)

#Build netcdf for FAO category wet to dry change
wetdry = xr.Dataset({'IIF_0405': wetdry_0405,'IIF_0506': wetdry_0506, 'IIF_0607': wetdry_0607, 'IIF_0708': wetdry_0708, 'IIF_0809': wetdry_0809, 'IIF_0910': wetdry_0910, 'IIF_1011': wetdry_1011, 'IIF_1112': wetdry_1112, 'IIF_1213': wetdry_1213, 'IIF_1314': wetdry_1314, 'IIF_1415': wetdry_1415, 'IIF_1516': wetdry_1516, 'IIF_1617': wetdry_1617, 'IIF_1718': wetdry_1718, 'IIF_1819': wetdry_1819})
wetdry.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/dry2wet.nc')

# For MODIS category of wet and dry: test whether there has been a yearly dry to wet change to indicate natural flooding, irrigation or otherwise inundation
mwetmdry_0304 = xr.where((mdry2003)&(mwet2004),1,0)
mwetmdry_0405 = xr.where((mdry2004)&(mwet2005),1,0)
mwetmdry_0506 = xr.where((mdry2005)&(mwet2006),1,0)
mwetmdry_0607 = xr.where((mdry2006)&(mwet2007),1,0)
mwetmdry_0708 = xr.where((mdry2007)&(mwet2008),1,0)
mwetmdry_0809 = xr.where((mdry2008)&(mwet2009),1,0)
mwetmdry_0910 = xr.where((mdry2009)&(mwet2010),1,0)
mwetmdry_1011 = xr.where((mdry2010)&(mwet2011),1,0)
mwetmdry_1112 = xr.where((mdry2011)&(mwet2012),1,0)
mwetmdry_1213 = xr.where((mdry2012)&(mwet2013),1,0)
mwetmdry_1314 = xr.where((mdry2013)&(mwet2014),1,0)
mwetmdry_1415 = xr.where((mdry2014)&(mwet2015),1,0)
mwetmdry_1516 = xr.where((mdry2015)&(mwet2016),1,0)
mwetmdry_1617 = xr.where((mdry2016)&(mwet2017),1,0)
mwetmdry_1718 = xr.where((mdry2017)&(mwet2018),1,0)
mwetmdry_1819 = xr.where((mdry2018)&(mwet2019),1,0)

#Build netcdf for MODIS category wet to dry change
mwetmdry = xr.Dataset({'IIF_0405': mwetmdry_0405,'IIF_0506': mwetmdry_0506, 'IIF_0607': mwetmdry_0607, 'IIF_0708': mwetmdry_0708, 'IIF_0809': mwetmdry_0809, 'IIF_0910': mwetmdry_0910, 'IIF_1011': mwetmdry_1011, 'IIF_1112': mwetmdry_1112, 'IIF_1213': mwetmdry_1213, 'IIF_1314': mwetmdry_1314, 'IIF_1415': mwetmdry_1415, 'IIF_1516': mwetmdry_1516, 'IIF_1617': mwetmdry_1617, 'IIF_1718': mwetmdry_1718, 'IIF_1819': mwetmdry_1819})
mwetmdry.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/mdry2mwet.nc')

#For FAO category: test whether there has been a yearly wet to dry change to indicate droughting, draining or reduction and ceasing of previously wet land, river basin or marsh
drywet_0405 = xr.where((wet2004)&(dry2005),1,0)
drywet_0506 = xr.where((wet2005)&(dry2006),1,0)
drywet_0607 = xr.where((wet2006)&(dry2007),1,0)
drywet_0708 = xr.where((wet2007)&(dry2008),1,0)
drywet_0809 = xr.where((wet2008)&(dry2009),1,0)
drywet_0910 = xr.where((wet2009)&(dry2010),1,0)
drywet_1011 = xr.where((wet2010)&(dry2011),1,0)
drywet_1112 = xr.where((wet2011)&(dry2012),1,0)
drywet_1213 = xr.where((wet2012)&(dry2013),1,0)
drywet_1314 = xr.where((wet2013)&(dry2014),1,0)
drywet_1415 = xr.where((wet2014)&(dry2015),1,0)
drywet_1516 = xr.where((wet2015)&(dry2016),1,0)
drywet_1617 = xr.where((wet2016)&(dry2017),1,0)
drywet_1718 = xr.where((wet2017)&(dry2018),1,0)
drywet_1819 = xr.where((wet2018)&(dry2019),1,0)

#Build netcdf for FAO category dry to wet change
drywet = xr.Dataset({'D_0405': drywet_0405,'D_0506': drywet_0506, 'D_0607': drywet_0607, 'D_0708': drywet_0708, 'D_0809': drywet_0809, 'D_0910': drywet_0910, 'D_1011': drywet_1011, 'D_1112': drywet_1112, 'D_1213': drywet_1213, 'D_1314': drywet_1314, 'D_1415': drywet_1415, 'D_1516': drywet_1516, 'D_1617': drywet_1617, 'D_1718': drywet_1718, 'D_1819': drywet_1819})
drywet.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/wet2dry.nc')

#For MODIS category: test whether there has been a yearly wet to dry change to indicate droughting, draining or reduction and ceasing of previously wet land, river basin or marsh
mdrymwet_0405 = xr.where((mwet2004)&(mdry2005),1,0)
mdrymwet_0506 = xr.where((mwet2005)&(mdry2006),1,0)
mdrymwet_0607 = xr.where((mwet2006)&(mdry2007),1,0)
mdrymwet_0708 = xr.where((mwet2007)&(mdry2008),1,0)
mdrymwet_0809 = xr.where((mwet2008)&(mdry2009),1,0)
mdrymwet_0910 = xr.where((mwet2009)&(mdry2010),1,0)
mdrymwet_1011 = xr.where((mwet2010)&(mdry2011),1,0)
mdrymwet_1112 = xr.where((mwet2011)&(mdry2012),1,0)
mdrymwet_1213 = xr.where((mwet2012)&(mdry2013),1,0)
mdrymwet_1314 = xr.where((mwet2013)&(mdry2014),1,0)
mdrymwet_1415 = xr.where((mwet2014)&(mdry2015),1,0)
mdrymwet_1516 = xr.where((mwet2015)&(mdry2016),1,0)
mdrymwet_1617 = xr.where((mwet2016)&(mdry2017),1,0)
mdrymwet_1718 = xr.where((mwet2017)&(mdry2018),1,0)
mdrymwet_1819 = xr.where((mwet2018)&(mdry2019),1,0)

#Build netcdf for MODIS category dry to wet change
mdrymwet = xr.Dataset({'D_0405': mdrymwet_0405,'D_0506': mdrymwet_0506, 'D_0607': mdrymwet_0607, 'D_0708': mdrymwet_0708, 'D_0809': mdrymwet_0809, 'D_0910': mdrymwet_0910, 'D_1011': mdrymwet_1011, 'D_1112': mdrymwet_1112, 'D_1213': mdrymwet_1213, 'D_1314': mdrymwet_1314, 'D_1415': mdrymwet_1415, 'D_1516': mdrymwet_1516, 'D_1617': mdrymwet_1617, 'D_1718': mdrymwet_1718, 'D_1819': mdrymwet_1819})
mdrymwet.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/mwet2mdry.nc')

#For FAO category: test whether there has been a yearly natural (undeveloped) to developed change to indicate human perturbation or degradation of natural habitat
devnat_0405 = xr.where((nat2004)&(dev2005),1,0)
devnat_0506 = xr.where((nat2005)&(dev2006),1,0)
devnat_0607 = xr.where((nat2006)&(dev2007),1,0)
devnat_0708 = xr.where((nat2007)&(dev2008),1,0)
devnat_0809 = xr.where((nat2008)&(dev2009),1,0)
devnat_0910 = xr.where((nat2009)&(dev2010),1,0)
devnat_1011 = xr.where((nat2010)&(dev2011),1,0)
devnat_1112 = xr.where((nat2011)&(dev2012),1,0)
devnat_1213 = xr.where((nat2012)&(dev2013),1,0)
devnat_1314 = xr.where((nat2013)&(dev2014),1,0)
devnat_1415 = xr.where((nat2014)&(dev2015),1,0)
devnat_1516 = xr.where((nat2015)&(dev2016),1,0)
devnat_1617 = xr.where((nat2016)&(dev2017),1,0)
devnat_1718 = xr.where((nat2017)&(dev2018),1,0)
devnat_1819 = xr.where((nat2018)&(dev2019),1,0)

#Build netcdf for FAO category characterising land degradation or change by humans
devnat = xr.Dataset({'N2D_0405': devnat_0405,'N2D_0506': devnat_0506, 'N2D_0607': devnat_0607, 'N2D_0708': devnat_0708, 'N2D_0809': devnat_0809, 'N2D_0910': devnat_0910, 'N2D_1011': devnat_1011, 'N2D_1112': devnat_1112, 'N2D_1213': devnat_1213, 'N2D_1314': devnat_1314, 'N2D_1415': devnat_1415, 'N2D_1516': devnat_1516, 'N2D_1617': devnat_1617, 'N2D_1718': devnat_1718, 'N2D_1819': devnat_1819})
devnat.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/devnat.nc')

#For MODIS category: test whether there has been a yearly natural (undeveloped) to developed change to indicate human perturbation or degradation of natural habitat
mdevmnat_0405 = xr.where((mnat2004)&(mdev2005),1,0)
mdevmnat_0506 = xr.where((mnat2005)&(mdev2006),1,0)
mdevmnat_0607 = xr.where((mnat2006)&(mdev2007),1,0)
mdevmnat_0708 = xr.where((mnat2007)&(mdev2008),1,0)
mdevmnat_0809 = xr.where((mnat2008)&(mdev2009),1,0)
mdevmnat_0910 = xr.where((mnat2009)&(mdev2010),1,0)
mdevmnat_1011 = xr.where((mnat2010)&(mdev2011),1,0)
mdevmnat_1112 = xr.where((mnat2011)&(mdev2012),1,0)
mdevmnat_1213 = xr.where((mnat2012)&(mdev2013),1,0)
mdevmnat_1314 = xr.where((mnat2013)&(mdev2014),1,0)
mdevmnat_1415 = xr.where((mnat2014)&(mdev2015),1,0)
mdevmnat_1516 = xr.where((mnat2015)&(mdev2016),1,0)
mdevmnat_1617 = xr.where((mnat2016)&(mdev2017),1,0)
mdevmnat_1718 = xr.where((mnat2017)&(mdev2018),1,0)
mdevmnat_1819 = xr.where((mnat2018)&(mdev2019),1,0)

#Build netcdf for MODIS category characterising land degradation or change by humans
mdevmnat = xr.Dataset({'N2D_0405': mdevmnat_0405,'N2D_0506': mdevmnat_0506, 'N2D_0607': mdevmnat_0607, 'N2D_0708': mdevmnat_0708, 'N2D_0809': mdevmnat_0809, 'N2D_0910': mdevmnat_0910, 'N2D_1011': mdevmnat_1011, 'N2D_1112': mdevmnat_1112, 'N2D_1213': mdevmnat_1213, 'N2D_1314': mdevmnat_1314, 'N2D_1415': mdevmnat_1415, 'N2D_1516': mdevmnat_1516, 'N2D_1617': mdevmnat_1617, 'N2D_1718': mdevmnat_1718, 'N2D_1819': mdevmnat_1819})
mdevmnat.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/mdevmnat.nc')

#For FAO category: test whether there has been a yearly change in any categories to characterise land use change of any kind
anych_0405 = xr.where((LV2004==LV2005),0,1)
anych_0506 = xr.where((LV2005==LV2006),0,1)
anych_0607 = xr.where((LV2006==LV2007),0,1)
anych_0708 = xr.where((LV2007==LV2008),0,1)
anych_0809 = xr.where((LV2008==LV2009),0,1)
anych_0910 = xr.where((LV2009==LV2010),0,1)
anych_1011 = xr.where((LV2010==LV2011),0,1)
anych_1112 = xr.where((LV2011==LV2012),0,1)
anych_1213 = xr.where((LV2012==LV2013),0,1)
anych_1314 = xr.where((LV2013==LV2014),0,1)
anych_1415 = xr.where((LV2014==LV2015),0,1)
anych_1516 = xr.where((LV2015==LV2016),0,1)
anych_1617 = xr.where((LV2016==LV2017),0,1)
anych_1718 = xr.where((LV2017==LV2018),0,1)
anych_1819 = xr.where((LV2018==LV2019),0,1)
anych_0419 = xr.where((LV2004==LV2019),0,1)

#Build netcdf for FAO category characterising any land use change
anych = xr.Dataset({'ANY_0419': anych_0419, 'ANY_0405': anych_0405,'ANY_0506': anych_0506, 'ANY_0607': anych_0607, 'ANY_0708': anych_0708, 'ANY_0809': anych_0809, 'ANY_0910': anych_0910, 'ANY_1011': anych_1011, 'ANY_1112': anych_1112, 'ANY_1213': anych_1213, 'ANY_1314': anych_1314, 'ANY_1415': anych_1415, 'ANY_1516': anych_1516, 'ANY_1617': anych_1617, 'ANY_1718': anych_1718, 'ANY_1819': anych_1819})
anych.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/anych.nc')

#For MODIS category: test whether there has been a yearly change in any categories to characterise land use change of any kind
manych_0405 = xr.where((MLV2004==MLV2005),0,1)
manych_0506 = xr.where((MLV2005==MLV2006),0,1)
manych_0607 = xr.where((MLV2006==MLV2007),0,1)
manych_0708 = xr.where((MLV2007==MLV2008),0,1)
manych_0809 = xr.where((MLV2008==MLV2009),0,1)
manych_0910 = xr.where((MLV2009==MLV2010),0,1)
manych_1011 = xr.where((MLV2010==MLV2011),0,1)
manych_1112 = xr.where((MLV2011==MLV2012),0,1)
manych_1213 = xr.where((MLV2012==MLV2013),0,1)
manych_1314 = xr.where((MLV2013==MLV2014),0,1)
manych_1415 = xr.where((MLV2014==MLV2015),0,1)
manych_1516 = xr.where((MLV2015==MLV2016),0,1)
manych_1617 = xr.where((MLV2016==MLV2017),0,1)
manych_1718 = xr.where((MLV2017==MLV2018),0,1)
manych_1819 = xr.where((MLV2018==MLV2019),0,1)
manych_0419 = xr.where((MLV2004==MLV2019),0,1)

#Build netcdf for MODIS category characterising any land use change
manych = xr.Dataset({'many_0419': manych_0419, 'many_0405': manych_0405,'many_0506': manych_0506, 'many_0607': manych_0607, 'many_0708': manych_0708, 'many_0809': manych_0809, 'many_0910': manych_0910, 'many_1011': manych_1011, 'many_1112': manych_1112, 'many_1213': manych_1213, 'many_1314': manych_1314, 'many_1415': manych_1415, 'many_1516': manych_1516, 'many_1617': manych_1617, 'many_1718': manych_1718, 'many_1819': manych_1819})
manych.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/luc/manych.nc')
