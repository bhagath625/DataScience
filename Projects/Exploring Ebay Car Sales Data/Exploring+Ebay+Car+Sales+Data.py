#!/usr/bin/env python
# coding: utf-8

# # Analyzing Used Car Listings on eBay Kleinanzeigen
# 
# We will be working on a dataset of used cars from eBay Kleinanzeigen, a classifieds section of the German eBay website.
# 
# The dataset was originally scraped and uploaded to Kaggle. The version of the dataset we are working with is a sample of 50,000 data points that was prepared by Dataquest including simulating a less-cleaned version of the data.
# 
# The data dictionary provided with data is as follows:
# 
#   1. dateCrawled - When this ad was first crawled. All field-values are taken from this date.
#   2. name - Name of the car.
#   3. seller - Whether the seller is private or a dealer.
#   4. offerType - The type of listing
#   5. price - The price on the ad to sell the car.
#   6. abtest - Whether the listing is included in an A/B test.
#   7. vehicleType - The vehicle Type.
#   8. yearOfRegistration - The year in which which year the car was first registered.
#   9. gearbox - The transmission type.
#   10. powerPS - The power of the car in PS.
#   11. model - The car model name.
#   12. lometer - How many kilometers the car has driven.
#   13. monthOfRegistration - The month in which which year the car was first registered.
#   14. fuelType - What type of fuel the car uses.
#   15. brand - The brand of the car.
#   16. notRepairedDamage - If the car has a damage which is not yet repaired.
#   17. dateCreated - The date on which the eBay listing was created.
#   18. nrOfPictures - The number of pictures in the ad.
#   19. postalCode - The postal code for the location of the vehicle.
#   20.lastSeenOnline - When the crawler saw this ad last online.
#   
# The aim of this project is to clean the data and analyze the included used car listings.

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


autos = pd.read_csv('autos.csv', encoding='Latin-1')
autos.info()
autos.head()


# Our dataset contains 20 columns, most of which are stored as strings. There are a few columns with null values, but no columns have more than ~20% null values. There are some columns that contain dates stored as strings.
# 
# We'll start by cleaning the column names to make the data easier to work with.
# 
# # Clean Columns

# In[3]:


autos.columns


# We'll make a few changes here:
# 
#   1. Change the columns from camelcase to snakecase.
#   2. Change a few wordings to more accurately describe the columns.

# In[4]:


autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'ab_test',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code',
       'last_seen']
autos.head()


# # Initial Data Exploration and Cleaning
# We'll start by exploring the data to find obvious areas where we can clean the data.

# In[5]:


autos.describe(include='all')


# Our initial observations:
# 
#   1. There are a number of text columns where all (or nearly all) of the values are the same:
#      1. seller
#      2. offer_type
#   2. The num_photos column looks odd, we'll need to investigate this further.

# In[6]:


autos["num_photos"].value_counts()


# It looks like the num_photos column has 0 for every column. We'll drop this column, plus the other two we noted as mostly one value.

# In[7]:


autos = autos.drop(["num_photos", "seller", "offer_type"], axis=1)


# There are two columns, price and auto, which are numeric values with extra characters being stored as text. We'll clean and convert these.

# In[8]:


autos["price"] = (autos["price"]
                          .str.replace("$","")
                          .str.replace(",","")
                          .astype(int)
                          )
autos["price"].head()


# In[9]:


autos["odometer"] = (autos["odometer"]
                             .str.replace("km","")
                             .str.replace(",","")
                             .astype(int)
                             )
autos.rename({"odometer": "odometer_km"}, axis=1, inplace=True)
autos["odometer_km"].head()


# # Exploring Odometer and Price¶

# In[10]:


autos["odometer_km"].value_counts()


# We can see that the values in this field are rounded, which might indicate that sellers had to choose from pre-set options for this field. Additionally, there are more high mileage than low mileage vehicles.

# In[11]:


print(autos["price"].unique().shape)
print(autos["price"].describe())
autos["price"].value_counts().head(20)


# Again, the prices in this column seem rounded, however given there are 2357 unique values in the column, that may just be people's tendency to round prices on the site.
# 
# There are 1,421 cars listed with $0 price - given that this is only 2% of the of the cars, we might consider removing these rows. The maximum price is one hundred million dollars, which seems a lot, let's look at the highest prices further.

# In[12]:


autos["price"].value_counts().sort_index(ascending=False).head(20)


# In[13]:


autos["price"].value_counts().sort_index(ascending=True).head(20)


