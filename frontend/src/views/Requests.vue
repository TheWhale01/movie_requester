<template>
	<div class="container">
		<Navbar />
		<div class="main_page">
			<ul>
				<li v-for="request in requests">
					<RequestCard :request="request" />
				</li>
			</ul>
		</div>
	</div>
</template>
<script lang="ts">
// For earch request check the state
// if request is PENDING show buttons to accept or deny

import Navbar from '@/components/Navbar.vue';
import environment from '@/interfaces/environment.class';
import RequestCard from '@/components/RequestCard.vue';
import type Request from '@/interfaces/request.interface';
import UserService from '@/services/user.service';
import type User from '@/interfaces/user.interface';

export default {
	components: {
		Navbar,
		RequestCard,
	},

	data() {
		return {
			requests: [] as Request[],
			show_no_requests: false as boolean,
			user: {} as User,
		};
	},

	async beforeMount(): Promise<void> {
		this.check_token();
		this.user = UserService.getUser;
		console.log(this.user);
		const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/request`, {
			method: 'get',
			headers: {'Authorization': `bearer ${sessionStorage.getItem('access_token')}`},
		});
		if (!response.ok) {
			this.show_no_requests = true;
			return ;
		}
		const response_json = await response.json();
		if (response_json['total_results'] == 0) {
			this.show_no_requests = true;
			return ;
		}
		for (let request of response_json['data'])
			this.requests.push(request);
	},

	methods: {
		async check_token(): Promise<void> {
			const token = sessionStorage.getItem('access_token');
			if (!token) {
				this.$router.push('/login');
				return;
			}
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/login`, {
				method: 'get',
				headers: { 'Authorization': `bearer ${token}` }
			});
			if (!response.ok) {
				this.$router.push('/login');
				return;
			}
		},
	}
};
</script>
<style scoped>
.main_page ul {
	overflow-y: scroll;
	max-height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}
</style>