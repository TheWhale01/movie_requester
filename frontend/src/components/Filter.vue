<template>
    <div class="filter_container">
        <Button @callback="showOptions">Filter</Button>
        <div v-if="showOptionsBool" class="options_container">
            <span @click="$emit('option', 1)">All requests</span>
            <span @click="$emit('option', 2)">Your requests</span>
        </div>
    </div>
</template>
<script lang="ts">
import Button from './Button.vue';

export default {
    components: {
        Button,
    },

    data() {
        return {
            showOptionsBool: false as boolean,
        };
    },

    methods: {
        showOptions(): void { this.showOptionsBool = !this.showOptionsBool },
    },
};
</script>
<style scoped>
.filter_container {
    width: 150px;
}

.options_container {
    background-color: #121a2a;
    width: 100%;
    border: 1px solid white;
}

span {
    display: block;
    text-align: center;
    padding-top: 15px;
    padding-bottom: 15px;
    border-top: 1px solid white;
}

</style>