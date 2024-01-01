<template>
	<div class="container">
		<Navbar />
		<div class="main_page">
			<ul v-if='requests.length'>
				<li v-for="request in requests">
					<RequestCard :request="request" @removeRequest="getRequests()" />
				</li>
			</ul>
			<div class='no_requests' v-else>
				<h2>No requests found.</h2>
			</div>
		</div>
	</div>
</template>
<script lang="ts">

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

	async mounted(): Promise<void> {
		this.check_token();
		this.user = UserService.getUser;
		await this.getRequests();
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
			if (!response.ok)
				this.$router.push('/login');
		},

		async getRequests(): Promise<void> {
			this.requests = [];
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/request`, {
				method: 'get',
				headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` },
			});
			if (!response.ok) {
				this.show_no_requests = true;
				return;
			}
			const response_json = await response.json();
			if (response_json['total_results'] == 0) {
				this.show_no_requests = true;
				return;
			}
			for (let request of response_json['data'])
				this.requests.push(request);
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

.no_requests {
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}
</style>