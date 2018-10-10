import tweepy
import time
import json
consumer_key = "VpsiBVvol7gGjcXhtkFAqMoBf"
consumer_secret="jyIEZKTAHhNLWMXKlFhK7EvuvNqUFGhKTOl692Ofwiwd9pumvJ"
access_key ="2286445472-bUTuy2HbUv5zy1uoeRLFiylLP5UzIAqWGJHSTZo"
access_secret="JimVlQsxcwmw8xGc61ALt5jkrur546hGE8VLqmDYw4FgA"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth)

def get_tweets(query):
    api = tweepy.API(auth)
    try:
        tweets = api.search(query)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]
    return tweets
    
import re
def Data_clean(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

import csv
TweetSearchqueries = ["#HanSolo", "\"Nova Scotia\"","#realDonaldTrump","#techsytalk","#GOT","#Canada","#SRK","#indiaissues","#halifax","#DalMacs"
          ,"#Dalfest","#KiteFestival","#Music","#Obama","#Goa","#disneyland","#Halloween","#YJHD","#ZNMD","#Feminism","#Violence"]
with open ('tweets.csv', 'w', encoding="utf-8", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id','user','created_at','text'])
    for query in TweetSearchqueries:
        t = get_tweets(query)
        for tweet in t:
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,Data_clean(tweet.text)])  
