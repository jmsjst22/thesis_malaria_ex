from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score, mean_squared_error #c stat
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import pandas as pd
from sklearn.inspection import permutation_importance
import shap

# Define directory
filepath = ('/home/s1987119/Diss_data/Final/Final_Products/final_outputs/')
# Read CSV
data = pd.read_csv(filepath+'FINAL_RT_WO_ref_mr.csv')
# Select columns with all feature data in
Xcol = data.columns[5:]
# Select data from selected columns
X = data[Xcol]
# Select data for labels in machine learning (predicted variable)
Y = data['me_rt_hh_district_prop']
# Train, test split populations of data for training and testing the data - randomly.
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

# Call RandomForestRegressor method
rf = RandomForestRegressor(random_state = 42)

# Train model with training populations of feature and label 
rf_fit = rf.fit(X_train,Y_train)

# Predict unseen Y from unseen X to test model performance
Y_predict = rf_fit.predict(X_test)

# Compute MSE for model error
mse = mean_squared_error(Y_test,Y_predict)
# mse --> rmse
rmse = np.sqrt(mse)
print(rmse)

# Call tree explainer module for visualisation and analysis using Shapley Value
explainer  = shap.TreeExplainer(rf_fit)
# Get Shapley Values for each feature from X_test
shap_values = explainer.shap_values(X_test)

# Get mean Shapley value for all features (mean for each feature)
vals= np.abs(shap_values).mean(0)
# Convert to dataframe with associated feature/Shapley value pair
feature_importance = pd.DataFrame(list(zip(X_train.columns,vals)),columns=['col_name','feature_importance_vals'])
# Sort values by feature importance 
feature_importance.sort_values(by=['feature_importance_vals'],ascending=False,inplace=True)
# Print column heads and top 5 rows of feature improtance for shapley
feature_importance.head()

# Test perm_importance for difference (permutation importance for feature removal/addition accuracy test - not used in current study)
perm_importance  = permutation_importance(rf_fit,X_test,Y_test)

# Sort permutation importance values 
sorted_idx = perm_importance.importances_mean.argsort()
print(sorted_idx)

# Plot bar graph of feature importances as measured by Shapley Value Mean
plt.barh(X_train.columns[sorted_idx], perm_importance.importances_mean[sorted_idx])
plt.show()
# Plot summary plot of shapley values for all query points (not just mean)
shap.summary_plot(shap_values,X_test, plot_type='bar')
# Edit plot
shap.summary_plot(shap_values,X_test, max_display = 10,  title='Shapley Values for Month Scale Environmental Factors', color_bar_label= 'Comparative Feature/Factor Value')
