<template>
	<div class='card_container'
		:style="{'background-image': `url(${media.poster})`}">
		<img :src="media.poster" />
		<Button class="request_btn" @callback='request'>Request</Button>
	</div>
</template>
<script lang='ts'>
import type Media from '@/interfaces/media.interface';
import Button from '../components/Button.vue';
import MediaType from '../interfaces/media_type.enum';

export default {
	components: {
		Button,
	},

	props: {
		media: { type: Object as () => Media, required: true },
	},

	data() {
		return {
			type: '' as string,
		};
	},

	async mounted(): Promise<void> {
		if (this.media.type == MediaType.MOVIE)
			this.type = 'Movie';
		else if (this.media.type == MediaType.TVSHOW)
			this.type = 'TV Show';
	},

	methods: {
		async request(): Promise<void> { console.log('bonsoir'); }
	},
};
</script>
<style scoped>
.card_container {
	display: flex;
	justify-content: center;
	position: relative;
	border: 2px solid rgba(246,249,249, 0.5) ;
	border-radius: 20px;
	background: no-repeat center;
	background-size: cover;
	margin-top: 15px;
	margin-right: 30px;
}

.card_container:hover .request_btn { display: block; }

img {
	width: 300px;
	height: auto;
	opacity: 0;
}

.request_btn {
	position: absolute;
	bottom: 15px;
	display: none;
}
</style>