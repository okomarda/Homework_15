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

file_json_listedin = 'movie_listedin.json'

with sqlite3.connect("netflix.db") as connection:
    cur = connection.cursor()
    sqlite_query_2 = """
            SELECT title, listed_in, description, release_year
            FROM netflix
            WHERE title != '' AND description != '' AND listed_in  != '' AND release_year != ''
            ORDER BY release_year DESC
            """

def make_list_listedin():
    cur.execute (sqlite_query_2)
    result = cur.fetchall()
    movie_list_3 = []

    for row in result:
        r = list(row)
        x = {}
        x['title'] = r[0]
        x['listed_in'] = r[1]
        x['release_yaer'] = r[3]
        x['description'] = r[2]
        movie_list_3.append(x)

    return movie_list_3

movie_list_3 = make_list_listedin()
with open (file_json_listedin, 'w') as outfile :
    json.dump (movie_list_3, outfile)

#print(make_list_listedin())
#print(len(make_list_listedin()))

def load_movies_listedin(file_json_listedin) :
    '''Передача данных файла json в список'''
    with open (file_json_listedin, 'r', encoding='utf-8') as file :
        movie_list_3 = json.load (file)
    for movie in movie_list_3:
        movie_list_3
    return movie_list_3
#print(load_movies_rating(file_json_listedin))
#print(len(load_movies_rating(file_json_listedin)))

def select_movie_listedin(keyword):
    movie_list_listedin = []
    movie_list_3 = load_movies_listedin(file_json_listedin)
    for movie in movie_list_3:
        if keyword.lower() in movie['listed_in'].lower():
            movie_list_listedin.append(movie)
        elif len(movie_list_listedin) > 9:
            break
    return movie_list_listedin
#print(select_movie_listedin('action'))
#print(len(select_movie_listedin('action')))

