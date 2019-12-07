#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import csv

jeopardy = pandas.read_csv("jeopardy.csv")

jeopardy


# In[ ]:


jeopardy.columns


# In[ ]:


jeopardy.columns = ['Show Number', 'Air Date', 'Round', 'Category', 'Value', 'Question', 'Answer']


# In[ ]:


import re

def normalize_text(text):
    text = text.lower()
    text = re.sub("[^A-Za-z0-9\s]", "", text)
    return text

def normalize_values(text):
    text = re.sub("[^A-Za-z0-9\s]", "", text)
    try:
        text = int(text)
    except Exception:
        text = 0
    return text


# In[ ]:


jeopardy["clean_question"] = jeopardy["Question"].apply(normalize_text)
jeopardy["clean_answer"] = jeopardy["Answer"].apply(normalize_text)
jeopardy["clean_value"] = jeopardy["Value"].apply(normalize_values)


# In[ ]:


jeopardy


# In[ ]:


jeopardy["Air Date"] = pandas.to_datetime(jeopardy["Air Date"])


# In[ ]:


jeopardy.dtypes


# In[ ]:


def count_matches(row):
    split_answer = row["clean_answer"].split(" ")
    split_question = row["clean_question"].split(" ")
    if "the" in split_answer:
        split_answer.remove("the")
    if len(split_answer) == 0:
        return 0
    match_count = 0
    for item in split_answer:
        if item in split_question:
            match_count += 1
    return match_count / len(split_answer)

jeopardy["answer_in_question"] = jeopardy.apply(count_matches, axis=1)


# In[ ]:


jeopardy["answer_in_question"].mean()


# # Answer terms in the question
# The answer only appears in the question about 6% of the time. This isn't a huge number, and means that we probably can't just hope that hearing a question will enable us to figure out the answer. We'll probably have to study.

# In[ ]:


question_overlap = []
terms_used = set()

jeopardy = jeopardy.sort_values("Air Date")

for i, row in jeopardy.iterrows():
        split_question = row["clean_question"].split(" ")
        split_question = [q for q in split_question if len(q) > 5]
        match_count = 0
        for word in split_question:
            if word in terms_used:
                match_count += 1
        for word in split_question:
            terms_used.add(word)
        if len(split_question) > 0:
            match_count /= len(split_question)
        question_overlap.append(match_count)
jeopardy["question_overlap"] = question_overlap

jeopardy["question_overlap"].mean()


# # Question overlap
# There is about 70% overlap between terms in new questions and terms in old questions. This only looks at a small set of questions, and it doesn't look at phrases, it looks at single terms. This makes it relatively insignificant, but it does mean that it's worth looking more into the recycling of questions.

# In[ ]:


def determine_value(row):
    value = 0
    if row["clean_value"] > 800:
        value = 1
    return value

jeopardy["high_value"] = jeopardy.apply(determine_value, axis=1)


# In[ ]:


def count_usage(term):
    low_count = 0
    high_count = 0
    for i, row in jeopardy.iterrows():
        if term in row["clean_question"].split(" "):
            if row["high_value"] == 1:
                high_count += 1
            else:
                low_count += 1
    return high_count, low_count

comparison_terms = list(terms_used)[:5]
observed_expected = []
for term in comparison_terms:
    observed_expected.append(count_usage(term))

observed_expected


# In[ ]:


from scipy.stats import chisquare
import numpy as np

high_value_count = jeopardy[jeopardy["high_value"] == 1].shape[0]
low_value_count = jeopardy[jeopardy["high_value"] == 0].shape[0]

chi_squared = []
for obs in observed_expected:
    total = sum(obs)
    total_prop = total / jeopardy.shape[0]
    high_value_exp = total_prop * high_value_count
    low_value_exp = total_prop * low_value_count
    
    observed = np.array([obs[0], obs[1]])
    expected = np.array([high_value_exp, low_value_exp])
    chi_squared.append(chisquare(observed, expected))

chi_squared


# # Chi-squared results
# None of the terms had a significant difference in usage between high value and low value rows. Additionally, the frequencies were all lower than 5, so the chi-squared test isn't as valid. It would be better to run this test with only terms that have higher frequencies.
