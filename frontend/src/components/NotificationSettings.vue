<template>
	<div class="container">
		<form @submit.prevent="null">
			<div class="checkbox_container">
				<label for="telegram">Click to activate/deactivate telegram notifications</label>
				<TickBox class="checkbox" name="telegram" :baseState="activated" @state="updateState" />
			</div>
			<Input v-if="activated" placeholder="Chat ID" type="text" v-model="chat_id" :prefill="chat_id"/>
			<Input v-if="activated" placeholder="Bot Token" type="text" v-model="bot_id" :prefill="bot_id"/>
			<h2 v-else>Telegram notifications desactivated</h2>
			<Button @callback="save">Save</Button>
		</form>
		<ErrorMessage v-if="show_error">{{ error_msg }}</ErrorMessage>
	</div>
</template>
<script lang="ts">
import TickBox from './TickBox.vue';
import Input from './Input.vue';
import Button from './Button.vue';
import ErrorMessage from './ErrorMessage.vue';
import environment from '@/interfaces/environment.class';
import { useNotification } from '@kyvg/vue3-notification';

export default {
	components: {
		TickBox,
		Button,
		Input,
		ErrorMessage,
	},

	data() {
		return {
			activated: false as boolean,
			state_changed: false as boolean,
			created: false as boolean,
			chat_id: '' as string,
			bot_id: '' as string,
			show_error: false as boolean,
			error_msg: '' as string,
		};
	},

	async beforeMount(): Promise<void> { await this.getSettings(); },

	methods: {
		updateState(value: boolean): void {
			this.activated = value;
			this.state_changed = true;
		},

		async save(): Promise<void> {
			this.show_error = false;
			if (this.state_changed) {
				if (this.activated && this.created)
					await this.activate();
				else if (!this.activated && this.created)
					await this.deactivate(); 
			}
			else if (this.activated && !this.created) {
				if (!this.bot_id || !this.chat_id) {
					this.showErrorMsg("Please fill all the fields");
					return ;
				}
				await this.create();
			}
			else if (this.activated && this.created)
				await this.updateSettings();
		},

		async updateSettings(): Promise<void> {
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/telegram/update`, {
				method: 'post',
				headers: {
					'Authorization': `bearer ${sessionStorage.getItem('access_token')}`,
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					'chat_id': this.chat_id,
					'bot_id': this.bot_id,
				}),
			});
			const notif = useNotification();
			if (!response.ok) {
				notif.notify({
					title: "Telegram",
					type: 'error',
					text: JSON.parse(await response.text())['detail'],
				});
				return ;
			}
			notif.notify({
				title: 'Telegram',
				type: 'success',
				text: 'settings updated'
			});
		},

		async create(): Promise<void> {
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/telegram/create`, {
				method: 'post',
				headers: {
					'Authorization': `bearer ${sessionStorage.getItem('access_token')}`,
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					'chat_id': this.chat_id,
					'bot_id': this.bot_id,
				}),
			});
			const notif = useNotification();
			if (!response.ok) {
				notif.notify({
					title: 'Telegram',
					type: 'error',
					text: JSON.parse(await response.text())['detail'],
				});
				return;
			}
			const response_json = (await response.json());
			if (!response_json['settings'])
				return;
			this.chat_id = response_json['settings']['chat_id'];
			this.bot_id = response_json['settings']['bot_id'];
			this.activated = response_json['settings']['active'];
			notif.notify({
				title: 'Telegram',
				type: 'success',
				text: 'Notifications activated',
			});
		},

		async deactivate(): Promise<void> {
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/telegram/deactivate`, {
				method: 'post',
				headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` },
			});
			const notif = useNotification();
			if (!response.ok) {
				notif.notify({
					type: 'error',
					title: 'Telegram',
					text: JSON.parse(await response.text())['detail'],
				});
				return;
			}
			notif.notify({
				type: 'success',
				title: 'Telegram',
				text: 'Settings successfully deactivated',
			});
		},

		async activate(): Promise<void> {
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/telegram/activate`, {
				method: 'post',
				headers: {'Authorization': `bearer ${sessionStorage.getItem('access_token')}`},
			});
			const notif = useNotification();
			if (!response.ok) {
				notif.notify({
					title: "Telegram",
					type: 'error',
					text: JSON.parse(await response.text())['detail'],
				});
				return ;
			}
			notif.notify({
				title: 'Telegram',
				type: 'success',
				text: 'Notifications activted',
			});
		},

		async getSettings(): Promise<void> {
			const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/telegram/get`, {
				method: 'get',
				headers: { 'Authorization': `bearer ${sessionStorage.getItem('access_token')}` },
			});
			if (!response.ok) {
				return;
			}
			const response_json = await response.json();
			if (!response_json['settings']) {
				this.created = false;
				return;
			}
			this.activated = response_json['settings']['active'];
			this.bot_id = response_json['settings']['bot_id'];
			this.chat_id = response_json['settings']['chat_id'];
			this.created = true;
		},

		showErrorMsg(error_msg: string): void {
			this.error_msg = error_msg;
			this.show_error = true;
		}
	},
};
</script>
<style scoped>
.container {
	justify-content: center;
	align-items: center;
	flex-direction: column;
}

form {
	height: 50%;
	width: 30%;
	display: flex;
	text-align: center;
	align-items: center;
	justify-content: space-between;
	flex-direction: column;
	margin-bottom: 50px;
}

form Input,
form Button {
	width: 100%;
}

.checkbox_container {
	display: flex;
	flex-direction: row-reverse;
	align-items: center;
}

label {
	font-weight: bold;
	font-size: large;
}
</style>