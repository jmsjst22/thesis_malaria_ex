# Environmental Malaria Risk: Thesis Repository, James Tomlinson

This repository is compiled to provide a basis to characterise theoretical malaria risk through environmental impactors, and recreate the findings of Tomlinson (2021). <b>

It is procedural code that can be used to download, create, treat, decompose and analyse netCDF4 data. Post-analysis deals with csv datasets of summarised theoretical malaria risk. <b>

## Logic <b>
  
  ![Logic Diagram](/diagrams/diagram_for_readme.png)

The library will make use of the following modules and packages with no known deprecation issues as of 30/07/2021.
 

|  PACKAGE/MODULE |  VERSION  | Notes|
|------------|-----------|---------------------------------------------|
| pandas     | 1.3.0rc1  |    Dataframe operations/csv manipulation                                         |
| xarray     | 0.18.2    |     Netcdf manipulation/creation                                      |
| ncview     | 2.1.8     | NetCDF viewer, GUI Launched at bash shell (not python)|
| argparse   | 1.1       |  Create command line arguments to alter operation of script                                           |
| zipfile    | correct at python v3.8| Zip/unzip files to location|
| os         | correct at python v3.8| Interface with Operating System |
| glob       | correct at python v3.8| Make list of file names in directory|
| numpy      | 1.21.0    | Numerical operations |
| Climate Data Operators |1.9.9rc1| Executed at bash shell|
| netCDF4    | 1.5.3| Some netCDF operations (likely executable with xarray) |
| rioxarray  | 0.4.3 | Used for shapefile/district summarisation and application of coordinate reference system |
| subprocess | correct at python v3.8| Call bash shell subprocesses from python script|
| GDAL  | 3.2.0 | Script used in study is called from bash shell| 
| seaborn | 0.11.1 | Visualisation implicit in most non-netcdf visualisation |
| sklearn | 0.22.2.post1 | (.ensemble : RandomForestRegressor;<b> .metrics : roc_auc_score,mean_squared_error; <b> .model_selection: train_test_split, GridSearchCV; <b> .inspection: permutation_importance;).|
| shap | 0.39 | Requires seaborn, sklearn: For Shapley value analysis and visualisation |
| pandas.plotting | 1.3.0rc1 | register_matplotlib_converters (for Shapley plotting)| 
| feature-selector | 1.0.0 | Contributes to collinearity and importance reduction |
  

# Data Download

  The following scripts should be executed at the command line or in their respective browser consoles to download data locally or to your cloud (gmail for Google Earth Engine):
  
  | SCRIPT | PLATFORM | DATA DOWNLOAD | Preview |
  |--------|----------|---------------|---------|
  | Forest_change_yearly_gee.txt | Google Earth Engine | Forest Change and Degradation (Hansen et al 2013).|   ![Forest Loss (/diagrams/Capture.png)
  | MODISdownload_gee.txt | Google Earth Engine | MODIS land cover class |
  |
  
 
