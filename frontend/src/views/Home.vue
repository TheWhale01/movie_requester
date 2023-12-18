<template>
	<div class='page_container'>
		<div class='navbar'>
			<h1>Movie Requester</h1>
			<div class='navbar_footer'>
				<p>Future Button (Requests)</p>
				<p>Future Button (Settings)</p>
			</div>
		</div>
		<div class='main_page'>
			<Input class='search_field' placeholder='Search' type='text' @input-finished='search'/>
			<div class='result_field'>
				<p v-if='result_found'>I found some results</p>
				<h2 v-else>Search Movies/TV Shows/Animes and other</h2>
			</div>
		</div>
	</div>
</template>
<script lang="ts">
import environment from '../interfaces/environment.class'
import Input from '../components/Input.vue';

export default {
	components: {
		Input,
	},

	data() {
		return {
			result_found: false as boolean,
		};
	},

	async mounted(): Promise<void> {
		const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/login`, {
			method: 'get',
			headers: {'authorization': `bearer ${sessionStorage.getItem('access_token')}`}
		});
		if (!response.ok)
			this.$router.push('/login');
	},
	
	methods: {
		search(value: string): void {
			this.result_found = false;
			console.log(value);
			this.result_found = true;
			if (!value)
				this.result_found = false;
		},
	}
};
</script>
<style scoped>
h1 {
	padding-top: 15px;
}

.page_container {
	display: flex;
	height: 100vh;
	width: 100%;
}

.navbar {
	padding-left: 20px;
	display: flex;
	width: 15%;
	height: 100%;
	flex-direction: column;
	justify-content: space-between;
	background-color: #121a2a;
}

.navbar_footer {
	padding-bottom: 20px;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	width: 100%;
	height: 30%;
}

.main_page {
	display: flex;
	flex-direction: column;
	width: 85%;	
	padding-top: 15px;
	padding-left: 15px;
	padding-right: 15px;	
}

.result_field {
	display: flex;
	height: 100%;
	flex-direction: column;
	justify-content: center;
	align-items: center;	
}
</style>
