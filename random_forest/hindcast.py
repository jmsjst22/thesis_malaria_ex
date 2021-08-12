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

# Get data
filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')
data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')

# Define for data of specific year
y2009 = data.loc[data['year']==2009]
y2014 =  data.loc[data['year']==2014]
y2016 =  data.loc[data['year']==2016]
y2018 =  data.loc[data['year']==2018]

# Define for data of all but a specific year
eb2009 = data.loc[data['year']!=2009]
eb2014 = data.loc[data['year']!=2014]
eb2016 =  data.loc[data['year']!=2016]
eb2018 =  data.loc[data['year']!=2018]

#define training phase X
Xcol = eb2018.columns[5:]
#define validation set X
ValX = y2018.columns[5:]


#selecting all label data (malaria transmission proportion) from non-excluded year
Y= eb2018['me_rt_hh_district_prop']
#selecting all feature data from non-excluded year
X = eb2018[Xcol]
#testing on data proportionate to excluded year proportion of all data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

#selecting validation data to test how the model predicts with unseen data
X_Val = y2018[ValX]
#selecting actual data for the predictions to be validated against
Y_act = y2018['me_rt_hh_district_prop']

rf = RandomForestRegressor(random_state=42)
#fit model
rf_fit = rf.fit(X_train,Y_train)

# Predict with model fit for all but 2014 on 2014
Y_validate = rf_fit.predict(X_Val)
act_std2018 = np.std(Y_act)
pred_std2018 = np.std(Y_validate)
# Test error between actual data and modelled data for model trained on all but 2014
mse = mean_squared_error(Y_validate,Y_act)
rmse = np.sqrt(mse)
print(rmse)
print('Actual standard deviation is:', act_std2018)
print('Predicted standard deviation is:', pred_std2018)
