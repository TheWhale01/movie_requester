export default function passwordValidator(password: string): boolean {
	const regex: RegExp = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d])$/;
	return (password.length > 8 && regex.test(password));
}