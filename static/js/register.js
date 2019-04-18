let bth = document.querySelector('#send');

bth.addEventListener('click', () => {
    let xhr = new XMLHttpRequest();
    role = document.getElementById('role').value;

    xhr.open('POST', '/todo/api/register', true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(JSON.stringify({"data": role}));

    xhr.onreadystatechange = () => {
        if (xhr.readyState !== 4)
            return;

        if (xhr.status === 200) {
            data = JSON.parse(xhr.response).data;

            if (data.status === 'Ok' && data.location) {
                window.location.href = data.location;
            } else {
                alert('Ошибка! Повторите отправку позже')
            }
        } else {
            alert('Ошибка! Повторите отправку позже')
        }
    }
});