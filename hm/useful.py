import sqlite3


# Rose McIver
# Ben Lamb

# Jack Black
# Dustin Hoffman

def two_actors(name_one, name_two):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(
        f"SELECT DISTINCT netflix.cast FROM netflix WHERE netflix.cast LIKE '%{name_one}%'")
    result = cursor.fetchall()
    list = []
    for i in range(0, len(result)):
        list += result[i]

    words = ("")
    for i in range(0, len(list)):
        words += list[i] + ", "
    words = words[0:len(words) - 2]
    words = words.split(", ")
    counter = 0
    for i in range(0, len(words)):
        if words[i] == f"{name_two}":
            counter += 1
    if counter > 2:
        print(f"{name_two} снимался с {name_one} в одном фильме больше двух раз.")
    else:
        print(f"Число совместных работ меньше двух.")


two_actors(name_one=input(), name_two=input())


def find_movie_or_TVshow(type, release_year, listed_in):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
    cursor.execute(
        f"SELECT title, description FROM netflix WHERE type = '{type}' AND release_year = {release_year} AND listed_in LIKE '%{listed_in}%'")
    result = cursor.fetchall()
    print(result)


find_movie_or_TVshow(type=input().title(), release_year=int(input()), listed_in=input().lower())
