import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: () => import('../views/Home.vue'),
		},
		{
			path: '/login',
			name: 'login',
			component: () => import('../views/Login.vue'),
		},
		{
			path: '/request',
			name: 'request',
			component: () => import('../views/Requests.vue'),
		}
	]
})

export default router
