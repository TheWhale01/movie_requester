<template>
	<input :placeholder="placeholder" :type='type' v-model='output' @input='handleInput' @blur='handleBlur'>
</template>
<script lang='ts'>
export default {
	props: {
		placeholder: { type: String },
		type: { type: String },
	},
	data() {
		return {
			output: '' as string,
			typingTimeout: undefined as number | undefined,
		};
	},
	methods: {
		handleInput(): void {
			clearTimeout(this.typingTimeout);
			this.typingTimeout = setTimeout(() => {
				this.$emit('input-finished', this.output);
			}, 100);
		},
		handleBlur(): void {
			this.$emit('input-finished', this.output);
		}
	},
};
</script>
<style scoped>
input {
	display: block;
	background-color: #121a2a;
	border: 2px solid #f6f9f9;
	font-size: 20px;
	border-radius: 30px;
	padding-top: 15px;
	padding-bottom: 15px;
	padding-left: 20px;
}
</style>
