<template>
	<div class="card_container">
		<div class="left">
			<img v-if="!show_loading" :src="media.poster">
			<Loading v-else/>
			<span>{{ media.title }}</span>
		</div>
		<div class="middle">
			<span>Status: <Status :statusProps="request.status" /></span>
			<span>Requested by: {{ user.username }}</span>
			<span>Request from: {{ request.date }}</span>
		</div>
		<div class="right" v-if="user.privilege == 0">
			<Button v-if="request.status == 0" @click="update(1)">Accept</Button>
			<Button v-if="request.status == 0" @click="update(2)">Deny</Button>
			<Button v-else-if="request.status == 1" @click="update(3)">Finish</Button>
			<Button @click="delete_request">Delete</Button>
		</div>
	</div>
</template>
<script lang="ts">
import Loading from './Loading.vue';
import type Request from '@/interfaces/request.interface';
import type Media from '@/interfaces/media.interface';
import StatusType from '@/interfaces/status_type.enum';
import Status from './Status.vue';
import MediaType from '@/interfaces/media_type.enum';
import environment from '@/interfaces/environment.class';
import Button from './Button.vue';
import UserService from '@/services/user.service';
import type User from '@/interfaces/user.interface';

export default {
	components: {
		Status,
		Button,
		Loading,
	},

	props: {
		request: {
			type: Object as () => Request,
			required: true,
		},
	},

	data() {
		return {
			media: {} as Media,
		    user: {} as User,
			show_loading: false as boolean,
		};
	},

	async mounted(): Promise<void> {
		this.show_loading = true;
		let type: string = '';
		this.user = UserService.getUser

		switch (this.request.type) {
			case MediaType.MOVIE:
				type = 'movie';
				break ;
			case MediaType.TVSHOW:
				type = 'tv';
				break ;
			default:
				break;
		}
		const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/get_${type}_details?id=${this.request.tmdb_id}`, {
			method: 'get',
			headers: {'Authorization': `bearer ${sessionStorage.getItem('access_token')}`},
		});
		if (!response.ok)
			return ;
		const response_json = await response.json();
		this.media.poster = 'https://image.tmdb.org/t/p/original' + response_json['poster_path'];
		this.media.poster_found = true;
		this.show_loading = false;
		this.media.requested = true;
		if (this.request.type == MediaType.TVSHOW)
			this.media.title = response_json['name'];
		else if (this.request.type == MediaType.MOVIE)
			this.media.title = response_json['title'];
		this.media.tmdb_id = this.request.tmdb_id;
		this.media.type = this.request.type;
	},

	methods: {
		async update(status: StatusType): Promise<void> {
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/request/update?id=${this.request.id}&status=${status}`, {
				method: 'PATCH',
				headers: {
					'Authorization': `bearer ${sessionStorage.getItem('access_token')}`,
				},
			});
			if (!response.ok) {
				console.log(await response.text());
				return ;
			}
			this.request.status = status;
		},

		async delete_request(): Promise<void> {
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/request/remove?id=${this.request.id}`, {
				method: 'delete',
				headers: {'Authorization': `bearer ${sessionStorage.getItem('access_token')}`},
			});
			if (!response.ok) {
				console.log(await response.text());
				return ;
			}
			this.$emit('removeRequest', this.request);
		}
	},
};
</script>
<style scoped>
.card_container {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	border-radius: 20px;
	margin-bottom: 20px;
	background-color: #121a2a;
	box-shadow: 0px 1px 5px #121a2a;
}

img {
	height: 200px;
	border-radius: 20px;
}

.left, .middle, .right {
	display: flex;
	align-items: center;
	width: 33%;
}

.left span {
	padding-left: 15px;
}

.middle, .right {
	flex-direction: column;
	justify-content: space-evenly;
	height: 200px;
	text-align: center;
}

.right {
	padding-right: 15px;
	align-items: end;
}

</style>
