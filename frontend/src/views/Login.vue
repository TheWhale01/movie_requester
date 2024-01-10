<template>
	<div class="container">
		<h1>Welcome to Movie Requester !</h1>
		<div class="form_container">
			<div class="login_container">
				<h2>Login</h2>
				<form @submit.prevent="null">
					<Input placeholder='username' type="text" @input-finished="getUsername" />
					<Input placeholder='password' type='password' @input-finished="getPassword" />
					<Button @callback='login'>Login</Button>
				</form>
				<ErrorMessage v-if="show_login_error_msg">{{ login_error_msg }}</ErrorMessage>
			</div>
		</div>
	</div>
</template>
<script lang="ts">
import Button from '../components/Button.vue';
import Input from '../components/Input.vue';
import ErrorMessage from '../components/ErrorMessage.vue';
import environment from '../interfaces/environment.class';

export default {
	components: {
		Button,
		Input,
		ErrorMessage,
	},
	
	data() {
		return {
			username: '' as string,
			password: '' as string,
			login_error_msg: '' as string,
			show_login_error_msg: false as boolean,
		};
	},

	async beforeCreate(): Promise<void> {
		const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/login`, {
			method: 'get',
			headers: {'authorization': `bearer ${sessionStorage.getItem('access_token')}`}
		});
		if (!response.ok)
			return ;
		this.$router.push('/');
	},

	methods: {
		showLoginError(msg: string): void {
			this.login_error_msg = msg;
			this.show_login_error_msg = true;
		},

		async login(): Promise<void> {
			this.show_login_error_msg = false;
			if (!this.username || !this.password) {
				this.showLoginError("Please all the fields.");
				return ;
			}
			const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/login`, {
				method: 'post',
				headers: {'Content-Type': 'application/json'},
				body: JSON.stringify({
					'username': this.username,
					'password': this.password
				}),
			});
			if (!response.ok) {
				this.showLoginError(JSON.parse((await response.text()))['detail']);
				return ;
			}
			const response_json = await response.json();
			sessionStorage.setItem('access_token', response_json['token']);
			this.$router.push('/');
		},

		getUsername(value: string): void { this.username = value; },
		getPassword(value: string): void { this.password = value; },
	},
};
</script>
<style scoped>
h1 {
	text-align: center;
	padding-top: 50px;
}

h2 {
	font-size: xx-large;
	text-align: center;
}

.container {
	flex-direction: column;
}

.form_container {
	display: flex;
	height: 100%;
	justify-content: center;
	align-items: center;
}

.login_container {
	display: flex;
	flex-direction: column;
	width: 30%;
	height: 55%;
}

.login_container form {
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
	height: 100%;
}

.login_container form Button {
	width: 100%;
}

</style>
