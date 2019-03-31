var form = document.querySelector('#logForm');
var bth = document.querySelector('#cardAction');

bth.addEventListener('click', function() {
	var inputs = document.querySelectorAll('input');
	var text={};

	for (var i = 0; i < inputs.length; i++) {
		text[inputs[i].name] = inputs[i].value
	}

	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/todo/api/login', true);
	xhr.setRequestHeader("Content-type", "application/json");

	xhr.send(JSON.stringify(text));

	xhr.onreadystatechange = function () {
		if (xhr.readyState != 4) return;

		if (xhr.status == 200) {
			var data = JSON.parse(xhr.responseText);

			if (data.data = 'OK') {
				document.location.href = "{{ url_for('index') }}"
			}
		}
	}
});