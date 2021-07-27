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

from feature_selector import FeatureSelector


filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')
data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')


y2009 = data.loc[data['year']==2009]
y2014 =  data.loc[data['year']==2014]
y2016 =  data.loc[data['year']==2016]
y2018 =  data.loc[data['year']==2018]

eb2009 = data.loc[data['year']!=2009]
eb2014 = data.loc[data['year']!=2014]
eb2016 =  data.loc[data['year']!=2016]
eb2018 =  data.loc[data['year']!=2018]

Xcol = y2009.columns[5:]

#Y=y2014['me_rt_hh_district_prop']
#Y=y2016['me_rt_hh_district_prop']
#Y=y2018['me_rt_hh_district_prop']

Y_train = eb2009['me_rt_hh_district_prop']
X_train = eb2009[Xcol]
X_test =  y2009[Xcol]
Y_test= y2009['me_rt_hh_district_prop']


rf = RandomForestRegressor(random_state=42)

rf_fit = rf.fit(X_train,Y_train)

Y_predict = rf_fit.predict(X_test)

pred_sum2009 = np.sum(Y_predict)
act_sum2009 = np.sum(Y_test)
pred_std2009 = np.std(Y_predict)
act_std2009 = np.std(Y_test)


mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(rmse)
print('Predicted sum is:', pred_sum2009)
print('Predicted standard deviation is:', pred_std2009)
print('Actual sum is:', act_sum2009)
print('Actual standard deviation is:', act_std2009)
