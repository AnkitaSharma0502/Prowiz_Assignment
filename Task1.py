
#Task 1
import requests as rq

url="https://jsonplaceholder.typicode.com/posts"

# A  To fetch data from API

response=rq.get(url)

data=response.json()

print(type(data))

print(len(data))

# B fetching all posts and printing them

for i in data:
    print({i['userId']},
    {i['id']},
    {i['title']},
    {i['body']})

# saving response in dataframe
import pandas as pd

df=pd.DataFrame(data)

print(df.head(10))


# C distinct number of users

total_distinct_users=df['userId'].nunique()

print("Total number of distinct users are ",total_distinct_users)


# D user with highest number of posts

max_post_user =df.groupby('userId').size().max()

print(f"max post count is {max_post_user} ")

# E average word length for post title

df["title_word_count"] = df["title"].apply(lambda x: len(x.split()))

avg_word_length=df["title_word_count"].mean()

print("Average post title word length is ", avg_word_length)