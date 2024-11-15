var last_unit = ''
var toggled_unit = ''

function toggle_div(unit) {
    var div = document.getElementById('value_block');
    if (last_unit === ''){
        div.style.display = 'block'
        last_unit = unit;
    } else {
        if (unit === last_unit){
            div.style.display = 'none';
            last_unit = '';
        } else {
            last_unit =  unit;
        }
    }
    toggled_unit = unit;
    draw_text(unit);
    draw_select(unit, 'converted_from')
    draw_select(unit, 'converted_to')
}

function draw_text(unit) {
    document.getElementById('value_label').textContent = 'Enter the ' + unit + ' to convert:';
}

function draw_select(unit, id) {
    const select = document.getElementById(id);
    while (select.firstChild) {
        select.removeChild(select.firstChild);
    }
    let new_select = [];
    switch (unit) {
        case 'length':
            new_select = [
                {value: 'millimeter', text: 'millimeter'},
                {value: 'centimeter', text: 'centimeter'},
                {value: 'meter', text: 'meter'},
                {value: 'kilometer', text: 'kilometer'},
                {value: 'inch', text: 'inch'},
                {value: 'foot', text: 'foot'},
                {value: 'yard', text: 'yard'},
                {value: 'mile', text: 'mile'}
            ];
            break;
        case 'weight':
            new_select = [
                {value: 'milligram', text: 'milligram'},
                {value: 'gram', text: 'gram'},
                {value: 'kilogram', text: 'kilogram'},
                {value: 'ounce', text: 'ounce'},
                {value: 'pound', text: 'pound'}
            ];
            break;
        case 'temperature':
            new_select = [
                {value: 'celsius', text: 'celsius'},
                {value: 'fahrenheit', text: 'fahrenheit'},
                {value: 'kelvin', text: 'kelvin'}
            ];
            break;
    }
    new_select.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option.value;
        opt.textContent = option.text;
        select.appendChild(opt);
    })
}

document.addEventListener("DOMContentLoaded", function (){
    const calculate_button = document.getElementById('calculate');
    const value = document.getElementById('value');
    const converted_from = document.getElementById('converted_from');
    const converted_to = document.getElementById('converted_to');
    const result_span = document.getElementById('result');

    calculate_button.addEventListener('click', function (event){
        event.preventDefault();
        const data={
            value: value.value,
            converted_from: converted_from.value,
            converted_to: converted_to.value,
            unit: toggled_unit
        };
        console.log(`POST запрос отправлен ${JSON.stringify(data)}`);

        fetch('/convert_length',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.text())
        .then(result => {
            result_span.innerText = result
            console.log('RESULT = ' + result)
        });
    });
});