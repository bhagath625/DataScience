#!/usr/bin/env python
# coding: utf-8

# # Exploring Hackers News Posts
# 
# In this project, we'll compare two different types of posts from Hacker News, a popular site where technology related stories (or 'posts') are voted and commented upon. The two types of posts we'll explore begin with either Ask HN or Show HN.
# 
# Users submit Ask HN posts to ask the Hacker News community a specific question, such as "What is the best online course you've ever taken?" Likewise, users submit Show HN posts to show the Hacker News community a project, product, or just generally something interesting.
# 
# We'll specifically compare these two types of posts to determine the following:
# 
#   1. Do Ask HN or Show HN receive more comments on average?
#   2. Do posts created at a certain time receive more comments on average?
# It should be noted that the data set we're working with was reduced from almost 300,000 rows to approximately 20,000 rows by removing all submissions that did not receive any comments, and then randomly sampling from the remaining submissions.
# 
# # Introduction
# First, we'll read in the data and remove the headers.

# In[1]:


# Read in the data.
import csv

f = open('hacker_news.csv')
hn = list(csv.reader(f))
hn[:5]


# # Removing Headers from a List of Lists

# In[2]:


# Remove the headers.
headers = hn[0]
hn = hn[1:]
print(headers)
print(hn[:5])


# We can see above that the data set contains the title of the posts, the number of comments for each post, and the date the post was created. Let's start by exploring the number of comments for each type of post.

# # Extracting Ask HN and Show HN Posts
# First, we'll identify posts that begin with either Ask HN or Show HN and separate the data for those two types of posts into different lists. Separating the data makes it easier to analyze in the following steps.

# In[3]:


# Identify posts that begin with either `Ask HN` or `Show HN` and separate the data into different lists.
ask_posts = []
show_posts =[]
other_posts = []

for post in hn:
    title = post[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(post)
    elif title.lower().startswith("show hn"):
        show_posts.append(post)
    else:
        other_posts.append(post)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# # Calculating the Average Number of Comments for Ask HN and Show HN Posts
# Now that we separated ask posts and show posts into different lists, we'll calculate the average number of comments each type of post receives.

# In[4]:


# Calculate the average number of comments `Ask HN` posts receive.
total_ask_comments = 0

for post in ask_posts:
    total_ask_comments += int(post[4])
    
avg_ask_comments = total_ask_comments / len(ask_posts)
print(avg_ask_comments)


# In[5]:


total_show_comments = 0

for post in show_posts:
    total_show_comments += int(post[4])
    
avg_show_comments = total_show_comments / len(show_posts)
print(avg_show_comments)


# On average, ask posts in our sample receive approximately 14 comments, whereas show posts receive approximately 10. Since ask posts are more likely to receive comments, we'll focus our remaining analysis just on these posts.

# # Finding the Amount of Ask Posts and Comments by Hour Created
# Next, we'll determine if we can maximize the amount of comments an ask post receives by creating it at a certain time. First, we'll find the amount of ask posts created during each hour of day, along with the number of comments those posts received. Then, we'll calculate the average amount of comments ask posts created at each hour of the day receive.

# In[6]:


# Calculate the amount of ask posts created during each hour of day and the number of comments received.
import datetime as dt

result_list = []

for post in ask_posts:
    result_list.append(
        [post[6], int(post[4])]
    )

comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour


# # Calculating the Average Number of Comments for Ask HN Posts by Hour

# In[7]:


# Calculate the average amount of comments `Ask HN` posts created at each hour of the day receive.
avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])

avg_by_hour


# # Sorting and Printing Values from a List of Lists

# In[8]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
    
print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap


# In[9]:


# Sort the values and print the the 5 hours with the highest average comments.

print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )


# The hour that receives the most comments per post on average is 15:00, with an average of 38.59 comments per post. There's about a 60% increase in the number of comments between the hours with the highest and second highest average number of comments.
# 
# According to the data set documentation, the timezone used is Eastern Time in the US. So, we could also write 15:00 as 3:00 pm est.
# 
# # Conclusion
# In this project, we analyzed ask posts and show posts to determine which type of post and time receive the most comments on average. Based on our analysis, to maximize the amount of comments a post receives, we'd recommend the post be categorized as ask post and created between 15:00 and 16:00 (3:00 pm est - 4:00 pm est).
# 
# However, it should be noted that the data set we analyzed excluded posts without any comments. Given that, it's more accurate to say that of the posts that received comments, ask posts received more comments on average and ask posts created between 15:00 and 16:00 (3:00 pm est - 4:00 pm est) received the most comments on average.

# In[ ]:




