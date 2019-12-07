#!/usr/bin/env python
# coding: utf-8

# # Introduction

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
recent_grads = pd.read_csv('recent-grads.csv')
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
recent_grads = recent_grads.dropna()


# # Pandas, Scatter Plots

# In[2]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# In[3]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')


# In[4]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# In[5]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# In[6]:


recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[7]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# # Pandas, Histograms

# In[8]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(1,5):
    ax = fig.add_subplot(4,1,r)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)


# In[9]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(4,8):
    ax = fig.add_subplot(4,1,r-3)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)


# # Pandas, Scatter Matrix Plot

# In[10]:


from pandas.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(6,6))


# In[11]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# # Pandas, Bar Plots

# In[12]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[ ]:




