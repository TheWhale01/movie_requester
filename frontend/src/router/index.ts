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
		},
		{
			path: '/settings',
			name: 'settings',
			component: () => import('../views/Settings.vue'),
		},
	]
})

export default router
