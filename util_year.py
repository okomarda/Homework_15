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

file_json_year = 'movie_year.json'

#ЗАДАНИЕ № 2
with sqlite3.connect("netflix.db") as connection:
    cur = connection.cursor()
    sqlite_query_1 = """
            SELECT title, release_year
            FROM netflix
            WHERE title != '' AND description != '' AND release_year != ''
            ORDER BY title
            LIMIT 100
            """

def make_list_year():
    cur.execute (sqlite_query_1)
    result = cur.fetchall()
    movie_list_1 = []

    for row in result:
        r = list(row)
        x = {}
        x["title"] = r[0]
        x["release_year"] = r[1]
        movie_list_1.append(x)

    return movie_list_1

movie_list_1 = make_list_year()
with open (file_json_year, 'w') as outfile :
    json.dump (movie_list_1, outfile)

#print(make_list_year())
#print(len(make_list_year()))

def load_movies_year(file_json_year) :
    '''Передача данных файла json в список'''
    with open (file_json_year, 'r', encoding='utf-8') as file :
        movie_list_1 = json.load (file)
    for movie in movie_list_1:
        movie_list_1
    return movie_list_1
#print(load_movies_year(file_json_year))
#print(len(load_movies_year(file_json_year)))

def select_movie_year():
    movie_list_year = []
    movie_list_1 = load_movies_year(file_json_year)
    for movie in movie_list_1:
        if 2020 <= movie['release_year'] <= 2022:
            movie_list_year.append(movie)
    return movie_list_year
#print(select_movie_year())
#print(len(select_movie_year()))
