let form = document.querySelector('#registerForm');
let bth_action = document.querySelector('#cardAction');

bth_action.addEventListener('click', function(e) {
	e.preventDefault();

	let inputs = form.querySelectorAll('input');
	let select = form.querySelector('select');

	let data = {};

	for (let i = 0; i < inputs.length; i++) {
		data[inputs[i].name] = inputs[i].value;
	}

	data.role = select.value;

	let xhr = new XMLHttpRequest();
	xhr.open('POST', '/todo/api/register', true);
	xhr.setRequestHeader('Content-type', 'application/json');

	xhr.send(JSON.stringify(data));

	xhr.onreadystatechange = function () {
		if (xhr.readyState != 4) {
			return;
		}

		if (xhr.status == 200) {
			let data = JSON.parse(xhr.response);

			if (data.data = 'Ok') {
				document.location.href = data.location;
			} else {
				alert('Ошибка ввода! Повторите попытку');
			}
		} else {
			alert('Ошибка сервера! Повторите попытку позже');
		}
	}
});