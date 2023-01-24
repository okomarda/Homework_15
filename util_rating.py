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

file_json_rating = 'movie_rating.json'

#ЗАДАНИЕ № 2
with sqlite3.connect("netflix.db") as connection:
    cur = connection.cursor()
    sqlite_query_2 = """
            SELECT title, rating, description
            FROM netflix
            WHERE title != '' AND description != '' AND rating != ''
            GROUP BY title, rating
            HAVING rating = 'G' OR rating = 'PG' OR rating = 'PG-13' OR rating = 'R' OR rating = 'NC-17'
            ORDER BY title
            """

def make_list_rating():
    cur.execute (sqlite_query_2)
    result = cur.fetchall()
    movie_list_2 = []

    for row in result:
        r = list(row)
        x = {}
        x["title"] = r[0]
        x["rating"] = r[1]
        x['description'] = r[2]
        movie_list_2.append(x)

    return movie_list_2

movie_list_2 = make_list_rating()
with open (file_json_rating, 'w') as outfile :
    json.dump (movie_list_2, outfile)

#print(make_list_rating())
#print(len(make_list_rating()))

def load_movies_rating(file_json_rating) :
    '''Передача данных файла json в список'''
    with open (file_json_rating, 'r', encoding='utf-8') as file :
        movie_list_2 = json.load (file)
    for movie in movie_list_2:
        movie_list_2
    return movie_list_2
#print(load_movies_rating(file_json_rating))
#print(len(load_movies_rating(file_json_rating)))

def select_movie_rating_children():
    movie_list_rating = []
    movie_list_2 = load_movies_rating(file_json_rating)
    for movie in movie_list_2:
        if movie['rating'] == 'G':
            movie_list_rating.append(movie)
    return movie_list_rating
#print(select_movie_rating_children())
#print(len(select_movie_rating_children()))

def select_movie_rating_family():
    movie_list_rating = []
    movie_list_2 = load_movies_rating(file_json_rating)
    for movie in movie_list_2:
        if movie['rating'] in ['PG', 'PG-13', 'G']:
            movie_list_rating.append(movie)
    return movie_list_rating
#print(select_movie_rating_family())
#print(len(select_movie_rating_family()))

def select_movie_rating_adult():
    movie_list_rating = []
    movie_list_2 = load_movies_rating(file_json_rating)
    for movie in movie_list_2:
        if movie['rating'] in ['R', 'NC-17']:
            movie_list_rating.append(movie)
    return movie_list_rating
#print(select_movie_rating_family())
#print(len(select_movie_rating_family()))

