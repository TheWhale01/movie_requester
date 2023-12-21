import type Request from "./request.interface";

export default interface User {
	id: number;
	username: string;
	profile_picture: string;
	lang: string;
	requests: Request[];
};