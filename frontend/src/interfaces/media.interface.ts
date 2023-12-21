import MediaType from '../interfaces/media_type.enum';

export default interface Media {
	title: string;
	type: MediaType;
	tmdb_id: number,
	nb_seasons: number;
	poster: string;
	poster_found: boolean;
	requested: boolean;
};
