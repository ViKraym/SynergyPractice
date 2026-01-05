// Получаем элементы DOM
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const output = document.getElementById('output');

// Функция проверки, является ли значение числом
function isNumber(value) {
    // Преобразуем в строку, убираем пробелы, затем проверяем на число
    const str = String(value).trim();
    
    // Если строка пустая — не число
    if (str === '') {
        return false;
    }
    // Проверяем, что строка представляет число (включая отрицательные и дробные)
    return !isNaN(parseFloat(str)) && isFinite(parseFloat(str));
}


// Функция вывода результата
function showResult(result) {
    output.textContent = result;
}

// Функции математических операций
function sum() {
    const a = parseFloat(num1Input.value);
    const b = parseFloat(num2Input.value);

    if (isNumber(a) && isNumber(b)) {
        showResult(a + b);
    } else {
        showResult('Ошибка: введите числа!');
    }
}

function difference() {
    const a = parseFloat(num1Input.value);
    const b = parseFloat(num2Input.value);

    if (isNumber(a) && isNumber(b)) {
        showResult(a - b);
    } else {
        showResult('Ошибка: введите числа!');
    }
}

function product() {
    const a = parseFloat(num1Input.value);
    const b = parseFloat(num2Input.value);

    if (isNumber(a) && isNumber(b)) {
        showResult(a * b);
    } else {
        showResult('Ошибка: введите числа!');
    }
}

function division() {
    const a = parseFloat(num1Input.value);
    const b = parseFloat(num2Input.value);

    if (!isNumber(a) || !isNumber(b)) {
        showResult('Ошибка: введите числа!');
        return;
    }

    if (b === 0) {
        showResult('Ошибка: деление на ноль!');
        return;
    }

    showResult(a / b);
}
