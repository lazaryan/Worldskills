let id = document.querySelector('#id_user');
let keys = document.querySelector('#keys');
let enter_bth = document.querySelector('#enter_bth');


enter_bth.addEventListener('click', () => {
    console.log(id);
   id =  id.value;
   if (!id) {
       alert('Введите данные!')
       return '';
   }
   key = {};
   inp = keys.querySelectorAll('li input');
   for (let i = 0; i < inp.length; i++) {
       if (!inp[i].value) {
           alert('Введите данные!')
           return '';
       }
       key[inp[i].name] = inp[i].value;
   }
   data = {
     "id": id,
     "keys": key
   };

    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/todo/api/enter', true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.send(JSON.stringify(data));

    xhr.onreadystatechange = () => {
        if (xhr.readyState !== 4)
            return;

        if (xhr.status === 200) {
            data = JSON.parse(xhr.response).data;
            if (data === 'err') {
                alert('Не правильно введены данные!')
            } else {

            }

        } else {
            alert('Ошибка! Повторите отправку позже')
        }
    }
});