from pprint import pprint
import random
from django.shortcuts import render
from imdb import IMDb


# Create your views here.


class ImdbApi():

    def __init__(self):
        self.ia = IMDb()

    def get_top_movies(self):
        return self.ia.get_top250_movies()

    def get_bottom_movies(self):
        return self.ia.get_bottom100_movies()

    def get_movies_id(self, movies):
        return [i.getID() for i in movies]

    def list_of_filtered_movie_information(self, movies_id):
        l = []
        for i in movies_id[:10]:
            di = {}
            film = self.ia.get_movie_main(i)
            di['rating'] = [i[1] for i in film['data'].items() if i[0] == 'rating']
            di['year'] = [i[1] for i in film['data'].items() if i[0] == 'year']
            di['name'] = [i[1] for i in film['data'].items() if i[0] == 'title']
            di['director'] = [i[1] for i in film['data'].items() if i[0] == 'director'][0][0]
            di['index'] = random.randint(0, 9)
            l.append(di)
        return l


def main_page(request):
    return render(request, 'main_page/index.html')


