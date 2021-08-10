from facebook_scraper import get_posts
from pymongo import MongoClient

username=input("hey please enter the username \n")

for post in get_posts(username, pages=10):
    print(post)
    client = MongoClient('mongodb://localhost:27017/')
    mydatabase = client['facebook']
    mycollection = mydatabase['posts']
    post = {
               'user': username,
               'content': post['text'],
    }
    mydatabase.mycollection.insert(post)










