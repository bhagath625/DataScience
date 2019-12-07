#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas

bike_rentals = pandas.read_csv("bike_rental_hour.csv")
bike_rentals.head()


# In[2]:


get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt

plt.hist(bike_rentals["cnt"])


# In[3]:


bike_rentals.corr()["cnt"]


# In[4]:


def assign_label(hour):
    if hour >=0 and hour < 6:
        return 4
    elif hour >=6 and hour < 12:
        return 1
    elif hour >= 12 and hour < 18:
        return 2
    elif hour >= 18 and hour <=24:
        return 3

bike_rentals["time_label"] = bike_rentals["hr"].apply(assign_label)


# # Error metric
# The mean squared error metric makes the most sense to evaluate our error. MSE works on continuous numeric data, which fits our data quite well.

# In[5]:


train = bike_rentals.sample(frac=.8)


# In[6]:


test = bike_rentals.loc[~bike_rentals.index.isin(train.index)]


# In[7]:


from sklearn.linear_model import LinearRegression

predictors = list(train.columns)
predictors.remove("cnt")
predictors.remove("casual")
predictors.remove("registered")
predictors.remove("dteday")

reg = LinearRegression()

reg.fit(train[predictors], train["cnt"])


# In[8]:


import numpy
predictions = reg.predict(test[predictors])

numpy.mean((predictions - test["cnt"]) ** 2)


# # Error
# The error is very high, which may be due to the fact that the data has a few extremely high rental counts, but otherwise mostly low counts. Larger errors are penalized more with MSE, which leads to a higher total error.

# In[9]:


from sklearn.tree import DecisionTreeRegressor

reg = DecisionTreeRegressor(min_samples_leaf=5)

reg.fit(train[predictors], train["cnt"])


# In[10]:


predictions = reg.predict(test[predictors])

numpy.mean((predictions - test["cnt"]) ** 2)


# In[11]:


reg = DecisionTreeRegressor(min_samples_leaf=2)

reg.fit(train[predictors], train["cnt"])

predictions = reg.predict(test[predictors])

numpy.mean((predictions - test["cnt"]) ** 2)


# # Decision tree error
# By taking the nonlinear predictors into account, the decision tree regressor appears to have much higher accuracy than linear regression.

# In[12]:


from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor(min_samples_leaf=5)
reg.fit(train[predictors], train["cnt"])


# In[13]:


predictions = reg.predict(test[predictors])

numpy.mean((predictions - test["cnt"]) ** 2)


# # Random forest error
# By removing some of the sources of overfitting, the random forest accuracy is improved over the decision tree accuracy.

# In[ ]:




