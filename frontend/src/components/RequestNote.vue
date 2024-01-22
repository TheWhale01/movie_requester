<template>
	<div class='body_container' @click='$emit("close_request_note");'>
		<div class='note_container' @click.stop>
			<textarea class="note_input" v-model='note_input' placeholder="Let the admins know any suggestions you have..." type="text" />
			<Button @callback='sendRequestEvent'>Add Note</Button>
		</div>
	</div>
</template>
<script lang='ts'>
import Button from '@/components/Button.vue';

export default {
	components: {
		Button,
	},

	data() {
		return {
			note_input: '' as string,
		};
	},

	methods: {
		sendRequestEvent(): void {
			let note: string | null = this.note_input ? this.note_input : null;
			this.$emit("add_note", note);
			this.$emit('close_request_note');
		},
	}
};
</script>
<style scoped>
.body_container {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	background-color: rgba(0, 0, 0, 0.3);
	z-index: 1000;
}

.note_container {
	width: 60%;
	height: 60%;
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
	align-items: center;
	background-color: #20293a;
	border-radius: 20px;
	box-shadow: 0px 1px 5px #121a2a;
}

::placeholder {
	text-align: center;
}

textarea {
	width: 85%;
	height: 70%;
	color: white;
	font-size: 1.2em;
	background-color: #121a2a;
	padding: 15px;
	box-shadow: 0px 1px 3px #121a2a;
	border: none;
}

</style>
