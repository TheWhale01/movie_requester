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
				<h2 class="base_view" v-else-if="none_results_found">No result found.</h2>
				<Loading v-else-if="show_loading" />
				<h2 class="base_view" v-else>Search Movies/TV Shows/Animes and other</h2>
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
			if (!this.query) {
				this.show_loading = false;
				return;
			}
			const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/search?query=${this.query}`, {
				method: 'get',
				headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` },
			});
			if (!response.ok) {
				this.$router.push('/login');
				return;
			}
			const response_json = await response.json();
			if (response_json['total_results'] === 0) {
				this.none_results_found = true;
				this.show_loading = false;
				return ;
			}
			for (let item of response_json['results']) {
				switch (item['type']) {
					case MediaType.MOVIE:
						this.movies.push(item);
						break ;
					case MediaType.TVSHOW:
						this.tv_shows.push(item);
						break;
					default:
						break;
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
	
}

form {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	margin-right: 15px;
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

.base_view {
	text-align: center;
	position: absolute;
	top: 50%;
	left: 50%;
}

.result_field {
	height: 100%;
}

.result_found {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
}
</style>
