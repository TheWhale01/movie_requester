import type User from '@/interfaces/user.interface';

export default class UserService {
	static user: User;

	static setUser(user: User): void { this.user = user; }
	static get getUser(): User { return this.user; }
};