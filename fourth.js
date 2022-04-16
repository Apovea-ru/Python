/* 4. Реализовать основные 4 арифметические операции (+, -, /, *)  в виде функций с

двумя параметрами. Т.е. например, функция для сложения должна принимать два числа,

складывать их и возвращать результат. Обязательно использовать оператор return.
*/

function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
  };

let a = Math.round(getRandomArbitrary(-100, 100));
let b = Math.round(getRandomArbitrary(-100, 100));

function OperationWithNumbers(number1, number2, operationwithnumbers) {
    if (operationwithnumbers === '+') {
        alert (number1+number2);
    } else if (operationwithnumbers === '-'){
        alert (number1-number2);
    } else if (operationwithnumbers === '/') {
        alert (number1/number2);
    } else if (operationwithnumbers === '*') {
        alert (number1*number2)
    } else {
        operationwithnumbers = prompt('Какую арифметическую функцию из представленных выполнить:*,/,+,- ?');
        OperationWithNumbers(number1, number2, operationwithnumbers);
    }
}

let c = prompt('Какую арифметическую функцию из представленных выполнить:*,/,+,- ?')

OperationWithNumbers(a, b, c);
