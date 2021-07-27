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
n_estimators = [20]
# Number of features to consider at every split
max_features = [18]
# Minimum number of samples required at each leaf node
min_samples_leaf = [27]
max_depth = [48]
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

Xcol = data.columns[5:]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

rf = RandomForestRegressor()

grid_search = GridSearchCV(estimator = rf,param_grid=param_grid,cv=5,n_jobs= -1,verbose=2)


grid_search.fit(X_train,Y_train)

grid_search.best_params_
bestscore=grid_search.best_score_
print(bestscore)

best_grid = grid_search.best_estimator_

print(best_grid)
print('for all')




mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)



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

#explainer  = shap.TreeExplainer(best_grid)
#shap_values = explainer.shap_values(X_test)

#vals= np.abs(shap_values).mean(0)
#feature_importance = pd.DataFrame(list(zip(X_train.columns,vals)),columns=['col_name','feature_importance_vals'])
#feature_importance.sort_values(by=['feature_importance_vals'],ascending=False,inplace=True)
#feature_importance.head()
#feature_importance.to_csv(filepath+'shaply_tuned_social.csv')

#print(feature_importance)


#shap.summary_plot(shap_values,X_test, plot_type='bar')
#shap.summary_plot(shap_values,X_test, max_display = 30,  title='Shapley Values for Month Scale Environmental Factors', color_bar_label= 'Comparative Feature/Factor Value')
