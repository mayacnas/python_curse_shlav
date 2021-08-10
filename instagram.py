from instascrape import *
from json import dumps, loads

def get_instagram_info(username):
  """
  Get information about specific username from instagram
  """
  # Instantiate the scraper objects 
  google = Profile(rf'https://www.instagram.com/{username}/')
  # google_post = Post('https://www.instagram.com/p/CG0UU3ylXnv/')
  google_hashtag = Hashtag('https://www.instagram.com/explore/tags/{username}/')

  # Scrape their respective data 
  google.scrape()
  google_post.scrape()
  google_hashtag.scrape()

  # print(google.followers)
  # print(google_post['hashtags'])
  # print(google_hashtag.amount_of_posts)
  
  returened_info = {}
  returened_info['username'] = username
  returened_info['amount_of_posts'] = google_hashtag.amount_of_posts
  returened_info['followers'] = google.followers
  
  return dumps(returened_info, indent=4)

def main():
  # Get username
  username = input('Enter username to scrape: ')
  
  # Scrape info
  json_info = get_instagram_info(username)
  print(json_info)

if __name__ == '__main__':
  main()
