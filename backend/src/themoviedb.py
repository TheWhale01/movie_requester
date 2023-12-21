from include import *


class TheMovieDB:
	def __init__(self):
		self.__token = environ['THE_MOVIE_DB_KEY']
		self.__global_endpoint = 'https://api.themoviedb.org/3'
		self.__search_endpoint = path.join(self.__global_endpoint, 'search/multi')
		self.__auth_header = {'Authorization': f'Bearer {self.__token}'}
		self.__accept_header = {'accept': 'application/json'}

	def __get_response_from_url(self, url):
		headers = self.__auth_header | self.__accept_header
		response = requests.get(url, headers=headers)
		if not response.ok:
			raise HTTPException(status_code=response.status_code, detail=response.text)
		return response.json()

	def search(self, query, language: str = 'fr-FR', include_adult: bool = False, page=1):
		url = self.__search_endpoint + \
			f'?query={query}&include_adult={include_adult}&language={language}&page={page}'
		return self.__get_response_from_url(url)

	def get_tv_details(self, id: int, language: str = 'fr-FR'):
		url = self.__global_endpoint + f'/tv/{id}?language={language}'
		return self.__get_response_from_url(url)