# There are a number of listings with prices below \$30, including about 1,500 at \$0. There are also a small number of listings with very high values, including 14 at around or over $1 million.
# 
# Given that eBay is an auction site, there could legitimately be items where the opening bid is \$1. We will keep the \$1 items, but remove anything above \$350,000, since it seems that prices increase steadily to that number and then jump up to less realistic numbers.

# In[14]:


autos = autos[autos["price"].between(1,351000)]
autos["price"].describe()


# # Exploring the date columns
# There are a number of columns with date information:
# 
#   1. date_crawled
#   2. registration_month
#   3. registration_year
#   4. ad_created
#   5. last_seen
# These are a combination of dates that were crawled, and dates with meta-information from the crawler. The non-registration dates are stored as strings.
# 
# We'll explore each of these columns to learn more about the listings.

# In[15]:


autos[['date_crawled','ad_created','last_seen']][0:5]


# In[16]:


(autos["date_crawled"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# In[17]:


(autos["date_crawled"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_values()
        )


# Looks like the site was crawled daily over roughly a one month period in March and April 2016. The distribution of listings crawled on each day is roughly uniform.

# In[18]:


(autos["last_seen"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# The crawler recorded the date it last saw any listing, which allows us to determine on what day a listing was removed, presumably because the car was sold.
# 
# The last three days contain a disproportionate amount of 'last seen' values. Given that these are 6-10x the values from the previous days, it's unlikely that there was a massive spike in sales, and more likely that these values are to do with the crawling period ending and don't indicate car sales.

# In[19]:


print(autos["ad_created"].str[:10].unique().shape)
(autos["ad_created"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# There is a large variety of ad created dates. Most fall within 1-2 months of the listing date, but a few are quite old, with the oldest at around 9 months.

# In[20]:


autos["registration_year"].describe()


# The year that the car was first registered will likely indicate the age of the car. Looking at this column, we note some odd values. The minimum value is 1000, long before cars were invented and the maximum is 9999, many years into the future.

# # Dealing with Incorrect Registration Year Data
# Because a car can't be first registered before the listing was seen, any vehicle with a registration year above 2016 is definitely inaccurate. Determining the earliest valid year is more difficult. Realistically, it could be somewhere in the first few decades of the 1900s.
# 
# One option is to remove the listings with these values. Let's determine what percentage of our data has invalid values in this column:

# In[21]:


(~autos["registration_year"].between(1900,2016)).sum() / autos.shape[0]


# Given that this is less than 4% of our data, we will remove these rows.

# In[22]:


# Many ways to select rows in a dataframe that fall within a value range for a column.
# Using `Series.between()` is one way.
autos = autos[autos["registration_year"].between(1900,2016)]
autos["registration_year"].value_counts(normalize=True).head(10)


# It appears that most of the vehicles were first registered in the past 20 years.
# 
# # Exploring Price by Brand

# In[23]:


autos["brand"].value_counts(normalize=True)


# German manufacturers represent four out of the top five brands, almost 50% of the overall listings. Volkswagen is by far the most popular brand, with approximately double the cars for sale of the next two brands combined.
# 
# There are lots of brands that don't have a significant percentage of listings, so we will limit our analysis to brands representing more than 5% of total listings.

# In[24]:


brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)


# In[25]:


brand_mean_prices = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price"].mean()
    brand_mean_prices[brand] = int(mean_price)

brand_mean_prices


# Of the top 5 brands, there is a distinct price gap:
# 
#   1. Audi, BMW and Mercedes Benz are more expensive
#   2. Ford and Opel are less expensive
#   3. Volkswagen is in between - this may explain its popularity, it may be a 'best of 'both worlds' option.

# # Exploring Mileage

# In[26]:


bmp_series = pd.Series(brand_mean_prices)
pd.DataFrame(bmp_series, columns=["mean_price"])


# In[27]:


brand_mean_mileage = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_mileage = brand_only["odometer_km"].mean()
    brand_mean_mileage[brand] = int(mean_mileage)

mean_mileage = pd.Series(brand_mean_mileage).sort_values(ascending=False)
mean_prices = pd.Series(brand_mean_prices).sort_values(ascending=False)


# In[28]:


brand_info = pd.DataFrame(mean_mileage,columns=['mean_mileage'])
brand_info


# In[29]:


brand_info["mean_price"] = mean_prices
brand_info


# The range of car mileages does not vary as much as the prices do by brand, instead all falling within 10% for the top brands. There is a slight trend to the more expensive vehicles having higher mileage, with the less expensive vehicles having lower mileage.

# In[ ]:




