import netCDF4 as nc
import numpy as np

'''

Produce a generic template netCDF for regridding humidity data at the resolution and extent
close to original humidity file

'''

#Define output filename
fn = 'regrid.nc'

#With write authorisation and type netCDF4
ds = nc.Dataset(fn, 'w', format='NETCDF4')

#With dimensions of generic longitude and latitude of flexible shape

lon=ds.createDimension('lon', 62)
lat= ds.createDimension('lat', 63)

#With variables populated by dimensions of flexible data type "float"
lons = ds.createVariable('lon','f4',('lon',))
lats = ds.createVariable('lat','f4',('lat',))

#With relative humidity template variable populated with spatial dimension attributes and percentage units
relative_humidity = ds.createVariable('relative_humidity', 'f4', ('lon','lat',))
relative_humidity.units = '%'

#Populate empty spatial variables with array of specified length and step
lons[:] = np.arange(29.1,35.3,0.1)
lats[:] = np.arange(4.3, -2.0, -0.1)

#Populate value variable with random values to make regridding to possible
relative_humidity[:,:] = np.random.uniform(0,100,size=(62,63))

#Close dataset
ds.close()
