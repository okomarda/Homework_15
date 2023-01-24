from flask import Flask, request, render_template, jsonify

from util_title import make_list, load_movies, get_movie_by_title
from util_year import select_movie_year
from util_rating import select_movie_rating_children, select_movie_rating_family, select_movie_rating_adult
from util_genre import select_movie_listedin
from util_cast import select_movie_cast
from util_type import select_movie_type

file_json = 'movie.json'

app = Flask(__name__)

@app.route('/')
def make_list_movies():
    '''Загрузка главной страницы со списком фильмов'''
    movie_list = load_movies(file_json)
    len_list = len(movie_list)
    try:
        return render_template('list.html', movie_list=movie_list, len_list=len_list)
    except:
        return "Имеется ошибка в файле html"

@app.route('/movie/<title>')
def get_json_by_title(title):
    '''Выгрузка страницы с фильмом по названию в формате json'''
    movie_list = load_movies(file_json)
    movie = get_movie_by_title(title)
    return jsonify (movie)

@app.route('/movie/year/to/year')
def select_year_to_year():
    '''Выгрузка страницы с фильмами с определенным временным диапазоном в формате json'''
    movie_list_year = select_movie_year()
    return jsonify (movie_list_year)

@app.route('/rating/children')
def select_rating_children():
    '''Выгрузка страницы с фильмами с определенным рейтингом в формате json'''
    movie_list_rating = select_movie_rating_children()
    return jsonify(movie_list_rating)

@app.route('/rating/family')
def select_rating_family():
    '''Выгрузка страницы с фильмами с определенным рейтингом в формате json'''
    movie_list_rating = select_movie_rating_family()
    return jsonify(movie_list_rating)

@app.route('/rating/adult')
def select_rating_adult():
    '''Выгрузка страницы с фильмами с определенным рейтингом в формате json'''
    movie_list_rating = select_movie_rating_adult()
    return jsonify(movie_list_rating)

@app.route('/genre/<genre>')
def select_movie_by_listedin(genre):
    '''Выгрузка страницы с 10 самыми свежими фильмами с определенным жанром в формате json'''
    movie_list_listedin = select_movie_listedin(genre)
    return jsonify(movie_list_listedin)


#Выгрузка списка актеров, игравших более 2 раз с Джеком Блэком или Дастином Хоффманом в формате json
movie_list_cast = select_movie_cast()
#print(movie_list_cast)

#Выгрузка фильмов по заданным параметрам
movie_list_type = select_movie_type()
print(movie_list_type)



app.run (debug=True)