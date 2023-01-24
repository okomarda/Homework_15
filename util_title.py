# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------

import sqlite3
import json

with sqlite3.connect("netflix.db") as connection:
    cur = connection.cursor()
    sqlite_query = """
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title != '' AND description != '' AND release_year != '' AND country != ''
            ORDER BY release_year DESC
            LIMIT 110
            """
file_json = 'movie.json'
file_json_year = 'movie_year.json'

#ЗАДАНИЕ № 1
def make_list():
    cur.execute (sqlite_query)
    result = cur.fetchall()
    movie_list = []

    for row in result:
        r = list(row)
        x = {}
        x["title"] = r[0]
        x["country"] = r[1]
        x["release_year"] = r[2]
        x["listed_in"] = r[3]
        x["description"] = r[4]
        movie_list.append(x)

    return movie_list
#print(make_list())

movie_list = make_list()
with open ('movie.json', 'w') as outfile :
    json.dump (movie_list, outfile)

def load_movies(file_json) :
    '''Передача данных файла json в список'''
    with open (file_json, 'r', encoding='utf-8') as file :
        movie_list = json.load (file)
    for movie in movie_list:
        movie_list
    return movie_list
#print(load_movies('movie.json'))
#print(len(load_movies(file_json)))

def get_movie_by_title(title):
    '''Поиск фильмов по выбранному названию'''
    movie_list = load_movies(file_json)
    for movie in movie_list:
        if title.lower() in movie['title'].lower ( ):
            return movie

#print(get_movie_by_title("cinema"))

