
'''

Intent

Command line script to convert .tif of sinusoidal projection to .tif of geographi projection (latlon WGS84)

Change file names and copy to command shell to action

Requires GDAL library, provide directory name in file specification

Accepts files in sinusoidal to change to common accepted netCDF format

'''

gdalwarp -of GTIFF -s_srs '+proj=sinu +R=6371007.181 +nadgrids@null +wktext' -r cubic -t_srs '+proj=longlat +datum=WGS84 +no_defs' landcover_MODIS2019.tif landcover_MODIS2019proj.tif

xds_reproj = xds.rio.reproject('epsg:4326') #reprojection if only reprojecting within crs but outwith EPSG projection


#https://gis.stackexchange.com/questions/194533/convert-modis-hdf-file-in-sinusoidal-projection-into-geotiff-with
