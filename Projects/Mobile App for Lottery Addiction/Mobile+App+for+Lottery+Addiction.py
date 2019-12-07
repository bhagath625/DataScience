#!/usr/bin/env python
# coding: utf-8

# # Mobile App for Lottery Addiction
# In this project, we are going to contribute to the development of a mobile app by writing a couple of functions that are mostly focused on calculating probabilities. The app is aimed to both prevent and treat lottery addiction by helping people better estimate their chances of winning.
# 
# The app idea comes from a medical institute which is specialized in treating gambling addictions. The institute already has a team of engineers that will build the app, but they need us to create the logical core of the app and calculate probabilities. For the first version of the app, they want us to focus on the 6/49 lottery and build functions that can answer users the following questions:
# 
# What is the probability of winning the big prize with a single ticket?
# What is the probability of winning the big prize if we play 40 different tickets (or any other number)?
# What is the probability of having at least five (or four, or three) winning numbers on a single ticket?
# The scenario we're following throughout this project is fictional — the main purpose is to practice applying probability and combinatorics (permutations and combinations) concepts in a setting that simulates a real-world scenario.
# 
# # Core Functions
# Below, we're going to write two functions that we'll be using frequently:
# 
# factorial() — a function that calculates factorials
# combinations() — a function that calculates combinations

# In[ ]:


def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n-k)
    return numerator/denominator


# # One-ticket Probability
# We need to build a function that calculates the probability of winning the big prize for any given ticket. For each drawing, six numbers are drawn from a set of 49, and a player wins the big prize if the six numbers on their tickets match all six numbers.
# 
# The engineer team told us that we need to be aware of the following details when we write the function:
# 
# Inside the app, the user inputs six different numbers from 1 to 49.
# Under the hood, the six numbers will come as a Python list and serve as an input to our function.
# The engineering team wants the function to print the probability value in a friendly way — in a way that people without any probability training are able to understand.
# Below, we write the one_ticket_probability() function, which takes in a list of six unique numbers and prints the probability of winning in a way that's easy to understand.

# In[ ]:


