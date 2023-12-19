<template>
	<div class='navbar'>
		<h1>Movie Requester</h1>
		<div class='navbar_footer'>
			<p>Future Button (Requests)</p>
			<p>Future Button (Settings)</p>
		</div>
	</div>
</template>
<style scoped>
h1 {
	padding-top: 15px;
}

.navbar {
	padding-left: 20px;
	display: flex;
	width: 15%;
	height: 100%;
	flex-direction: column;
	justify-content: space-between;
	background-color: #121a2a;
}

.navbar_footer {
	padding-bottom: 20px;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	width: 100%;
	height: 30%;
}
</style>
