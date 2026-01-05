let counter = 0;
const resultElement = document.getElementById('result');
const plusBtn = document.getElementById('plusBtn');
const minusBtn = document.getElementById('minusBtn');
const extremeMessage = document.getElementById('extremeMessage');

// Функция обновления фона в зависимости от значения счётчика
function updateBackgroundColor() {
    if (counter > 0) {
        resultElement.style.backgroundColor = 'yellow';
    } else if (counter < 0) {
        resultElement.style.backgroundColor = 'green';
    } else {
        resultElement.style.backgroundColor = 'red';
    }
}

// Функция проверки экстремальных значений и активации/деактивации кнопок
function checkExtremeValues() {
    if (counter >= 10) {
        plusBtn.disabled = true;
        extremeMessage.style.display = 'block';
        extremeMessage.textContent = 'Вы достигли экстремального значения';
    } else if (counter <= -10) {
        minusBtn.disabled = true;
        extremeMessage.style.display = 'block';
        extremeMessage.textContent = 'Вы достигли экстремального значения';
    } else {
        plusBtn.disabled = false;
        minusBtn.disabled = false;
        extremeMessage.style.display = 'none';
    }
}

// Слушатели событий для кнопок
plusBtn.addEventListener('click', () => {
    counter++;
    resultElement.textContent = counter;
    updateBackgroundColor();
    checkExtremeValues();
});

minusBtn.addEventListener('click', () => {
    counter--;
    resultElement.textContent = counter;
    updateBackgroundColor();
    checkExtremeValues();
});

// Инициализация (вызываем функции при загрузке страницы)
updateBackgroundColor();
checkExtremeValues();
