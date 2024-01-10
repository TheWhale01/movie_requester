export default class environment {
	static readonly BACKEND_HOST: string = import.meta.env.VITE_BACKEND_HOST;
	static readonly BACKEND_PORT: number = Number(import.meta.env.VITE_BACKEND_PORT);
	static readonly HTTP_SCHEMA: string = import.meta.env.VITE_HTTP_SCHEMA;
	static readonly API_ENDPOINT: string = import.meta.env.VITE_API_ENDPOINT;
}