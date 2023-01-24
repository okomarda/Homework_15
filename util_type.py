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

file_json_type = 'movie_type.json'

with sqlite3.connect("netflix.db") as connection:
    cur = connection.cursor()
    sqlite_query_2 = """
            SELECT title, type, listed_in, description, release_year
            FROM netflix
            WHERE title != '' AND description != '' AND listed_in  != '' AND release_year != ''
            ORDER BY release_year DESC
            """

def make_list_type():
    cur.execute (sqlite_query_2)
    result = cur.fetchall()
    movie_list_5 = []

    for row in result:
        r = list(row)
        x = {}
        x['title'] = r[0]
        x['type'] = r[1]
        x['listed_in'] = r[2]
        x['release_year'] = r[4]
        x['description'] = r[3]
        movie_list_5.append(x)

    return movie_list_5

movie_list_5 = make_list_type()
with open (file_json_type, 'w') as outfile :
    json.dump (movie_list_5, outfile)

#print(make_list_type())
#print(len(make_list_type()))

def load_movies_type(file_json_type) :
    '''Передача данных файла json в список'''
    with open (file_json_type, 'r', encoding='utf-8') as file :
        movie_list_5 = json.load (file)
    for movie in movie_list_5:
        movie_list_5
    return movie_list_5
#print(load_movies_type(file_json_type))
#print(len(load_movies_type(file_json_type)))

def select_movie_type():
    print("Введите тип фильма")
    type = input()
    print ("Введите год выпуска фильма")
    year = int(input())
    print ("Введите жанр фильма")
    genre = input()
    movie_list_type = []
    movie_list_5 = load_movies_type(file_json_type)
    for movie in movie_list_5:
        if type.lower() in movie['type'].lower() and year == movie['release_year'] and genre.lower() in movie['listed_in'].lower():
            movie_list_type.append(movie)

    return movie_list_type
#print(select_movie_type())
#print(len(select_movie_type()))

