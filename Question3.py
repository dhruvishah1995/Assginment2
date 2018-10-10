from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
import csv

#https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json
csvfile = open('output.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("sentiment","tweets","sentiment_score")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
    
es = Elasticsearch()

with open('file.json') as f:
    for line in f:
        data = json.loads(line)
        print(data)
        if 'text' in data:  
            actions = [
              {
                "_index": "tweets",
                "_type": "tweet",
                "_source": {
                    "any":str(data['text']),
                    "timestamp": datetime.now()}
              }
            ]
                
            helpers.bulk(es, actions)
