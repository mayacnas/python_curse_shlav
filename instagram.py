from instascrape import *

get_instagram_info(username):
  # Get username
  username = input('Enter username to scrape: ')

  # Instantiate the scraper objects 
  google = Profile(rf'https://www.instagram.com/{username}/')
  # google_post = Post('https://www.instagram.com/p/CG0UU3ylXnv/')
  google_hashtag = Hashtag('https://www.instagram.com/explore/tags/{username}/')

  # Scrape their respective data 
  google.scrape()
  google_post.scrape()
  google_hashtag.scrape()

  print(google.followers)
  # print(google_post['hashtags'])
  print(google_hashtag.amount_of_posts)

def main():
  

if __name__ == '__main__':
  main()
