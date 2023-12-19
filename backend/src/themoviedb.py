from .include import *
import sys

class TheMovieDB:
    def __init__(self, lang='en-GB', include_adult=False):
        self.__token = environ['THE_MOVIE_DB_KEY']
        self.__global_endpoint = 'https://api.themoviedb.org/3'
        self.__search_endpoint = path.join(self.__global_endpoint, 'search/multi')
        self.__auth_header = {'Authorization': f'Bearer {self.__token}'}
        self.__accept_header = {'accept': 'application/json'}
        self.__poster_base_path = 'https://image.tmdb.org/t/p/original/'
        self.lang = lang
        self.include_adult = include_adult

    def search(self, query, page=1):
        url = self.__search_endpoint + f'?query={query}&include_adult={self.include_adult}&language={self.lang}&page={page}'
        headers = self.__auth_header | self.__accept_header
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

    def get_tv_details(self, id: int):
        url = self.__global_endpoint + f'/tv/{id}?language={self.lang}'
        headers = self.__auth_header | self.__accept_header
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()
