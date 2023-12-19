<template>
	<button @click='send_callback'>
			<slot></slot>
	</button>
</template>
<script lang="ts">
export default {
	methods: {
		send_callback(): void {
			this.$emit('callback');
		},
	},
};
</script>
<style scoped>
button {
	height: 50px;
	width: 150px;
	background-color: #5046e5;
	cursor: pointer;
	border: none;
	border-radius: 10px;
	box-shadow: 0px 1px 5px #121a2a;
	font-weight: bold;
	font-size: medium;
}

button span {
	padding-right: 50px;
	padding-left: 50px;
}
</style>
