#! python3.
import praw
#import pandas as pd
import datetime as dt
reddit = praw.Reddit(client_id='wHT8kEmws_FWWQ', \
                     client_secret='4VBpGRWTUMqA8UQb5AfLMyMh8QY', \
                     user_agent='scraper', \
                     username='SaveOurGayFrogs', \
                     password='3631247ihatemyself?><')
                    
                    
subreddit = reddit.subreddit('nottheonion')
top_subreddit = subreddit.top(limit=999)

dict2 = { "title":[],
         "url":[] }


for submission in top_subreddit:
    dict2["title"].append(submission.title)
    dict2["url"].append(submission.url)
    
print(dict2['title'])

f = open("dict3.txt","w")
f.write( str(dict2) )
f.close()