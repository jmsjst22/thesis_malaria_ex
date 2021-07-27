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
#Xcol1 = data.columns[data.columns.str.contains('hum')]
#Xcol1 = data[Xcol1]
#Xcol2 = Xcol1.columns[Xcol1.columns.str.contains('1mb')]
Xcol = data.columns[5:]
X = data[Xcol]
Y = data['me_rt_hh_district_prop']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

RandomForestRegressor(random_state = 42)


rf_fit = rf.fit(X_train,Y_train)

Y_predict = rf_fit.predict(X_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)

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
shap.summary_plot(shap_values,X_test, max_display = 10,  title='Shapley Values for Month Scale Environmental Factors', color_bar_label= 'Comparative Feature/Factor Value')
