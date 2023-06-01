import pandas as pd
import snscrape.modules.twitter as sntwitter
from collections import defaultdict

def export_df_tweets(length, query):
    
    scraper = sntwitter.TwitterSearchScraper(query=query)

    d = defaultdict(list)
    for idx, tweet in enumerate(scraper.get_items()):
        
        print(idx)
        
        s = [('id', tweet.id), 
            ('content', tweet.rawContent), 
            ('user_name', tweet.user.username), 
            ('like_count', tweet.likeCount), 
            ('rt_count', tweet.retweetCount),
            ('date', tweet.date)]
        
        for k, v in s:
            if(v in d['id']):
                break
            d[k].append(v)
                
        if(idx>length):
            break
        
    df = pd.DataFrame(d)
    df.to_csv (r'data/tweets_lemonde.csv', index = None)
    
#export_df_tweets(400000, "'from:lemondefr'")
