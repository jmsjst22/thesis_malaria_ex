from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score, mean_squared_error #c stat
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import pandas as pd

'''

Script for testing error for best parameters- optimised using GridSearchCV

'''


# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 3000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 200, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 4,6,8, 10,12,14,16,18,20]
# Method of selecting samples for training each tree
bootstrap = [True, False]
#choose criterion
criterion= ['mse','mae']
# Create the random grid
param_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth':max_depth,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap,
               }

# define file path
filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')
# Get data
data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')
# Define Columns
Xcol = data.columns[5:]
print(Xcol)
# Get column data for features
X = data[Xcol]
# Get column data for labels
Y = data['me_rt_hh_district_prop']
# Split into populations for testing and training for model performance assessment
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)
# Call regressor
rf = RandomForestRegressor()
# Call gridsearch for hyper-parameter optimisation using random forest as a searching method
grid_search = GridSearchCV(estimator = rf,param_grid=param_grid,cv=5,n_jobs= -1,verbose=2)

# Fit model (train)
grid_search.fit(X_train,Y_train)

# Get Best H-Parameters
grid_search.best_params_
# Get best score from hyper-parameters (f1 score for all hyper-parameter sets
bestscore=grid_search.best_score_
print(bestscore)

# Find and print best grid to ascertain best hyper-parameters 
best_grid = grid_search.best_estimator_

print(best_grid)
print('for all')

# Get MSE
mse = mean_squared_error(Y_test,Y_predict)
# Get RMSE
rmse = np.sqrt(mse)
print(rmse)
