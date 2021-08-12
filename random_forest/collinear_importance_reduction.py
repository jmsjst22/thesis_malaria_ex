# Experimental Collinear and unimportant feature removal not used in final product

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
from feature_selector import FeatureSelector


filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')
plt.rc('font',size=8)
data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')
Xcol = data.columns[5:]
X = data[Xcol]
Y = data['me_rt_hh_district_prop']


# Call feature selector
fs = FeatureSelector(data = X, labels = Y)

# Identify collinear features with threshold of above 0.6 correlation coefficient.
fs.identify_collinear(correlation_threshold=0.6)

correlated_features = fs.ops['collinear']
# Identify unimportant features
fs.identify_zero_importance(task= 'regression',eval_metric = 'l2',n_iterations=10,early_stopping=True)
# Identify Features that do not contribute to 0.95 of the importance 
fs.identify_low_importance(cumulative_importance = 0.95)
# Action low importance method
low_importance_features = fs.ops['low_importance']
# Remove low importance and collinear features
X_nc_nli = fs.remove(methods = 'all')


# Train/Test/Split with 
X_train,X_test,Y_train,Y_test = train_test_split(X_nc_nli,Y,test_size=0.25,random_state=42)


rf = RandomForestRegressor(random_state=42)

# Train model
rf_fit = rf.fit(X_train,Y_train)

# Predict with test data
Y_predict = rf_fit.predict(X_test)

# Test with error, RMSE
mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)

# Call visualiser/assessor of importance with Shapley value
explainer  = shap.TreeExplainer(rf_fit)
shap_values = explainer.shap_values(X_test)

vals= np.abs(shap_values).mean(0)
feature_importance = pd.DataFrame(list(zip(X_train.columns,vals)),columns=['col_name','feature_importance_vals'])
feature_importance.sort_values(by=['feature_importance_vals'],ascending=False,inplace=True)
feature_importance.head()
#feature_importance.to_csv(filepath+'vis_importance_all.csv')

#print(feature_importance)

perm_importance  = permutation_importance(rf_fit,X_test,Y_test)

sorted_idx = perm_importance.importances_mean.argsort()

print(sorted_idx)

plt.barh(X_train.columns[sorted_idx], perm_importance.importances_mean[sorted_idx])
plt.show()

shap.summary_plot(shap_values,X_test, plot_type='bar')
shap.summary_plot(shap_values,X_test, max_display = 30,  title='Shapley Values for Month Scale Environmental Factors', color_bar_label= 'Comparative Feature/Factor Value')
