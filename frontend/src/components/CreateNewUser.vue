<template>
    <div class="container">
        <form @submit.prevent="null">
            <h2>Create New User</h2>
            <Input type="text" placeholder="Username" v-model="username" />
            <Input type="password" placeholder="Password" v-model="password"/>
            <Input type="password" placeholder="Confirmation" v-model="password_conf"/>
            <select v-model="privilege">
                <option selected disabled hidden value="-1">User Privilege</option>
                <option value="0">Admin</option>
                <option value="1">Normal user</option>
            </select>
            <Button @callback="createNewUser">Create !</Button>
        </form>
        <ErrorMessage v-if="show_error_msg">{{ error_msg }}</ErrorMessage>
    </div>
</template>
<script lang="ts">
import Button from './Button.vue';
import Input from './Input.vue';
import ErrorMessage from './ErrorMessage.vue';
import environment from '@/interfaces/environment.class';

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
            password_conf: '' as string,
            privilege: -1 as number,
            error_msg: '' as string,
            show_error_msg: false as boolean,
        }
    },

    methods: {
        async createNewUser(): Promise<void> {
            this.show_error_msg = false;
            if (!this.username || !this.password || !this.password_conf || this.privilege == -1) {
                this.showErrorMsg('Please fill all the fields');
                return ;
            }
            else if (this.password !== this.password_conf) {
                this.showErrorMsg('Password mismatch');
                return ;
            }
            const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/user/create`, {
                method: 'post',
                headers: {
                    'Authorization': `bearer ${sessionStorage.getItem('access_token')}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "username": this.username,
                    "password": this.password_conf
                }),
            });
            if (!response.ok) {
                this.showErrorMsg(JSON.parse(await response.text())['detail']);
                return ;
            }
        },

        showErrorMsg(error: string): void {
            this.error_msg = error;
            this.show_error_msg = true;
        },
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

form * {
    width: 100%;
}
</style>