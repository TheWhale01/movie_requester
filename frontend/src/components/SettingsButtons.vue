<template>
    <div class="settings_btn_container">
        <button @click="sendEvent(1)" :class="{'selected': selected_button === 1}">Change username</button>
        <button @click="sendEvent(2)" :class="{'selected': selected_button === 2}">Change Password</button>
        <button @click="sendEvent(3)" :class="{'selected': selected_button === 3}">Change profile picture</button>
        <button @click="sendEvent(4)" :class="{'selected': selected_button === 4}">Change language</button>
        <button @click="sendEvent(5)" :class="{'selected': selected_button === 5}">Notifications</button>
        <button v-if='user.privilege === 0' @click="sendEvent(6)" :class="{'selected': selected_button === 6}">Create new user</button>
        <button class="logout_btn" @click="logout">Logout</button>
    </div>
</template>
<script lang="ts">
import type User from '@/interfaces/user.interface';
import UserService from '@/services/user.service';

export default {
    data() {
        return {
            selected_button: 1 as number,
            user: {} as User,
        };
    },

    beforeMount(): void {
        this.user = UserService.getUser;
    },

    methods: {
        sendEvent(event_nb: number): void {
            this.selected_button = event_nb;
            this.$emit('event', event_nb);
        },

        logout(): void {
            sessionStorage.removeItem('access_token');
            this.$router.push('/login');
        }
    }
};
</script>
<style scoped>
.settings_btn_container {
    margin: auto;
}

button {
	border-bottom: 3px solid #5046e5;
    padding: 15px;
    font-size: 1em;
    font-weight: bold;
}

button:hover {
    background-color: #121a2a;
}

.selected {
    background-color: #121a2a;
}

.logout_btn {
    border-bottom: 3px solid red;
}

.logout_btn:hover {
    background-color: rgba(255, 0, 0, 0.5);
}
</style>
