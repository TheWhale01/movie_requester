<template>
	<button @click='send_callback'>
		<span>
			<slot></slot>
		</span>
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
	background-color: #5046e5;
	cursor: pointer;
	border: none;
	border-radius: 10px;
	box-shadow: 0px 1px 5px #121a2a;
}

button span {
	padding-right: 50px;
	padding-left: 50px;
	font-size: medium;
	font-weight: bold;
}
</style>
