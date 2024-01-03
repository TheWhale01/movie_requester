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
