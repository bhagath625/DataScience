#!/usr/bin/env python
# coding: utf-8

# # Clean and Analyze Employee Exit Surveys
# In this project, we'll clean and analyze exit surveys from employees of the Department of Education, Training and Employment (DETE)}) and the Technical and Further Education (TAFE) body of the Queensland government in Australia. The TAFE exit survey can be found here and the survey for the DETE can be found here.
# 
# We'll pretend our stakeholders want us to combine the results for both surveys to answer the following question:
# 
#    Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?
#     
# # Introduction
# First, we'll read in the datasets and do some initial exporation.

# In[1]:


#Read in the data
import pandas as pd
import numpy as np
dete_survey = pd.read_csv('dete_survey.csv')

#Quick exploration of the data
pd.options.display.max_columns = 150 # to avoid truncated output 
dete_survey.head()


# In[2]:


dete_survey.info()


# In[3]:


#Read in the data
tafe_survey = pd.read_csv("tafe_survey.csv")

#Quick exploration of the data
tafe_survey.head()


# In[4]:


tafe_survey.info()


# We can make the following observations based on the work above:
# 
# 1. The dete_survey dataframe contains 'Not Stated' values that indicate values are missing, but they aren't represented as NaN.
# 2. Both the dete_survey and tafe_survey contain many columns that we don't need to complete our analysis.
# 3. Each dataframe contains many of the same columns, but the column names are different.
# 4. There are multiple columns/answers that indicate an employee resigned because they were dissatisfied.
# 
# # Identify Missing Values and Drop Unneccessary Columns
# First, we'll correct the Not Stated values and drop some of the columns we don't need for our analysis.

# In[5]:


# Read in the data again, but this time read `Not Stated` values as `NaN`
dete_survey = pd.read_csv('dete_survey.csv', na_values='Not Stated')

# Quick exploration of the data
dete_survey.head()


# In[6]:


# Remove columns we don't need for our analysis
dete_survey_updated = dete_survey.drop(dete_survey.columns[28:49], axis=1)
tafe_survey_updated = tafe_survey.drop(tafe_survey.columns[17:66], axis=1)

#Check that the columns were dropped
print(dete_survey_updated.columns)
print(tafe_survey_updated.columns)


# # Rename Columns
# Next, we'll standardize the names of the columns we want to work with, because we eventually want to combine the dataframes.

# In[7]:


# Clean the column names
dete_survey_updated.columns = dete_survey_updated.columns.str.lower().str.strip().str.replace(' ', '_')

# Check that the column names were updated correctly
dete_survey_updated.columns


# In[8]:


# Update column names to match the names in dete_survey_updated
mapping = {'Record ID': 'id', 'CESSATION YEAR': 'cease_date', 'Reason for ceasing employment': 'separationtype', 'Gender. What is your Gender?': 'gender', 'CurrentAge. Current Age': 'age',
       'Employment Type. Employment Type': 'employment_status',
       'Classification. Classification': 'position',
       'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service',
       'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'}
tafe_survey_updated = tafe_survey_updated.rename(mapping, axis = 1)

# Check that the specified column names were updated correctly
tafe_survey_updated.columns


# # Filter the Data
# For this project, we'll only analyze survey respondents who resigned, so we'll only select separation types containing the string 'Resignation'.

# In[9]:


# Check the unique values for the separationtype column
tafe_survey_updated['separationtype'].value_counts()


# In[10]:


# Check the unique values for the separationtype column
dete_survey_updated['separationtype'].value_counts()


# In[11]:


# Update all separation types containing the word "resignation" to 'Resignation'
dete_survey_updated['separationtype'] = dete_survey_updated['separationtype'].str.split('-').str[0]

# Check the values in the separationtype column were updated correctly
dete_survey_updated['separationtype'].value_counts()


# In[12]:


