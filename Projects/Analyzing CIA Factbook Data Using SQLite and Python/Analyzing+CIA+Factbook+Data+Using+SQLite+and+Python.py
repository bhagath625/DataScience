#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
import pandas as pd

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
cursor.execute(q1).fetchall()


# In[4]:


q1 = "SELECT * FROM sqlite_master WHERE type='table';"
pd.read_sql_query(q1, conn)


# In[5]:


q2 = "select * from facts limit 5"
pd.read_sql_query(q2, conn)


# # Summary Statistics

# In[6]:


q3 = '''
select min(population) min_pop, max(population) max_pop, 
min(population_growth) min_pop_grwth, max(population_growth) max_pop_grwth 
from facts
'''
pd.read_sql_query(q3, conn)


# # Outliers

# In[7]:


q4 = '''
select *
from facts
where population == (select max(population) from facts);
'''

pd.read_sql_query(q4, conn)


# In[8]:


q5 = '''
select *
from facts
where population == (select min(population) from facts);
'''

pd.read_sql_query(q5, conn)


# # Histograms

# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

q6 = '''
select population, population_growth, birth_rate, death_rate
from facts
where population != (select max(population) from facts)
and population != (select min(population) from facts);
'''
pd.read_sql_query(q6, conn).hist(ax=ax)


# # Which countries have the highest population density?

# In[10]:


q7 = "select name, cast(population as float)/cast(area as float) density from facts order by density desc limit 20"
pd.read_sql_query(q7, conn)


# In[11]:


q7 = '''select population, population_growth, birth_rate, death_rate
from facts
where population != (select max(population) from facts)
and population != (select min(population) from facts);
'''
pd.read_sql_query(q7, conn)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




