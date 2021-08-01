# Thesis Repository, James Tomlinson: Environmental Malaria Risk.

This repository is compiled to provide a basis to characterise theoretical malaria risk through environmental impactors, and recreate the findings of Tomlinson (2021). <b>

It is procedural code that can be used to download, create, treat, decompose and analyse netCDF4 data. Post-analysis deals with csv datasets of summarised theoretical malaria risk. <b>

## Logic <b>
  
  ![Logic Diagram](/diagrams/diagram_for_readme.png)

The library will make use of the following modules and packages with no known deprecation issues as of 30/07/2021.
 

|  PACKAGE/MODULE |  VERSION  | Notes|
|------------|-----------|---------------------------------------------|
| ``` pandas ```   | ``` 1.3.0rc1 ``` |    Dataframe operations/csv manipulation                                         |
| ``` xarray ```    | ``` 0.18.2 ```    |     Netcdf manipulation/creation                                      |
|  ``` ncview  ```   | ``` 2.1.8   ```  | NetCDF viewer, GUI Launched at bash shell (not python)|
| ``` argparse ```  | ``` 1.1 ```      |  Create command line arguments to alter operation of script                                           |
| ``` zipfile ```   | correct at python ``` v3.8 ```| Zip/unzip files to location|
| ``` os  ```       | correct at python ``` v3.8 ```| Interface with Operating System |
| ``` glob ```       | correct at python ``` v3.8 ```| Make list of file names in directory|
| ``` numpy ```     |  ``` 1.21.0 ```   | Numerical operations |
|  ``` Climate Data Operators ``` | ``` 1.9.9rc1 ```| Executed at bash shell|
| ``` netCDF4 ```   | ``` 1.5.3 ```| Some netCDF operations (likely executable with xarray) |
| ``` rioxarray ``` | ``` 0.4.3 ``` | Used for shapefile/district summarisation and application of coordinate reference system |
| ``` subprocess ``` | correct at python ``` v3.8 ```| Call bash shell subprocesses from python script|
| ``` GDAL ```  |``` 3.2.0 ```| Script used in study is called from bash shell| 
| ``` seaborn ``` | ``` 0.11.1 ``` | Visualisation implicit in most non-netcdf visualisation |
| ``` sklearn ``` | ``` 0.22.2.post1 ``` | (``` .ensemble ```: ``` RandomForestRegressor ```;<b> ``` .metrics ``` :  ``` mean_squared_error ```; <b> ``` .model_selection ```: ``` train_test_split ```, ```GridSearchCV ```; <b> ``` .inspection ```: ```permutation_importance ```;).|
| ``` shap ```| ``` 0.39 ``` | ``` Requires seaborn ```, ``` sklearn ```: For Shapley value analysis and visualisation |
| ``` pandas.plotting ``` | ``` 1.3.0rc1 ``` | register_matplotlib_converters (for Shapley plotting)| 
|  ``` feature-selector ``` | ``` 1.0.0 ``` | Contributes to collinearity and importance reduction |
  

# Data Download

  The following scripts should be executed at the command line or in their respective browser consoles to download data locally or to your cloud (GDrive for Google Earth Engine):
  
  # Land Use Change
  
  | SCRIPT | PLATFORM | DATA DOWNLOAD | Preview |
  |--------|----------|---------------|---------|
  | ``` Forest_change_yearly_gee.txt ``` Single Years | Google Earth Engine | Forest Change and Degradation (Hansen et al 2013).|   ![Forest Loss](/diagrams/Capture.GIF) |
  | ``` MODISdownload_gee.txt ``` Single Years| Google Earth Engine | MODIS land cover class |  ![MODIS Land Cover Classes](/diagrams/modis.GIF) |
  | ``` landcover_download.py ``` Single Years | CDS toolbox/API on command line | ICDR land cover class |  ![ICDR Land Cover Classes](/diagrams/icdr.GIF) |
  
  Scripts are/can be adapted for period of study. The scripts operate by serving multiple single year files.
  
  # Climate
  
  | Variable | SCRIPT | PLATFORM | DATA DOWNLOAD | Preview |
  |----------|--------|----------|---------------|---------|
  | Humidity | ``` downloadhumidity.py ``` | CDS toolbox/API on command line | Agrometeorological indicators from 1979 <b> to present derived from reanalysis (2m relative humidity) |  ![Relative Humidity at 2 metres](/diagrams/humidity.gif) |
  | Temperature |``` temp_cdi.py ``` | CDS toolbox/API on command line | ERA5-Land hourly data from 1981 to present <b> (2m temperature (K)) |  ![Temperature at 2 metres](/diagrams/temperature.gif)
  | Precipitation | Adapted ``` temp_cdi.py ``` | CDS toolbox/API on command line | ERA5-Land hourly data from 1981 to present <b> (Total Precipitation (metres)) |  ![Total Precipitation](/diagrams/precipitation.gif)
 
