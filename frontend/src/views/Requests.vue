<template>
	<div class="container">
		<Navbar />
		<p>Welcome to requests</p>
	</div>
</template>
<script lang="ts">
// If user is admin, show all requests
// else show only requests of the user.
// (Backend)

// For earch request check the state
// if request is PENDING show buttons to accept or deny

import Navbar from '@/components/Navbar.vue';

export default {
	components: {
		Navbar,
	}
};
</script>