# Select only the resignation separation types from each dataframe
dete_resignations = dete_survey_updated[dete_survey_updated['separationtype'] == 'Resignation'].copy()
tafe_resignations = tafe_survey_updated[tafe_survey_updated['separationtype'] == 'Resignation'].copy()


# # Verify the Data
# Below, we clean and explore the cease_date and dete_start_date columns to make sure all of the years make sense. We'll use the following criteria:
# 
# 1. Since the cease_date is the last year of the person's employment and the dete_start_date is the person's first year of employment, it wouldn't make sense to have years after the current date.
# 2. Given that most people in this field start working in their 20s, it's also unlikely that the dete_start_date was before the year 1940.

# In[13]:


# Check the unique values
dete_resignations['cease_date'].value_counts()


# In[14]:


# Extract the years and convert them to a float type
dete_resignations['cease_date'] = dete_resignations['cease_date'].str.split('/').str[-1]
dete_resignations['cease_date'] = dete_resignations['cease_date'].astype("float")

# Check the values again and look for outliers
dete_resignations['cease_date'].value_counts()


# In[15]:


# Check the unique values and look for outliers
dete_resignations['dete_start_date'].value_counts().sort_values()


# In[16]:


# Check the unique values
tafe_resignations['cease_date'].value_counts().sort_values()


# # Below are our findings:
# 
# The years in both dataframes don't completely align. The tafe_survey_updated dataframe contains some cease dates in 2009, but the dete_survey_updated dataframe does not. The tafe_survey_updated dataframe also contains many more cease dates in 2010 than the dete_survey_updaed dataframe. Since we aren't concerned with analyzing the results by year, we'll leave them as is.
# 
# # Create a New Column
# Since our end goal is to answer the question below, we need a column containing the length of time an employee spent in their workplace, or years of service, in both dataframes.
# 
# End goal: Are employees who have only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been at the job longer?
# 
# The tafe_resignations dataframe already contains a "service" column, which we renamed to institute_service.
# 
# Below, we calculate the years of service in the dete_survey_updated dataframe by subtracting the dete_start_date from the cease_date and create a new column named institute_service.

# In[17]:


# Calculate the length of time an employee spent in their respective workplace and create a new column
dete_resignations['institute_service'] = dete_resignations['cease_date'] - dete_resignations['dete_start_date']

# Quick check of the result
dete_resignations['institute_service'].head()


# # Identify Dissatisfied Employees
# Next, we'll identify any employees who resigned because they were dissatisfied. Below are the columns we'll use to categorize employees as "dissatisfied" from each dataframe:
# 
# 1. tafe_survey_updated:
#     1. Contributing Factors. Dissatisfaction
#     2. Contributing Factors. Job Dissatisfaction
# 2. dafe_survey_updated:
#     1. job_dissatisfaction
#     2. dissatisfaction_with_the_department
#     3. physical_work_environment
#     4. lack_of_recognition
#     5. lack_of_job_security
#     6. work_location
#     7. employment_conditions
#     8. work_life_balance
#     9. workload
#     
# If the employee indicated any of the factors above caused them to resign, we'll mark them as dissatisfied in a new column. After our changes, the new dissatisfied column will contain just the following values:
# 
# 1. True: indicates a person resigned because they were dissatisfied in some way
# 2. False: indicates a person resigned because of a reason other than dissatisfaction with the job
# 3. NaN: indicates the value is missing

# In[18]:


# Check the unique values
tafe_resignations['Contributing Factors. Dissatisfaction'].value_counts()


# In[19]:


# Check the unique values
tafe_resignations['Contributing Factors. Job Dissatisfaction'].value_counts()


# In[20]:


# Update the values in the contributing factors columns to be either True, False, or NaN
def update_vals(x):
    if x == '-':
        return False
    elif pd.isnull(x):
        return np.nan
    else:
        return True
tafe_resignations['dissatisfied'] = tafe_resignations[['Contributing Factors. Dissatisfaction', 'Contributing Factors. Job Dissatisfaction']].applymap(update_vals).any(1, skipna=False)
tafe_resignations_up = tafe_resignations.copy()

