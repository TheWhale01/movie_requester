<template>
	<div class="container">
		<Navbar />
		<div class="main_page">
			<SettingsButtons @event="getEvent"/>
			<ChangeUsername v-if="show_change_username"/>
			<ChangePassword v-if="show_change_password"/>
			<ChangeProfilePicture v-if="show_change_profile_picture" />
			<ChangeLanguage v-if="show_change_language" />
			<NotificationSettings v-if="show_notifications" />
			<CreateNewUser v-if="show_create_user" />
		</div>
	</div>
</template>
<script lang="ts">
import Navbar from '@/components/Navbar.vue';
import ChangeUsername from '@/components/ChangeUsername.vue';
import ChangePassword from '@/components/ChangePassword.vue';
import SettingsButtons from '@/components/SettingsButtons.vue';
import ChangeProfilePicture from '@/components/ChangeProfilePicture.vue';
import ChangeLanguage from '@/components/ChangeLanguage.vue';
import environment from '@/interfaces/environment.class';
import NotificationSettings from '@/components/NotificationSettings.vue';
import CreateNewUser from '@/components/CreateNewUser.vue';

export default {
	components: {
		Navbar,
		ChangeUsername,
		ChangePassword,
		ChangeProfilePicture,
		ChangeLanguage,
		NotificationSettings,
		CreateNewUser,
		SettingsButtons,
	},

	data() {
		return {
			show_change_username: true as boolean,
			show_change_password: false as boolean,
			show_change_profile_picture: false as boolean,
			show_change_language: false as boolean,
			show_notifications: false as boolean,
			show_create_user: false as boolean,
		};
	},

	async mounted(): Promise<void> {
		const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/login`, {
			method: 'get',
			headers: {'authorization': `bearer ${sessionStorage.getItem('access_token')}`}
		});
		if (!response.ok)
			this.$router.push('/login');
	},

	methods: {
		getEvent(event: number): void {
			this.show_change_username = false;
			this.show_change_password = false;
			this.show_change_profile_picture = false;
			this.show_change_language = false;
			this.show_notifications = false;
			this.show_create_user = false;
			switch(event) {
				case 1:
					this.show_change_username = true;
					break ;
				case 2:
					this.show_change_password = true;
					break;
				case 3:
					this.show_change_profile_picture = true;
					break;
				case 4:
					this.show_change_language = true;
					break ;
				case 5:
					this.show_notifications = true;
					break;
				case 6:
					this.show_create_user = true;
					break ;
				default:
					break;
			}
		}
	}
};
</script>
<style scoped>
</style>