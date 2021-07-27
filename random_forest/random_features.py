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
import shap

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 800, stop = 1100, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2,3, 4,8]
# Create the random grid
param_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

def evaluate(model, X_test, Y_test):
    predictions = model.predict(X_test)
    errors = abs(predictions - Y_test)
    mape = 100 * np.mean(errors / Y_test)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))

    return accuracy



filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')
plt.rc('font',size=8)
data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')

Xcol = data.columns[5:16]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

rf = RandomForestRegressor()
# random params n_estimators= 900,min_samples_split= 18,min_samples_leaf= 1,max_features= 'auto',bootstrap= True
#grid_search = GridSearchCV(estimator = rf_random,param_grid=grid,cv=20,n_jobs=-1)

#rf_random = (estimator=rf, param_distributions=random_grid,n_iter=500,cv=10,verbose=2,random_state=42,n_jobs=-1)



grid_search = GridSearchCV(estimator = rf, param_grid = param_grid,
                          cv = 40, n_jobs = -1, verbose = 2)


grid_search=grid_search.fit(X_train,Y_train)

best_params = grid_search.best_params_

best_grid = grid_search.best_estimator_
grid_accuracy = evaluate(best_grid,X_test,Y_test)
#Y_predict = rf_fit.predict(X_test)
#base_accuracy = evaluate(rf_fit,X_test,Y_test)

#best_random = rf_fit.best_estimator_
#random_accuracy = evaluate(rf_fit,X_test,Y_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))
print(nrmse)

print(best_params)
#rf_fit.best_params_
#grid.best_score_


#feature_importances = pd.DataFrame(rf_random.feature_importances_,
#                                    index  =X_train.columns,columns=['importance']).sort_values('importance',ascending=False)

#print(feature_importances)
#feature_importances.to_csv(filepath+'feature_importance_envmonth.csv')



#perm_importance  = permutation_importance(rf_fit,X_test,Y_test)
#sorted_idx = perm_importance.importances_mean.argsort()

#plt.barh(X_train.columns[sorted_idx], perm_importance.importances_mean[sorted_idx])
#plt.show()

#bestfit=grid.best_params_
#bestfitscore = grid.best_score_
#print(bestfit)
#print(bestfitscore)

#explainer  = shap.TreeExplainer(rf_fit)
#shap_values = explainer.shap_values(X_test)

#vals= np.abs(shap_values).mean(0)
#feature_importance = pd.DataFrame(list(zip(X_train.columns,vals)),columns=['col_name','feature_importance_vals'])
#feature_importance.sort_values(by=['feature_importance_vals'],ascending=False,inplace=True)
#feature_importance.head()
#feature_importance.to_csv(filepath+'shapley_importance_top10.csv')

#print(feature_importance)


#shap.summary_plot(shap_values,X_test, plot_type='bar')
#shap.summary_plot(shap_values,X_test, max_display = 30,  title='Shapley Values for Month Scale Environmental Factors', color_bar_label= 'Comparative Feature/Factor Value')