# Check the unique values after the updates
tafe_resignations_up['dissatisfied'].value_counts(dropna=False)


# In[21]:


# Update the values in columns related to dissatisfaction to be either True, False, or NaN
dete_resignations['dissatisfied'] = dete_resignations[['job_dissatisfaction',
       'dissatisfaction_with_the_department', 'physical_work_environment',
       'lack_of_recognition', 'lack_of_job_security', 'work_location',
       'employment_conditions', 'work_life_balance',
       'workload']].any(1, skipna=False)
dete_resignations_up = dete_resignations.copy()
dete_resignations_up['dissatisfied'].value_counts(dropna=False)


# # Combining the Data
# Below, we'll add an institute column so that we can differentiate the data from each survey after we combine them. Then, we'll combine the dataframes and drop any remaining columns we don't need.

# In[22]:


# Add an institute column
dete_resignations_up['institute'] = 'DETE'
tafe_resignations_up['institute'] = 'TAFE'


# In[23]:


# Combine the dataframes
combined = pd.concat([dete_resignations_up, tafe_resignations_up], ignore_index=True)

# Verify the number of non null values in each column
combined.notnull().sum().sort_values()


# In[24]:


# Drop columns with less than 500 non null values
combined_updated = combined.dropna(thresh = 500, axis =1).copy()


# # Clean the Service Column
# Next, we'll clean the institute_service column and categorize employees according to the following definitions:
# 
# 1. New: Less than 3 years in the workplace
# 2. Experienced: 3-6 years in the workplace
# 3. Established: 7-10 years in the workplace
# 4. Veteran: 11 or more years in the workplace
# 
# Our analysis is based on this article, which makes the argument that understanding employee's needs according to career stage instead of age is more effective.

# In[25]:


# Check the unique values
combined_updated['institute_service'].value_counts(dropna=False)


# In[26]:


# Extract the years of service and convert the type to float
combined_updated['institute_service_up'] = combined_updated['institute_service'].astype('str').str.extract(r'(\d+)')
combined_updated['institute_service_up'] = combined_updated['institute_service_up'].astype('float')

# Check the years extracted are correct
combined_updated['institute_service_up'].value_counts()


# In[27]:


# Convert years of service to categories
def transform_service(val):
    if val >= 11:
        return "Veteran"
    elif 7 <= val < 11:
        return "Established"
    elif 3 <= val < 7:
        return "Experienced"
    elif pd.isnull(val):
        return np.nan
    else:
        return "New"
combined_updated['service_cat'] = combined_updated['institute_service_up'].apply(transform_service)

# Quick check of the update
combined_updated['service_cat'].value_counts()


# # Perform Some Initial Analysis
# Finally, we'll replace the missing values in the dissatisfied column with the most frequent value, False. Then, we'll calculate the percentage of employees who resigned due to dissatisfaction in each service_cat group and plot the results.
# 
# Note that since we still have additional missing values left to deal with, this is meant to be an initial introduction to the analysis, not the final analysis.

# In[28]:


# Verify the unique values
combined_updated['dissatisfied'].value_counts(dropna=False)


# In[29]:


# Replace missing values with the most frequent value, False
combined_updated['dissatisfied'] = combined_updated['dissatisfied'].fillna(False)


# In[30]:


# Calculate the percentage of employees who resigned due to dissatisfaction in each category
dis_pct = combined_updated.pivot_table(index='service_cat', values='dissatisfied')

# Plot the results
get_ipython().magic('matplotlib inline')
dis_pct.plot(kind='bar', rot=30)


# From the initial analysis above, we can tentatively conclude that employees with 7 or more years of service are more likely to resign due to some kind of dissatisfaction with the job than employees with less than 7 years of service. However, we need to handle the rest of the missing data to finalize our analysis.

# In[ ]:




