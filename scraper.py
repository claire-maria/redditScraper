#! python3.
import praw
reddit = praw.Reddit(client_id='wHT8kEmws_FWWQ', \
                     client_secret='4VBpGRWTUMqA8UQb5AfLMyMh8QY', \
                     user_agent='scraper', \
                     username='xxxxxxxxxxxxx' \
                     password='xxxxxxxxxxxxxxxxx')
                    
                    
subreddit = reddit.subreddit('TheOnion')
top_subreddit = subreddit.top(limit=999)

dict = { "title":[],
         "url":[] }


for submission in top_subreddit:
    dict["title"].append(submission.title)
    dict["url"].append(submission.url)
    
print(dict['title'])

f = open("dict2.txt","w")
f.write( str(dict) )
f.close()
