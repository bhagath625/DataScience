## 2. Grabbing data with SELECT ##

SELECT * FROM recent_grads LIMIT 10;

## 3. Filter your data with WHERE and LIMIT ##

SELECT Major, ShareWomen FROM recent_grads WHERE ShareWomen < 0.5;

## 4. Expressing Multiple Filters with AND ##

SELECT Major, Major_category, Median, ShareWomen FROM recent_grads WHERE ShareWomen > 0.5 AND Median > 50000

## 5. Returning One of Several Conditions With OR ##

SELECT Major, Median, Unemployed FROM recent_grads WHERE Median >= 10000 OR Unemployed <= 1000 LIMIT 20;

## 6. Grouping Operators With Parentheses ##

SELECT Major, Major_category, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Engineering') AND (ShareWomen > 0.5 OR Unemployment_rate < 0.051);

## 7. Specify Sorting Rules With ORDER BY ##

SELECT Major, ShareWomen, Unemployment_rate FROM recent_grads
WHERE ShareWomen > 0.3 AND Unemployment_rate < 0.1
ORDER BY ShareWomen DESC

## 8. Practice Writing A Query ##

SELECT Major_category, Major, Unemployment_rate FROM recent_grads WHERE Major_category='Engineering' OR Major_category='Physical Sciences' ORDER BY Unemployment_rate ASC