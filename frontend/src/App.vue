<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
	<header>
		<div class="wrapper">
			<nav>
				<RouterLink to="/" />
				<RouterLink to="login" />
				<RouterLink to="request" />
				<RouterLink to="settings" />
			</nav>
		</div>
	</header>
	<notifications position="top center"/>
	<RouterView />
</template>

<style scoped></style>
