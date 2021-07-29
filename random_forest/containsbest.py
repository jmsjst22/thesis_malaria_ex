#build the model

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
from sklearn.model_selection import RandomizedSearchCV
from sklearn.inspection import permutation_importance
import shap

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 1, stop = 1500, num = 10)]
# Number of features to consider at every split
max_features = [int(x) for x in np.linspace(start = 1, stop = 200, num = 5)]
# Minimum number of samples required at each leaf node
min_samples_leaf = [int(x) for x in np.linspace(start = 1, stop = 200, num = 10)]
max_depth = [int(x) for x in np.linspace(start = 1, stop = 40, num = 5)]
bootstrap = [True,False]
# Create the random grid
param_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth':max_depth,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

def evaluate(best_grid, X_test, Y_test):
    predictions = best_grid.predict(X_test)
    errors = abs(predictions - Y_test)
    mape = 100 * np.mean(errors / Y_test)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))

    return accuracy



filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')

data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')
Xcol1 = data.columns[data.columns.str.contains('temp')]
Xcol1 = data[Xcol1]
Xcol2 = Xcol1.columns[Xcol1.columns.str.contains('2mb')]
Xcol = data.columns[5:]
X = data[Xcol2]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

rf = RandomForestRegressor()

grid_search = GridSearchCV(estimator = rf,param_grid=param_grid,cv=5,n_jobs= -1,verbose=2)


grid_search.fit(X_train,Y_train)


grid_search.best_params_
bestscore=grid_search.best_score_
print(bestscore)

best_grid = grid_search.best_estimator_
Y_predict = best_grid.predict(X_test)
print(best_grid)
print('for year')

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
