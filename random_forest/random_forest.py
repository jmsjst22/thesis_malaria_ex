#build the model

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

#n_estimators = [100,400,800,900,1000,1200,1400]

#max_features =['auto','sqrt','log2']

#bootstrap = [True,False]

#grid = {'n_estimators':n_estimators,'max_features':max_features,'bootstrap':bootstrap}



filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')

data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')

Xcol = data.columns[16:119]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25)

rf_random = RandomForestRegressor()

#grid_search = GridSearchCV(estimator = rf_random,param_grid=grid,cv=20,n_jobs=-1)

rf_fit=rf_random.fit(X_train,Y_train)
Y_predict = rf_fit.predict(X_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))
print(nrmse)

feature_importances = pd.DataFrame(rf_random.feature_importances_,
                                    index  =X_train.columns,columns=['importance']).sort_values('importance',ascending=False)

print(feature_importances)
feature_importances.to_csv(filepath+'feature_importance_envmonth.csv')


perm_importance  = permutation_importance(rf_fit,X_test,Y_test)

sorted_idx = perm_importance.importances_mean.argsort()

plt.barh(X_train.columns[sorted_idx], perm_importance.importances_mean[sorted_idx])
plt.show()
#bestfit=grid.best_params_
#bestfitscore = grid.best_score_
#print(bestfit)
#print(bestfitscore)
