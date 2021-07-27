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
from scipy import stats
from scipy.stats.stats import pearsonr
from sklearn.feature_selection import SelectKBest, f_regression

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

Xcol = data.columns[5:]
print(Xcol)
X = data[Xcol]
Y = data['me_rt_hh_district_prop']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

from sklearn.feature_selection import RFE
rfe_selector = RFE(estimator=RandomForestRegressor(),n_features_to_select=1,step=1,verbose=-1)

rfefit = rfe_selector.fit(X_train,Y_train)

Y_predict = rfefit.predict(X_test)



mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))
print(nrmse)

accuracy = evaluate(rfefit,X_test,Y_test)




threshold = 0.9

def correlation(dataset,threshold):
    col_corr = set()
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if corr_matrix.iloc[i,j])>threshold:
                colname = corr_matrix.columns[i]
                col_corr.add(colname)
    return col_corr

corr_features = correlation(X_train,0.9)

len(set(corr_features))

X_train = X_train.drop(corr_features,axis=1)
X_test = X_test.drop(corr_features,axis=1)

rf = RandomForestRegressor()

rf_fit = rf.fit(X_train,Y_train)

Y_predict = rf_fit.predict(X_test)

mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
nrmse = rmse/(np.max(Y_predict)-np.min(Y_predict))
print(nrmse)

accuracy = evaluate(rf_fit,X_test,Y_test)


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
