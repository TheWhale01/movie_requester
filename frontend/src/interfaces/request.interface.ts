import type MediaType from "./media_type.enum";
import StatusType from "./status_type.enum";

export default interface Request {
	id: number;
	user_id: number;
	tmdb_id: number;
	date: string;
	status: StatusType;
	type: MediaType;
}