import sqlite3
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main_page():
    return "Халк крушить!"


@app.route("/<movie_title>")
def title_page(movie_title):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(
        f"SELECT title, country, MIN(release_year), listed_in, description FROM netflix WHERE title = '{movie_title}'")
    result = cursor.fetchall()

    title = result[0][0]
    country = result[0][1]
    release_year = result[0][2]
    genre = result[0][3]
    description = result[0][4]

    words = "<br>"
    words += "Название:" + " " + title + "<br>"
    words += "Страна:" + " " + country + "<br>"
    words += "Год производства:" + " " + str(release_year) + "<br>"
    words += "Жанр:" + " " + genre + "<br>"
    words += "Описание:" + " " + description + "<br>"

    return words


@app.route("/movie/<int:year_1>/to/<int:year_2>")
def year_to_year_page(year_1, year_2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(
        f"SELECT title, release_year FROM netflix WHERE release_year BETWEEN {year_1} AND {year_2} ORDER BY release_year LIMIT 100")
    result = cursor.fetchall()
    max = len(result)
    words = "<br>"
    for i in range(0, max):
        words += "Название:" + " " + result[i][0] + "<br>"
        words += "Год производства:" + " " + str(result[i][1]) + "<br>"
        words += "<br>"

    return words


@app.route("/rating/children")
def children_page():  # (включаем сюда рейтинг G)
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(
        f"SELECT title, rating FROM netflix WHERE rating = 'G' LIMIT 100")
    result = cursor.fetchall()
    max = len(result)
    words = "<br>"
    for i in range(0, max):
        words += "Название:" + " " + result[i][0] + "<br>"
        words += "Возрастной рейтинг:" + " " + str(result[i][1]) + "<br>"
        words += "<br>"

    return words


@app.route("/rating/family")
def family_page():  # (G, PG, PG-13)
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(
        f"SELECT title, rating FROM netflix WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13' LIMIT 100")
    result = cursor.fetchall()
    max = len(result)
    words = "<br>"
    for i in range(0, max):
        words += "Название:" + " " + result[i][0] + "<br>"
        words += "Возрастной рейтинг:" + " " + str(result[i][1]) + "<br>"
        words += "<br>"

    return words


@app.route("/rating/adult")
def adult_page():  # (R, NC-17)
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(f"SELECT title, rating FROM netflix WHERE rating = 'R' OR rating = 'NC-17' LIMIT 100")
    result = cursor.fetchall()
    max = len(result)
    words = "<br>"
    for i in range(0, max):
        words += "Название:" + " " + result[i][0] + "<br>"
        words += "Возрастной рейтинг:" + " " + str(result[i][1]) + "<br>"
        words += "<br>"
    return words


@app.route("/genre/<genre>")
def description_page(genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(
        f"SELECT title, description, date_added FROM netflix WHERE listed_in LIKE '%{genre}%' ORDER BY date_added DESC LIMIT 10")
    result = cursor.fetchall()
    max = len(result)
    words = "<br>"
    for i in range(0, max):
        words += "Название:" + " " + result[i][0] + "<br>"
        words += "Краткое описание:" + " " + str(result[i][1]) + "<br>"
        words += "<br>"
    return words


app.run()
