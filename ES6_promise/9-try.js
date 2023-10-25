export default function guardrail(mathFunction) {
	let value;

	try {
		value = mathFunction();
	} catch (error) {
		value = error.toString();
	}

	return [value, 'Guardrail was processed'];
}
