# Thesis Repository, Facilitative of Supporting Documentation Tomlinson (2021): Environmental Malaria Risk

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
| ``` shap ```| ``` 0.39 ``` | Requires ``` seaborn ```, ``` sklearn ```: For Shapley value analysis and visualisation |
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

  Land use change was tested for spatial artefacts of error only, in ``` ncview ```. Any digitization artefacts within the bounds of Uganda were investigated - if not error in method could be found the data would be thrown out, and the process started again in order to assess differences in pre-analysis products. Continuation of error artefacts would see the data thrown out of all experiments.  
                                                                                                                                                    
Artefacts of error (straight continuous lines, blocks, or continuously/unrealistically changing areas).
 ![Land Use change Error Artefacts](/diagrams/luc_vald.GIF)        
                                                                                                                                                    
 Much of the above validation campaign is the method repeated for post-analysis validation.                                                                                                                                                   
 # Analysis
                                                                                                                                                    
 The analysis stage finds the highest divergence in treatment and scripts used for each variable:
                                                                                                                                                    
 ## Temperature

| Variable | Script | Requirements |
|----------|--------|--------------|                                                                                                                        
| Diurnal Temperature Range | diurnal_summary_temp.py | Merged temperature netCDF at appropriate directory location, packages as above |
| Risk attributable to mosquito transmission component related to temperature | PPM_temp_model.py | As above |

## Precipitation

| Variable | Script | Requirements |
|----------|--------|--------------|
| Number of days at precipitation bands, temporal statistics for year and months | precipitation.py | Merged precipitation netCDF at appropriate directory location, packages as above |

## Humidity 

| Variable | Script | Requirements |
|----------|--------|--------------|
| Number of days at high/low humidity, temporal statistics for year and months | humidity.py | All pre-treatment measures have to be completed in order, to get a merged humidity netCDF at appropriate location, packages as above |

## Land use change

| Variable | Script | Requirements |
|----------|--------|--------------|
| LUC for MODIS and ICDR suites: Land use change as defined by natural to developed, wet to dry, dry to wet, any change at all, any change appearing as degradation (for example from forest to grassland) | LUCall.py | MODIS and ICDR data suites for all years in single directory for all years, regridded where necessary, packages as above |
| Forest loss (multiple years) | frontierforest_LUC.py | Single regridded/ converted to netCDF with dataset variables representing single years, packages as above |

Following analysis, it is recommended that all final products are stored in a folder relative to the post-analysis script requirements.

# Validation 

All steps from the previous validation stage should be repeated here. Additional validation includes sense checking for unusual artefacts (straight lines) in all dataset variables. If there appears to be repeated land use change of the same kind happening at a single location this portion may have to be removed at final stages (removal of districts effected from modelling). 

### Sample of digitization/analysis artefact
(See top right and bottom right areas that do not change, with bottom showing artefacts of regridding outside of the Uganda area).

 ![land use is sometimes wrong](/diagrams/luc_art.gif)

Following removal  of error artefacts and sense checking of humidity, temperature and precipitation summarisations (there was no exceedence of expected or maximum values for risk or climate variable data), the datasets are ready for geographical summary, leading to final stages of modelling with RF regressor.

# Geographic Summarisation 

At this stage, the data is prepared to be summarised by geographies. This geography must be in shapefile format with a designated filepath. The code for each sumamrisation is seperated by month and year as these will require different treatements and checks at later stages. The scripts are also written as such where, especially in the case of land use change, if there are any 'empty' districts post-summarisation, these will be accepted and registered as 0.

| Time-scale | Script | Output |
|------------|--------|--------|
| Month      | m_districts.py | Format .csv: Geographically summarised environmental conditions and  aggregated risk and summary statistics for monthly precipitation, temperature and humidity only |
| Year       | y_districts.py | Format .csv: Geographically summarised environmental conditions and aggregated risk and summary statistics for yearly precipitation, temperature and humidity. Land use change is at yearly frequency and will be summed per district rather than spatially averaged. |

