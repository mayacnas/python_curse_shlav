from pymongo import MongoClient
import json
import os
from facebook_scraper import get_posts
client = MongoClient('mongodb://localhost:27017/')
mydatabase = client['facebook']
mycollection = mydatabase['posts']
page=input("hey please enter the page you want to take posts from: ")
for post in get_posts(page, pages=1):
    facebook_post={
    'username': post['username'],
    'text': post['text'],
    'date': str(post['time']),
    'likes': post['likes'],
    'comments': post['comments'],
    'shares': post['shares']
    }
    json_object = json.dumps(facebook_post, indent = 4)
    jsonFile = open("data.json", "w")
    jsonFile.write(json_object)
    jsonFile.close()
    with open('data.json') as f:
        data = json.load(f)
    x = mycollection.insert_one(data)
os.remove("data.json")
