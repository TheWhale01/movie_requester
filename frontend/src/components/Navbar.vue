<template>
	<div class='navbar'>
		<button @click="homepage"><h1>Movie Requester</h1></button>
		<div class='navbar_footer'>
			<Button @callback="show_requests">Requests</Button>
			<Button @callback="show_settings">Settings</Button>
		</div>
	</div>
</template>
<script lang="ts">
import type User from '@/interfaces/user.interface';
import Button from './Button.vue';
import environment from '@/interfaces/environment.class';
import UserService from '@/services/user.service';

export default {
	components: {
		Button,
	},

	async beforeMount(): Promise<void> {
		if (UserService.isSet)
			return ;
		const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/login`, {
			method: 'get',
			headers: { 'authorization': `bearer ${sessionStorage.getItem('access_token')}` }
		});
		if (!response.ok)
			this.$router.push('/login');
		const response_json = await response.json();
		console.log(response_json);
		let user: User = {
			id: response_json['user']['id'],
			language: response_json['user']['language'],
			profile_picture: response_json['user']['profile_picture'],
			username: response_json['user']['username'],
			privilege: response_json['user']['privilege'],
		}
		UserService.setUser(user);
	},

	methods: {
		show_requests(): void { this.$router.push('/request'); },
		show_settings(): void { this.$router.push('/settings'); },
		homepage(): void { this.$router.push('/'); },
	}
};
</script>
<style scoped>
h1 {
	margin-top: 30px;
}

.navbar {
	display: flex;
	width: 15%;
	height: 100%;
	flex-direction: column;
	justify-content: space-between;
	align-items: center;
	background-color: #121a2a;
	min-width: 200px;
}

.navbar_footer {
	padding-bottom: 15px;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-around;
	width: 100%;
	height: 30%;
}

.navbar Button {
	width: 75%;
}
</style>
