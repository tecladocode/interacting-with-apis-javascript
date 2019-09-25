from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
movies = []

@app.route('/', methods=["POST"])
def add_movie():
    global movies
    title = request.form.get("title") or request.get_json()["title"]
    year = request.form.get("year") or request.get_json()["year"]
    movies.append({"title": title, "year": year})
    return jsonify({"message": "Movie added"}), 201


@app.route('/movies')
def get_movies():
    return jsonify({"movies": movies})
