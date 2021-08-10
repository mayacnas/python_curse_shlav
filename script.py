from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
mydatabase = client['facebook']
mycollection = mydatabase['posts']
post={
'user': 'user',
'content': 'hello',
'date': ,
'likes': 104,
'comments': 103,
'shares': 102
}
mydatabase.mycollection.insert(post)
