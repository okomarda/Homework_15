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
from itertools import count

with sqlite3.connect("netflix.db") as connection:
    cur = connection.cursor()
    sqlite_query_2 = """
            SELECT title, netflix.cast, description
            FROM netflix
            WHERE netflix.cast LIKE '%Jack Black%' OR netflix.cast LIKE '%Dustin Hoffman%'
            """

def make_list_cast():
    cur.execute(sqlite_query_2)
    result = cur.fetchall()
    movie_list_4 = []

    for row in result:
        r = list(row)
        x = {}
        x['cast'] = r[1]
        movie_list_4.append(x)
    return movie_list_4

def select_movie_cast():
    movie_list_cast = []
    movie_list_4 = make_list_cast()
    for movie in movie_list_4:
        movie_list_cast.append(movie['cast'])
        movie_list_cast_1 = ", ".join(movie_list_cast)
        cast_list = movie_list_cast_1.split(", ")
        double_list = {"Jack Black", "Dustin Hoffman"}
        for actor in cast_list:
            if cast_list.count(actor) > 2:
                double_list.add(actor)
                double_list.discard("Jack Black")
                double_list.discard ("Dustin Hoffman")
                double_list_final = list(double_list)

    return double_list_final

#print(select_movie_cast())
#print(len(select_movie_cast()))


