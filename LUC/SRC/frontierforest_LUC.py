import xarray as xr
import numpy as np

'''
Intent
Binary count of forest loss per year as measured by Hansen et al 2013, version up to and including 2020.

Requirements
File in netcdf format. Reindexing to a unified grid is not required or beneficial before analysis.

Information on data bands is held at data source:

https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2020_v1_8

and in product research paper at Hansen et al, 2013.


'''

#open netCDF
forestloss = xr.open_dataset('/home/s1987119/Diss_data/Final/Land Use Change/Process/yearlyfrontier.nc')

#Extract multi-dimensional data array from dataset variable
lossyear=forestloss['Band1']

#test with xarray where for presence of pixels lost in each year, classify binary and build data array for each year
loss2020= xr.where((lossyear==20),1,0)
loss2019= xr.where((lossyear==19),1,0)
loss2018= xr.where((lossyear==18),1,0)
loss2017= xr.where((lossyear==17),1,0)
loss2016= xr.where((lossyear==16),1,0)
loss2015= xr.where((lossyear==15),1,0)
loss2014= xr.where((lossyear==14),1,0)
loss2013= xr.where((lossyear==13),1,0)
loss2012= xr.where((lossyear==12),1,0)
loss2011= xr.where((lossyear==11),1,0)
loss2010= xr.where((lossyear==10),1,0)
loss2009= xr.where((lossyear==9),1,0)
loss2008= xr.where((lossyear==8),1,0)
loss2007= xr.where((lossyear==7),1,0)
loss2006= xr.where((lossyear==6),1,0)
loss2005= xr.where((lossyear==5),1,0)
loss2004= xr.where((lossyear==4),1,0)

#Build netcdf full of data array composites to netCDF variables
lossyear = xr.Dataset({'loss_2020':loss2020,'loss_2019':loss2019,'loss_2018':loss2018,'loss_2017':loss2017,'loss_2016':loss2016,'loss_2015':loss2015,'loss_2014':loss2014,'loss_2013':loss2013,'loss_2012':loss2012,'loss_2011':loss2011,'loss_2010':loss2010,'loss_2009':loss2009,'loss_2008':loss2008,'loss_2007':loss2007,'loss_2006':loss2006,'loss_2005':loss2005,'loss_2004':loss2004})
lossyear.to_netcdf('/home/s1987119/Diss_data/Final/Final_Products/forestloss.nc')
