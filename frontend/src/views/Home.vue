<template>
	<div class='container'>
		<Navbar />
		<div class='main_page'>
			<form @submit.prevent="null">
				<Input class='search_field' placeholder='Search' type='text' @input-finished='update_query' />
				<Button class="search_btn" @callback="search"><font-awesome-icon icon='fa-solid fa-search' /></Button>
			</form>
			<div class='result_field'>
				<div class='result_found' v-if='result_found'>
					<div class="movie_container">
						<h2>Movies</h2>
						<ul>
							<li v-for="movie in movies">
								<MediaCard :media="movie" />
							</li>
						</ul>
					</div>
					<div class="tvshow_container">
						<h2>TV Shows</h2>
						<ul>
							<li v-for="tvshow in tv_shows">
								<MediaCard :media="tvshow" />
							</li>
						</ul>
					</div>
				</div>
				<h2 v-else-if="none_results_found">No result found.</h2>
				<Loading v-else-if="show_loading" />
				<h2 v-else>Search Movies/TV Shows/Animes and other</h2>
			</div>
		</div>
	</div>
</template>
<script lang="ts">
import Loading from '@/components/Loading.vue';
import environment from '../interfaces/environment.class';
import Input from '../components/Input.vue';
import Navbar from '../components/Navbar.vue';
import MediaType from '../interfaces/media_type.enum';
import type Media from '../interfaces/media.interface';
import MediaCard from '../components/MediaCard.vue';
import Button from '@/components/Button.vue';
import UserService from '@/services/user.service';

export default {
	components: {
		Input,
		Navbar,
		MediaCard,
		Button,
		Loading,
	},

	data() {
		return {
			result_found: false as boolean,
			movies: [] as Media[],
			tv_shows: [] as Media[],
			query: '' as string,
			none_results_found: false as boolean,
			show_loading: false as boolean,
			base_poster_path: 'https://image.tmdb.org/t/p/original' as string,
		};
	},

	methods: {
		update_query(value: string): void {
			if (!value) {
				this.result_found = false;
				this.movies = [];
				this.tv_shows = [];
			}
			this.query = value;
		},

		async search(): Promise<void> {
			this.show_loading = true;
			this.result_found = false;
			this.none_results_found = false;
			this.movies = [];
			this.tv_shows = [];
			if (!this.query)
				return;
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/search?query=${this.query}`, {
				method: 'get',
				headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` },
			});
			if (!response.ok) {
				console.log(await response.text());
				this.$router.push('/login');
				return;
			}
			const response_json = await response.json();
			if (response_json['total_results'] === 0) {
				this.none_results_found = true;
				return ;
			}
			for (let item of response_json['results']) {
				let poster_path: string = '';
				let poster_found: boolean = true;
				let requested: boolean = (await (await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/request/is_in_db?tmdb_id=${item['id']}`, {
					method: 'get',
				})).json())['data'];

				if ('poster_path' in item && item['poster_path'])
					poster_path = this.base_poster_path + item['poster_path'];
				else {
					poster_path = 'https://artworks.thetvdb.com/banners/images/missing/movie.jpg';
					poster_found = false;
				}
				if (item['media_type'] == 'movie') {
					this.movies.push({
						title: item['title'],
						type: MediaType.MOVIE,
						nb_seasons: 0,
						tmdb_id: item['id'],
						poster: poster_path,
						poster_found: poster_found,
						requested: requested,
					});
				}
				else if (item['media_type'] == 'tv') {
					const resp_nb_seasons = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/get_tv_details?id=${item['id']}`, {
						method: 'get',
						headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` }
					});
					if (!resp_nb_seasons.ok)
						return;
					const nb_seasons = await resp_nb_seasons.json();
					this.tv_shows.push({
						title: item['name'],
						type: MediaType.TVSHOW,
						tmdb_id: item['id'],
						nb_seasons: nb_seasons['number_of_seasons'],
						poster: poster_path,
						poster_found: poster_found,
						requested: requested,
					});
				}
			}
			this.show_loading = false;
			this.result_found = true;
		},
	}
};
</script>
<style scoped>
ul {
	display: flex;
	flex-direction: row;
	overflow-x: scroll;
	-ms-overflow-style: none;
	scrollbar-width: none;
}

ul::-webkit-scrollbar {
	display: none;
}

form {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}

form Input {
	width: 100%;
	margin-right: 15px;
}

form Button {
	width: 50px;
	height: 50px;
	border-radius: 50%;
	font-size: 1.3em;
}

.result_field {
	display: flex;
	height: 100%;
	padding-top: 15px;
	padding-bottom: 15px;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}

.result_found {
	height: 100%;
	width: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.movie_container, .tvshow_container {
	height: 50%;
}
</style>
