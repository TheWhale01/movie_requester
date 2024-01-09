<template>
	<input :placeholder="placeholder" :type='type' v-model='output' @input='handleInput' >
</template>
<script lang='ts'>
export default {
	props: {
		placeholder: { type: String },
		type: { type: String },
		prefill: { type: String },
	},
	data() {
		return {
			output: '' as string,
			typingTimeout: undefined as number | undefined,
		};
	},

	mounted(): void {
		if (this.prefill)
			this.output = this.prefill;
	},

	methods: {
		handleInput(): void {
			clearTimeout(this.typingTimeout);
			this.typingTimeout = setTimeout(() => {
				this.$emit('input-finished', this.output);
			}, 100);
		},
	},

	watch: {
		prefill: function(newString, oldString): void {
			this.output = newString;
			this.$forceUpdate();
		}
	}
};
</script>
<style scoped>
input {
	background-color: #121a2a;
	border: 2px solid #f6f9f9;
	font-size: 20px;
	border-radius: 30px;
	padding-top: 15px;
	padding-bottom: 15px;
	padding-left: 20px;
}
</style>
