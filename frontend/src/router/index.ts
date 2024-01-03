import environment from '@/interfaces/environment.class';
import UserService from '@/services/user.service';
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
});

router.beforeEach(async (to, from, next): Promise<void> => {
	if (to.name !== 'login') {
		const response = await fetch(`http://${environment.BACKEND_HOST}:${environment.BACKEND_PORT}/login`, {
			method: 'get',
			headers: { 'authorization': `bearer ${sessionStorage.getItem('access_token')}` }
		});
		if (!response.ok) {
			next('/login');
			return;
		}
		UserService.setUser((await response.json())['user']);
	}
	next();
});
export default router
