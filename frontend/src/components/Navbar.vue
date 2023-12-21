<template>
	<div class='navbar'>
		<h1>Movie Requester</h1>
		<div class='navbar_footer'>
			<Button @callback="show_requests">Requests</Button>
			<p>Future Button (Settings)</p>
		</div>
	</div>
</template>
<script lang="ts">
import Button from './Button.vue';

export default {
	components: {
		Button,
	},

	methods: {
		show_requests(): void { console.log('redirecting to requests page.'); }
	}
};
</script>
<style scoped>
h1 {
	padding-top: 15px;
}

.navbar {
	padding-left: 15px;
	padding-right: 15px;
	display: flex;
	width: 15%;
	height: 100%;
	flex-direction: column;
	justify-content: space-between;
	background-color: #121a2a;
	min-width: 200px;
}

.navbar_footer {
	padding-bottom: 15px;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	width: 100%;
	height: 30%;
}
</style>
