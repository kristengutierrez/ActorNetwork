import omdb
from omdb import Client
from pymongo import MongoClient

client = Client(apikey="*******")
omdb.set_default('apikey', '*******')

client = MongoClient()
db = client.primer
coll = db.dataset
omdb.get(title='Inception')
result = db.movie.insert_one({'actors': 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy', 'awards': 'Won 4 Oscars. Another 152 wins & 204 nominations.', 'box_office': '$292,568,851', 'country': 'USA, UK', 'dvd': '07 Dec 2010', 'director': 'Christopher Nolan', 'genre': 'Action, Adventure, Sci-Fi', 'language': 'English, Japanese, French', 'metascore': '74', 'plot': 'A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.', 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg', 'production': 'Warner Bros. Pictures', 'rated': 'PG-13', 'released': '16 Jul 2010', 'response': 'True', 'runtime': '148 min', 'title': 'Inception', 'type': 'movie', 'website': 'http://inceptionmovie.warnerbros.com/', 'writer': 'Christopher Nolan', 'year': '2010', 'imdb_id': 'tt1375666', 'imdb_rating': '8.8', 'imdb_votes': '1,626,815'})
db = client.test
db.movie.insert_one(omdb.get(title='Harry Potter and the Prisoner of Azkaban'))
cursor = db.movie.aggregate(
    [
        {"$group": {"_id": "$title"}}
    ]
)
for document in cursor:
    print(document)
