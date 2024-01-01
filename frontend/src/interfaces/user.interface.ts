import type Privilege from "./privilege.enum";

export default interface User {
	id: number;
	username: string;
	profile_picture: string;
	language: string;
	privilege: Privilege;
};