# Association with malaria indicating survey timescale                                                                                                                                                     
From this, computation will be manual to get 1,2,3 months and year of and year before summary statistics for each district record pertaining to DHS/MIS malaria indicators. Future development/recommendations for streamlining will make this automatic with date/time objects as part of the variable titles,
associating these variables with their appropriate survey date.

The final product for modelling will require pandas merging of month and year data and pandas vertical concatenation of all year/district combinations. 

This will give one dataset with all variable columns at each timescale (subsequently, ``` features ```) with a year/district multi-index ( subsequently ``` rows ``` or ``` samples ``` ), with each row having a ``` label ```, or malaria indicating proportion value, as specified in the supporting technical document.   

# Random Forest 

Each of the following scripts can be adapted to 'slice' the data by desired features to assess their label response:

| Script | Function |
|--------|----------|                                                                                                                                
|  ``` base_model.py``` | Serves an output of performance of a non-tuned model, as measured by RMSE. Adapting script can serve and measure performance of different feature sets, for optimisation and experimentation.|
| ```best_params.py``` | Serves an output of performance for a model tuned by GridSearchCV in its hyper-parameters. It is recommended that hyper-parameters are tried in a wide and varying combination. Combination sets will be explained in the technical document as they are related to model performance directly. |
| ```collinear_importance_reduction.py``` | This script leverages ```feature-selector``` package to experiment with removing collinear variables at non-systematically. Less impactful features are also removed with ``` feature-selector ``` in-built method using a gradient boosting machine. Warning: this method is non-deterministic (please action multiple times to capture variation) and is consumptive of time- so please make a cup of tea or go for a wander when you run this script. The main output is, as above, a new measure of model error.
| ```containsbest.py``` | This script leverages hyper-parameter tuning as above, but is adapted (and adaptable) to only query certain feature sets. For example, if I am only interested in temperature related risk trends 3 months before the survey date, I can adapt the code to query only this set against the malaria indicating labels. This script can be used for ultra-specific testing of new variable combinations while "holding back" unwanted features.
| ``` randomsearch.py ``` | Uses RandomSearchCV instead of GridSearchCV to find the best hyper-parameters. Tests all feature sets from Tomlinson (2021). Effective when considering a starting point for hyper-parameterisation (e.g. identifying a good starting range). Warning: not as accurate as GridSearchCV; could be more compact - consider looping for slices in future versions or if user would like to adapt. |
| ``` hindcast.py ``` |  This script is adaptable to 'hold back' a certain year from test and train sets. The intent is to hindcast and test for overfitting- which are theoretical and practical tests of model generalisabilty, respectively. Standard deviation and RMSE of the models are the output to test if the model captures the geographical and temporal variation with little overall error. |                                                                           
        

## Main Feature Importance Outputs
                                                          
Each of primary basic models with hyper-parameterisation calculate and utilise Shapley values and SHAP visualisations, respectively. These are a tool for investigating feature importance interpreted in full in research documentation (Tomlinson 2021). Visualisations will be served that include: permutation importance outputs, feature_importance, aggregated importance of features before an aggregation threshold (most important features), Shapley means and Shapley individual distributions; all shown in Research Paper (Tomlinson 2021).

# Future Developments

It is accepted by the author that there is a lot of boiler plate code that is beyond theoretical flexibility, and is impractical to maintain. Comments will be made in individual scripts about where this will be developed in the future for the project timescale. Some of the boiler plate is lack of resources and know-how to get the file IO and variables into an appropriate flow of loops and lists, which would be the main facilitator of script shortening. There will also be an attempt to add everything to at least procedural method form and perhaps even object-based form as the author recognises the benefit of organising and actioning from single scripts.

Recommendations to the author for adaptation and improvement are welcome. Please cite this repository if any methods from it are used.



                                                                                                                                                  
                                                                                                                                                   
                                                                                                                                                  
                                                                                                                                                    


                                                                                                                                                
                                                                                                                                                   


                                                                                                                                                    
                                                                                                                                                   
                                                                                                                                                    
                                                                                                                                                  
                                                                                                                                                    
  
 
