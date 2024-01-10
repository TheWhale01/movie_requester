<template>
    <div class="container">
        <form @submit.prevent="null">
            <h2>Change Password</h2>
            <Input type="password" placeholder="Old Password" v-model="old_password" />
            <Input type="password" placeholder="New Password" v-model="new_password" />
            <Input type="password" placeholder="Confirmation" v-model="confirmation" />
            <Button @click="changePassword">Change !</Button>
        </form>
        <ErrorMessage class="error" v-if="show_error_msg">{{ error_msg }}</ErrorMessage>
    </div>
</template>
<script lang="ts">
import Button from './Button.vue';
import Input from './Input.vue';
import ErrorMessage from './ErrorMessage.vue';
import environment from '@/interfaces/environment.class';
import { useNotification } from '@kyvg/vue3-notification';

export default {
    components: {
        Button,
        Input,
        ErrorMessage,
    },

    data() {
        return {
            old_password: '' as string,
            new_password: '' as string,
            confirmation: '' as string,
            error_msg: '' as string,
            show_error_msg: false as boolean,
        };
    },

    methods: {
        async changePassword(): Promise<void> {
            this.show_error_msg = false;
            if (!this.old_password || !this.new_password || !this.confirmation) {
                this.showErrorMsg('Please fill all the fields');
                return;
            }
            else if (this.confirmation !== this.new_password) {
                this.showErrorMsg('Passwords do not match');
                return;
            }
            const response = await fetch(`${environment.HTTP_SCHEMA}://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/user/password`, {
                method: 'post',
                headers: {
                    'Authorization': `bearer ${sessionStorage.getItem('access_token')}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "old_password": this.old_password,
                    "new_password": this.confirmation,
                }),
            });
            if (!response.ok) {
                this.showErrorMsg(JSON.parse((await response.text()))['detail']);
                return;
            }
            const notif = useNotification();
            notif.notify({
                type: 'success',
                title: 'User',
                text: 'Password successfully changed.'
            });
        },

        showErrorMsg(error: string): void {
            this.error_msg = error;
            this.show_error_msg = true;
        }
    }
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

form * {
    width: 100%;
}
</style>