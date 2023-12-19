import MediaType from '../interfaces/media_type.enum';

export default interface Media {
	title: string;
	type: MediaType;
	nb_seasons: number;
	poster: string;
};
