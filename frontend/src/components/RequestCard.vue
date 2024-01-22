<template>
	<div class="card_container">
		<div class='infos'>
			<div class="left">
				<img v-if="!show_loading" :src="media.poster">
				<Loading v-else />
				<span>{{ media.title }}</span>
			</div>
			<div class="middle">
				<span>Status:
					<Status :statusProps="request.status" />
				</span>
				<span>Requested by: {{ user.username }}</span>
				<span>Request from: {{ request.date }}</span>
			</div>
			<div class="right">
				<div v-if="is_admin === 0">
					<Button v-if="request.status == 0" @click="update(1)">Accept</Button>
					<Button v-if="request.status == 0" @click="update(2)">Deny</Button>
					<Button v-else-if="request.status == 1" @click="update(3)">Finish</Button>
					<Button @click="delete_request">Delete</Button>
				</div>
			</div>
		</div>
		<div class='note_container' v-if='is_note'>
			<p><h2>Note: </h2>{{ request.note }}</p>
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
			is_admin: UserService.getUser.privilege as number,
			is_note: false as boolean,
		};
	},

	async mounted(): Promise<void> {
		this.is_note = this.$props.request.note ? true : false;
		this.show_loading = true;
		let type: string = '';
		const user_response = await fetch(`${environment.HTTP_SCHEMA}://${environment.API_ENDPOINT}/user?id=${this.request.user_id}`, {
			method: 'get',
			headers: {'Authorization': `bearer ${sessionStorage.getItem('access_token')}`},
		});
		if (!user_response.ok) {
			console.log(await user_response.text());
			return ;
		}
		this.user = (await user_response.json())['user'];

		switch (this.request.type) {
			case MediaType.MOVIE:
				type = 'movie';
				break;
			case MediaType.TVSHOW:
				type = 'tv';
				break;
			default:
				break;
		}
		const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.API_ENDPOINT}/get_${type}_details?id=${this.request.tmdb_id}`, {
			method: 'get',
			headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` },
		});
		if (!response.ok)
			return;
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
			const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.API_ENDPOINT}/request/update?id=${this.request.id}&status=${status}`, {
				method: 'PATCH',
				headers: {
					'Authorization': `bearer ${sessionStorage.getItem('access_token')}`,
				},
			});
			if (!response.ok) {
				console.log(await response.text());
				return;
			}
			this.request.status = status;
		},

		async delete_request(): Promise<void> {
			const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.API_ENDPOINT}/request/remove?id=${this.request.id}`, {
				method: 'delete',
				headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` },
			});
			if (!response.ok) {
				console.log(await response.text());
				return;
			}
			this.$emit('removeRequest', this.request);
		}
	},
};
</script>
<style scoped>
.card_container {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	align-items: center;
	border-radius: 20px;
	margin-bottom: 15px;
	background-color: #121a2a;
	box-shadow: 0px 1px 5px #121a2a;
}

.infos {
	width: 100%;
	display: flex;
	flex-direction: row;
}

img {
	height: 200px;
	border-radius: 20px;
}

.left,
.middle,
.right {
	display: flex;
	align-items: center;
	width: 33%;
}

.left span {
	padding-left: 15px;
}

.middle,
.right {
	flex-direction: column;
	justify-content: space-evenly;
	height: 200px;
	text-align: center;
}

.right {
	padding-right: 15px;
	align-items: end;
}

.right div {
	display: flex;
	flex-direction: column;
	height: 100%;
	justify-content: space-evenly;
}

.note_container {
	margin-left: 15px;
	padding-top: 15px;
	padding-bottom: 15px;
	width: 100%;
	height: auto;
	height: 50px;
	border-top: 1px solid white;
	overflow-wrap: anywhere;
	height: fit-content;
}

.note_container h2 {
	padding-left: 15px;
	display: inline;
}
</style>