def one_ticket_probability(user_numbers):
    
    n_combinations = combinations(49, 6)
    probability_one_ticket = 1/n_combinations
    percentage_form = probability_one_ticket * 100
    
    print('''Your chances to win the big prize with the numbers {} are {:.7f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(user_numbers,
                    percentage_form, int(n_combinations)))


# We now test a bit the function on two different outputs.

# In[ ]:


test_input_1 = [2, 43, 22, 23, 11, 5]
one_ticket_probability(test_input_1)


# Your chances to win the big prize with the numbers [2, 43, 22, 23, 11, 5] are 0.0000072%.
# In other words, you have a 1 in 13,983,816 chances to win.

# In[ ]:


test_input_2 = [9, 26, 41, 7, 15, 6]
one_ticket_probability(test_input_2)


# Your chances to win the big prize with the numbers [9, 26, 41, 7, 15, 6] are 0.0000072%.
# In other words, you have a 1 in 13,983,816 chances to win.
# # Historical Data Check for Canada Lottery
# The institute also wants us to consider the data coming from the national 6/49 lottery game in Canada. The data set contains historical data for 3,665 drawings, dating from 1982 to 2018 (the data set can be downloaded from here).

# In[ ]:


import pandas as pd

lottery_canada = pd.read_csv('649.csv')
lottery_canada.shape


# In[ ]:


lottery_canada.head(3)


# In[ ]:


lottery_canada.tail(3)


# # Function for Historical Data Check
# The engineering team tells us that we need to write a function that can help users determine whether they would have ever won by now using a certain combination of six numbers. These are the details we'll need to be aware of:
# 
# Inside the app, the user inputs six different numbers from 1 to 49.
# Under the hood, the six numbers will come as a Python list and serve as an input to our function.
# The engineering team wants us to write a function that prints:
# the number of times the combination selected occurred; and
# the probability of winning the big prize in the next drawing with that combination.
# We're going to begin by extracting all the winning numbers from the lottery data set. The extract_numbers() function will go over each row of the dataframe and extract the six winning numbers as a Python set.

# In[ ]:


def extract_numbers(row):
    row = row[4:10]
    row = set(row.values)
    return row

winning_numbers = lottery_canada.apply(extract_numbers, axis=1)
winning_numbers.head()


# Below, we write the check_historical_occurrence() function that takes in the user numbers and the historical numbers and prints information with respect to the number of occurrences and the probability of winning in the next drawing.

# In[ ]:


def check_historical_occurrence(user_numbers, historical_numbers):   
    '''
    user_numbers: a Python list
    historical numbers: a pandas Series
    '''
    
    user_numbers_set = set(user_numbers)
    check_occurrence = historical_numbers == user_numbers_set
    n_occurrences = check_occurrence.sum()
    
    if n_occurrences == 0:
        print('''The combination {} has never occured.
This doesn't mean it's more likely to occur now. Your chances to win the big prize in the next drawing using the combination {} are 0.0000072%.
In other words, you have a 1 in 13,983,816 chances to win.'''.format(user_numbers, user_numbers))
        
    else:
        print('''The number of times combination {} has occured in the past is {}.
Your chances to win the big prize in the next drawing using the combination {} are 0.0000072%.
In other words, you have a 1 in 13,983,816 chances to win.'''.format(user_numbers, n_occurrences,
                                                                            user_numbers))


# In[ ]:


test_input_3 = [33, 36, 37, 39, 8, 41]
check_historical_occurrence(test_input_3, winning_numbers)


# In[ ]:


test_input_4 = [3, 2, 44, 22, 1, 44]
check_historical_occurrence(test_input_4, winning_numbers)


# # Multi-ticket Probability
# For the first version of the app, users should also be able to find the probability of winning if they play multiple different tickets. For instance, someone might intend to play 15 different tickets and they want to know the probability of winning the big prize.
# 
# The engineering team wants us to be aware of the following details when we're writing the function:
# 
# The user will input the number of different tickets they want to play (without inputting the specific combinations they intend to play).
# Our function will see an integer between 1 and 13,983,816 (the maximum number of different tickets).
# The function should print information about the probability of winning the big prize depending on the number of different tickets played.
# The multi_ticket_probability() function below takes in the number of tickets and prints probability information depending on the input.

# In[ ]:


def multi_ticket_probability(n_tickets):
    
    n_combinations = combinations(49, 6)
    
    probability = n_tickets / n_combinations
    percentage_form = probability * 100
    
    if n_tickets == 1:
        print('''Your chances to win the big prize with one ticket are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(percentage_form, int(n_combinations)))
    
    else:
        combinations_simplified = round(n_combinations / n_tickets)   
        print('''Your chances to win the big prize with {:,} different tickets are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(n_tickets, percentage_form,
                                                               combinations_simplified))


# Below, we run a couple of tests for our function.

# In[ ]:


test_inputs = [1, 10, 100, 10000, 1000000, 6991908, 13983816]

for test_input in test_inputs:
    multi_ticket_probability(test_input)
    print('------------------------') # output delimiter


# # Less Winning Numbers — Function
# In most 6/49 lotteries, there are smaller prizes if a player's ticket match two, three, four, or five of the six numbers drawn. This means that players might be interested in finding out the probability of having two, three, four, or five winning numbers — for the first version of the app, users should be able to find those probabilities.
# 
# These are the details we need to be aware of when we write a function to make the calculations of those probabilities possible:
# 
# Inside the app, the user inputs:
# six different numbers from 1 to 49; and
# an integer between 2 and 5 that represents the number of winning numbers expected
# Our function prints information about the probability of having a certain number of winning numbers
# To calculate the probabilities, we tell the engineering team that the specific combination on the ticket is irrelevant and we only need the integer between 2 and 5 representing the number of winning numbers expected. Consequently, we will write a function named probability_less_6() which takes in an integer and prints information about the chances of winning depending on the value of that integer.

# In[ ]:


def probability_less_6(n_winning_numbers):
    
    n_combinations_ticket = combinations(6, n_winning_numbers)
    n_combinations_remaining = combinations(49 - n_winning_numbers,
                                           6 - n_winning_numbers)
    successful_outcomes = n_combinations_ticket * n_combinations_remaining
    n_combinations_total = combinations(49, 6)
    
    probability = successful_outcomes / n_combinations_total
    probability_percentage = probability * 100
    
    combinations_simplified = round(n_combinations_total/successful_outcomes)
    
    print('''Your chances of having {} winning numbers with this ticket are {:.6f}%.
In other words, you have a 1 in {:,} chances to win.'''.format(n_winning_numbers, probability_percentage,
                                                               int(combinations_simplified)))


# Now, let's test the function on all the three possible inputs.

# # Next steps
# For the first version of the app, we coded four main functions:
# 
# one_ticket_probability() — calculates the probability of winning the big prize with a single ticket
# check_historical_occurrence() — checks whether a certain combination has occurred in the Canada lottery data set
# multi_ticket_probability() — calculates the probability for any number of of tickets between 1 and 13,983,816
# probability_less_6() — calculates the probability of having two, three, four or five winning numbers
# Possible features for a second version of the app include:
# 
# Making the outputs even easier to understand by adding fun analogies (for example, we can find probabilities for strange events and compare with the chances of winning in lottery; for instance, we can output something along the lines "You are 100 times more likely to be the victim of a shark attack than winning the lottery")
# Combining the one_ticket_probability() and check_historical_occurrence() to output information on probability and historical occurrence at the same time

# In[ ]:





# In[ ]:





# In[ ]:




