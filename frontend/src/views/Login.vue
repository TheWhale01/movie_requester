<template>
	<div class="login_page_container">
		<h1>Welcome to Movie Requester !</h1>
		<div class="form_container">
			<div class="login_container">
				<h2>Already have an account ?</h2>
				<form @submit.prevent="null">
					<Input placeholder='e-mail / username' type="text" @input-finished="getUsername" />
					<Input placeholder='password' type='password' @input-finished="getPassword" />
					<Button @callback='login'>Login</Button>
					<ErrorMessage v-if="show_login_error_msg">{{ login_error_msg }}</ErrorMessage>
				</form>
			</div>
			<div class="border"></div>
			<div class="signup_container">
				<h2>First time ?</h2>
				<form @submit.prevent="null">
					<Input placeholder='e-mail' type='text' @input-finished="getEmail" />
					<Input placeholder='username' type='text' @input-finished="getUsername" />
					<Input placeholder='password' type='password' @input-finished="getPassword" />
					<Input placeholder='repeat password' type='password' @input-finished="getPasswordConfirmation" />
					<Button @callback='signup'>Sign Up</Button>
					<ErrorMessage v-if="show_signup_error_msg">{{ signup_error_message }}</ErrorMessage>
				</form>
			</div>
		</div>
	</div>
</template>
<script lang="ts">
import Button from '../components/Button.vue';
import Input from '../components/Input.vue';
import ErrorMessage from '../components/ErrorMessage.vue';
import emailValidator from '../utils/EmailValidator';
import passValidator from '../utils/PasswordValidator';

export default {
	components: {
		Button,
		Input,
		ErrorMessage,
	},
	data() {
		return {
			email: '' as string,
			username: '' as string,
			password: '' as string,
			password_confirmation: '' as string,
			signup_error_message: '' as string,
			login_error_msg: '' as string,
			show_signup_error_msg: false as boolean,
			show_login_error_msg: false as boolean,
		};
	},
	methods: {
		showSignupError(msg: string): void {
			this.signup_error_message = msg;
			this.show_signup_error_msg = true;
		},

		showLoginError(msg: string): void {
			this.login_error_msg = msg;
			this.show_login_error_msg = true;
		},

		login(): void {
			if (!this.email || !this.password) {
				this.showLoginError("Please all the fields.");
				return ;
			}
			console.log('Send login informations to backend.');
			// Check if the authentication has succeded
		},

		signup(): void {
			this.show_signup_error_msg = false;
			if (!emailValidator(this.email))
				this.showSignupError("Email not valid.");
			else if (this.password != this.password_confirmation)
				this.showSignupError("Passwords do not match.");
			else if (passValidator(this.password))
				this.showSignupError("Password does not match the requirements.");
			else if (!this.email || !this.username || !this.password || !this.password_confirmation)
				this.showSignupError("Please fill all the fields.");
			else {
				console.log("Send signup informations to backend.");
				// Check if the inscription has succeded
			}
		},
	
		getUsername(value: string): void { this.username = value; },
		getPassword(value: string): void { this.password = value; },
		getPasswordConfirmation(value: string): void { this.password_confirmation = value; },
		getEmail(value: string): void { this.email = value; },

	},
};
</script>
<style scoped>
h1 {
	text-align: center;
	padding-top: 50px;
	position: absolute;
	top: 0;
	width: 100%;
}

h2 {
	font-size: xx-large;
	text-align: center;
}
.login_page_container {
	display: flex;
	align-items: center;
	height: 100vh;
}

.form_container {
	display: flex;
	flex-direction: row;
	width: 100%;
	height: 50%;
	justify-content: space-evenly;
}

.signup_container, .login_container {
	display: flex;
	flex-direction: column;
	width: 100%;
	justify-content: space-between;
}

form {
	display: flex;
	align-items: center;
	height: 100%;
	justify-content: space-evenly;
	flex-direction: column;
}

form * {
	width: 50%;
}

.border {
	border: 1px solid grey;
}

</style>
