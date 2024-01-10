<template>
    <div class="container">
        <form @submit.prevent="null">
            <h2>Change username</h2>
            <Input type="text" placeholder="Username" v-model="new_username" />
            <Button @click="changeUsername">Change !</Button>
        </form>
        <ErrorMessage v-if="show_error_msg">{{ error_msg }}</ErrorMessage>
    </div>
</template>
<script lang="ts">
import environment from '@/interfaces/environment.class';
import Button from './Button.vue';
import UserService from '@/services/user.service';
import Input from './Input.vue';
import ErrorMessage from './ErrorMessage.vue';
import { useNotification } from '@kyvg/vue3-notification';

export default {
    components: {
        Button,
        Input,
        ErrorMessage,
    },

    data() {
        return {
            new_username: '' as string,
            show_error_msg: false as boolean,
            error_msg: '' as string,
        };
    },

    methods: {
        async changeUsername(): Promise<void> {
            this.show_error_msg = false;
            if (!this.new_username) {
                this.showErrorMsg('Please fill all the fields');
                return ;
            }
            const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.API_ENDPOINT}/user/username?username=${this.new_username}`, {
                method: 'POST',
                headers: {
                    'Authorization': `bearer ${sessionStorage.getItem('access_token')}`,
                    'Content-Type': 'application/json',
                },
            });
            if (!response.ok) {
                this.showErrorMsg(JSON.parse(await response.text())['detail']);
                return;
            }
            const response_json = await response.json();
            UserService.setUser({
                id: response_json['user']['id'],
                username: response_json['user']['username'],
                profile_picture: response_json['user']['profile_picture'],
                language: response_json['user']['language'],
                privilege: response_json['user']['privilege']
            });
            const notif = useNotification();
            notif.notify({
                type: 'success',
                title: 'User',
                text: 'Username successfully changed.',
            })
        },

        showErrorMsg(error: string): void {
            this.error_msg = error;
            this.show_error_msg = true;
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
    height: 30%;
    width: 30%;
    display: flex;
    text-align: center;
    align-items: center;
    justify-content: space-between;
    flex-direction: column;
    margin-bottom: 50px;
}

form * {
    width: 100%;
}
</style>