from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
import os

print("Current Working Directory:", os.getcwd())

app = Flask(__name__)
CORS(app)
# Loading data
movies_db = pd.read_csv("ml-32m/movies.csv")
rating_db = pd.read_csv("ml-32m/ratings.csv")

@app.route('/api/movies/top10', methods=['GET'])
def get_top_movies():
    #group data by id and then sort it by rating to get top 10
    movieID = rating_db.groupby("movieId")
    top10 = movieID['rating'].count().sort_values(ascending=False).head(10)
    
    # empty list of top movies made
    top_movies = []

    #iterate in the too10 wali list
    for monkey in top10.index:
        movie_info = movies_db[movies_db['movieId'] == monkey].to_dict(orient='records') #converted to dictionary 
        if movie_info:
            top_movies.append(movie_info[0])  #append the dict, (it is reset everytime to another movie in each iteration)

    return jsonify(top_movies)

if __name__ == '__main__':
    app.run(debug=True)
