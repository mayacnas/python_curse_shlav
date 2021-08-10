from pymongo import MongoClient
import json
import os
from facebook_scraper import get_posts
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
    app_name = request.form['app_name']
    page = request.form['page']
    insert(app_name, page)
    return render_template('index.html')

def facebook_post(client, page):
    """
    this function takes a facebook post from a page requested by the user
    and turns it into json
    """
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

def insert(app_name, page):
    client = MongoClient('mongodb://localhost:27017/')
    if app_name == 'facebook':
        mydatabase = client['facebook']
        mycollection = mydatabase['posts']
        json_object = facebook_post(client, page)
    write_to_db(mycollection, json_object)
    return

if __name__ == '__main__':
    app.run(host='0.0.0.0')