## Notes on data download
>Precipitation data can be downloaded with adaptation of the Temperature API code. The hourly temporal resolution and data source are the same so variable only will need to be changed. Precipitation and temperature are downloaded in two smaller portions for storage control - 5 years each are recommended. This can be merged for the study period (demonstrated in the next section).
  
>Humidity data is served in period streams - therefore upon download a dataset will represent the entire study period but only one timestamp daily (e.g. 900,1500,1800). A demonstration on its merging is in the next section. 

>Finally, it is recommended that each data stream is taken to analysis individually. The data downloads are storage consumptive (with land use change and humidity requiring more than 2GB for full variable sets). The processes from this point are all reductive as they are clipping and merging larger datasets. It is recommended that the raw data be removed from local directories at each stage. This is automated for Relative Humidity but is kept as an option for other variable sets.
  
# Data Treatment and Pre-processing
  
  The following scripts merge and initiate pre-processing of all files in preparation for their analysis.

  | Variable | Script Flow | Primary/Final Output |
  |----------|-------------|----------------------|
  |Temperature & Precipitation| ``` Temp_Prec_merge.py ``` default merge of downloaded temperature files. <b> Optional argument ``` --prec True ``` at command line will merge precipitation files. | Optionally merged Temperature or Precipitation for entire initial period.
  | Humidity | Unzip and clip iteratively with ``` rename_retime.py ```--> Create grid for unifying humidity netcdf format with ``` regridhum.py ``` --> <b> Reindex all netcdf to create grid with ``` reind_like.py ```  --> <b> Delete ``` regrid.nc ``` from directory to exclude from merge --> <b> Merge across all hour period sets at command shell with ``` cdo merge ``` (``` merge.txt ```). | Merged single file for whole period, appropriately timed and formatted. |
  
## Land use data suites
  
  | Datasets | Script Flow | Primary/Final Output |
  |----------|-------------|----------------------|
  | Forest Loss | Convert to netCDF with ``` tiftonetcdf.txt ``` copied to command shell | .netCDF for all single years from .tif with binary pixel notification for forest loss |
  | MODIS Land Cover Class | Arrives in MODIS Sinusoidal projection, regrid at command line with ``` warp.txt ``` --> Convert to netCDF with ``` tiftonetcdf.txt ``` copied in command shell | .netCDF for all single years with land use classes |
  | ICDR Land Cover Class | Optionally Clip (storage saving) with adapted ``` netxclip.py ``` method --> Regrid to common grid frame with ``` reindex_LUC.py ``` | .netCDF for all single years with land use classes
  
 # Validation
  
  All validation was facilitated with minimum working examples (for method step validation) and ncview (for product step validation).
  
  There are no code templates for this as the method of validation is likely to change upon generalisation and many of the operations were single line or visual checks.
  
  Minimum working examples were used for humidity, precipitation and temperature, whereby 0.1 degree (latitude and longitude) subsections were taken from within Uganda borders. This was typically taken at random (np.random between a range for latitude and longitude), where the location was checked for correct merging and minimal impacts of the regridding. Regridding was assessed in order to view the impact in offset of unifying the spatial grids. This assessment was finalised in QGIS with single time slices, whereby spatial statistics (of Uganda's districts shapefile) and the RMSE and total differences between untreated netCDF values and regridded, post-merging netCDF values were assessed in a time slice (hour) for each year of the study period. 
  
  For example, 0900 1/04/2018 for humidity, temperature and precipitation at a 300km^2 area were tested for their spatial statistics. RMSE of <0.05 were observed for all time slices under this method and were accepted.

  Land Use Change was tested for spatial artefacts of error only, in ``` ncview ```. Any digitization artefacts within the bounds of Uganda were investigated - if not error in method could be found the data would be thrown out, and the process started again in order to assess differences in pre-analysis products. Continuation of error artefacts would see the data thrown out of all experiments.  

 ![Land Use Change Error Artefacts](/diagrams/luc_vald.GIF)                                                                                                                                               
                                                                                                                                                   
                                                                                                                                                 
                                                                                                                                                    
  
 
