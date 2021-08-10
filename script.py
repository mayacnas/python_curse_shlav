from pymongo import MongoClient
import json
import os
from facebook_scraper import get_posts

def facebook_post(client):
    """
    this function takes a facebook post from a page requested by the user
    and turns it into json
    """
    page=input("please enter the page you want to take a post from: ")
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
        return json_object

def write_to_db(mycollection, json_object):
    """
    this function writes a json object into a mongodb database
    """
    jsonFile = open("data.json", "w")
    jsonFile.write(json_object)
    jsonFile.close()
    with open('data.json') as f:
        data = json.load(f)
    x = mycollection.insert_one(data)
    os.remove("data.json")

def main():
    client = MongoClient('mongodb://localhost:27017/')
    app_name = input('do you want facebook or instagram? ')
    if app_name == 'facebook':
        mydatabase = client['facebook']
        mycollection = mydatabase['posts']
        json_object = facebook_post(client)
    write_to_db(mycollection, json_object)    

if __name__ == '__main__':
    main()
