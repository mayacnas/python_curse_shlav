from facebook_scraper import get_posts
from json import dumps, loads
from pymongo import MongoClient

def last_post_facebook(username):
    """
    Gets the last post on facebook with the specified user
    """
    for post in get_posts(username, pages=1):
        post = dumps(post, indent=4, sort_keys=True, default=str)
        post = loads(post)
        return dumps(post, indent=4)

def write_to_db(json_info):
    """
    Write the json info to the mongodb
    """
    client = MongoClient(r"mongodb://localhost:27017/")
    db = client["fb_db"]
    col = db["fb"]
    x = col.insert_one(loads(json_info))


def main():
   write_to_db(last_post_facebook('adultswim'))

if __name__ == '__main__':
    main()
