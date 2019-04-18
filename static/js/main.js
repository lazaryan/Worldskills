let pay = document.querySelector('#pay');
let sendBth = document.querySelector('#sendBth');
let select = document.querySelector('#sendPy');
let id = document.querySelector('#id');

pay.addEventListener('input', (e) => {
    target = e.target;
    target.value = +target.value;

    if (+target.value > +target.dataset.max){
        target.value = target.dataset.max;
    }

    if (+target.value < 0) {
        target.value = 0;
    }
});

sendBth.addEventListener('click', () => {
    if (+pay.value === 0) {
        alert('Введите сумму!');
        return '';
    }

    if (!select.value) {
        alert('Не выбран пользователь!');
        return '';
    }

    let data = {
        "to": select.value,
        "from": id.dataset.id,
        "coins": pay.value
    };
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/todo/api/pay', true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(JSON.stringify(data));

    xhr.onreadystatechange = () => {
        if (xhr.readyState !== 4)
            return;

        if (xhr.status === 200) {
            data = JSON.parse(xhr.response).data;

        } else {
            alert('Ошибка! Повторите отправку позже')
        }
    }
});