import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
	const signUp = {
		status: 'fulfilled',
	};
	const uploadPh = {
		status: 'fulfilled',
	};

	try {
		signUp.value = await signUpUser(firstName, lastName);
	} catch (err) {
		signUp.status = 'rejected';
		signUp.value = err.toString();
	}

	try {
		uploadPh.value = await uploadPhoto(fileName);
	} catch (err) {
		uploadPh.status = 'rejected';
		uploadPh.value = err.toString();
	}

	return [signUp, uploadPh];
}
