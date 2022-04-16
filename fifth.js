/* Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),

где arg1, arg2 – значения аргументов, operation – строка с названием операции. В зависимости  от

переданного значения операции (использовать switch) выполнить одну из арифметических операций

(использовать функции из задания 4) и вернуть полученное значение.
*/
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
  };

let a = Math.round(getRandomArbitrary(-100, 100));
let b = Math.round(getRandomArbitrary(-100, 100));

function mathOperation(arg1, arg2, operation) {
    if (operation === '+') {
        return arg1+arg2;
    } else if (operation === '-'){
        return arg1-arg2;
    } else if (operation === '/') {
        return  arg1/arg2;
    } else if (operation === '*') {
        return arg1*arg2;
    } else {
        operation = prompt('Какую арифметическую функцию из представленных выполнить:*,/,+,- ?');
        return mathOperation(arg1, arg2, operation);
    }
}

let c = prompt('Какую арифметическую функцию из представленных выполнить:*,/,+,- ?')

let d = Math.round(mathOperation(a, b, c));
alert (d)
