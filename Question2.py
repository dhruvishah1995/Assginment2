import pandas as pd
import csv

with open("negative.csv", "r") as f:
    negText = f.read()
negWordList= negText.split("\n")
negWordList[-1:] = []

with open("positive.csv", "r") as f:
    posText = f.read()
posWordList = posText.split("\n")
posWordList[-1:] = []

df= pd.read_csv('tweets.csv')
tweetsList = df['text']

import re
def tokenize(TweetText):
    Tokens = re.findall(r'\b\w[\w-]*\b', TweetText.lower())
    return Tokens
    
def compareCalculate(TweetText):
    PosWordCount = 0
    NegWordCount = 0
    tweetsList = tokenize(TweetText)
    for word in tweetsList:
        if word in posWordList:
            PosWordCount += 1
      
    for word in tweetsList:
        if word in negTokens:
            NegWordCount += 1

    sum = (PosWordCount - NegWordCount)
    return sum

    ScoreList=[]
    SentimentList = []
    Sentence = []
    
for tweet in tweetsList:
        calc = compareCalculate(tweet)
        score = calc
        if calc==0 :
            status="neutral" 
        elif calc == -1 :
            status="negative"
        elif calc == 1 :
            status="Positive"
        
        Sentence.append(tweet)
        ScoreList.append(calc)
        SentimentList.append(status);
        
        df = pd.DataFrame(columns=["Sentence", "Score","Sentiment"])
        df["Sentence"] = Sentence
        df["Score"] = ScoreList
        df["Sentiment"] = SentimentList
        df.to_csv("output.csv", index=False)
