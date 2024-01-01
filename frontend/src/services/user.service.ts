import type User from '@/interfaces/user.interface';

export default class UserService {
	static user: User;
	static is_set: boolean = false;

	static setUser(user: User): void {
		this.user = user;
		this.is_set = true;
	}

	static get getUser(): User { return this.user; }
	static get isSet(): boolean { return this.is_set; }
};