# gridsearch adaptation

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score, mean_squared_error #c stat
import math
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.inspection import permutation_importance
import shap


filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')

data = pd.read_csv(filepath+'FINAL_p_imp.csv')

Xcol = data.columns[5:]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 3000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 200, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 4,6,8, 10,12,14,16,18,20]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4,8,10,12,13]
# Method of selecting samples for training each tree
bootstrap = [True, False]
#choose criterion
criterion= ['mse','mae']
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,'criterion':criterion,
               'bootstrap': bootstrap}

rf = RandomForestRegressor()

rf_random = RandomizedSearchCV(estimator=rf, param_distributions = random_grid, n_iter=1000,cv=10,random_state=42,n_jobs=-1)

rf_random.fit(X_train, Y_train)

Y_predict = rf_fit.predict(X_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))
print(nrmse)

bestset =rf_random.best_params_

print('best params for combined is',bestset)
print(nrmse)
Xcol = data.columns[5:11]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 3000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 200, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 4,6,8, 10,12,14,16,18,20]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4,8,10,12,13]
# Method of selecting samples for training each tree
bootstrap = [True, False]
#choose criterion
criterion= ['mse','mae']
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,'criterion':criterion,
               'bootstrap': bootstrap}

rf = RandomForestRegressor()

rf_random = RandomizedSearchCV(estimator=rf, param_distributions = random_grid, n_iter=1000,cv=10,random_state=42,n_jobs=-1)

rf_random.fit(X_train, Y_train)

Y_predict = rf_fit.predict(X_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))
print(nrmse)

bestset =rf_random.best_params_
print(nrmse)
print('best params for social is',bestset)

Xcol = data.columns[85:]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 3000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 200, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 4,6,8, 10,12,14,16,18,20]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4,8,10,12,13]
# Method of selecting samples for training each tree
bootstrap = [True, False]
#choose criterion
criterion= ['mse','mae']
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,'criterion':criterion,
               'bootstrap': bootstrap}

rf = RandomForestRegressor()

rf_random = RandomizedSearchCV(estimator=rf, param_distributions = random_grid, n_iter=1000,cv=10,random_state=42,n_jobs=-1)

rf_random.fit(X_train, Y_train)

Y_predict = rf_fit.predict(X_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))


bestset =rf_random.best_params_
print(nrmse)
print('best params for envy is',bestset)

Xcol = data.columns[11:84]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 3000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 200, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 4,6,8, 10,12,14,16,18,20]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4,8,10,12,13]
# Method of selecting samples for training each tree
bootstrap = [True, False]
#choose criterion
criterion= ['mse','mae']
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,'criterion':criterion,
               'bootstrap': bootstrap}

rf = RandomForestRegressor()

rf_random = RandomizedSearchCV(estimator=rf, param_distributions = random_grid, n_iter=1000,cv=10,random_state=42,n_jobs=-1)

rf_fit= rf_random.fit(X_train, Y_train)

Y_predict = rf_fit.predict(X_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))


bestset =rf_random.best_params_
print(nrmse)
print('best params for envmonth is',bestset)
