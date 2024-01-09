<template>
	<div class="tickbox_container" :class="{ 'ticked': state }" @click="sendState">
		<font-awesome-icon v-if="state" class="icon" icon='fa-solid fa-check' />
	</div>
</template>
<script lang="ts">
export default {
    props: {
        baseState: { type: Boolean, required: true },
    },
    data() {
        return {
            state: false as boolean,
        };
    },

    beforeMount(): void { this.state = this.baseState; },

    methods: {
        sendState(): void {
            this.state = !this.state;
            this.$emit('state', this.state);
        },
    },

	watch: {
		baseState: function(newState, oldState): void {
			this.state = newState;
			this.$forceUpdate();
		},
	}
};
</script>
<style scoped>
div {
	width: 25px;
	height: 25px;
	border: 2px solid grey;
	border-radius: 5px;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: #121a2a;
	padding: 5px;
}

.ticked {
	background-color: #5046e5; 
}

.icon {
	width: 100%;
	height: 100%;
}
</style>