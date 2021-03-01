const calculator = {
    plus: function (num1, num2) {
        return num1 + num2;
    },
    minus: function (num1, num2) {
        return num1 - num2;
    },
    multiply: function (num1, num2) {
        return num1 * num2;
    },
    divide: function (num1, num2) {
        return num1 / num2;
    },
    remainder: function (num1, num2) {
        return num1 % num2;
    },
    powerOf: function (num1, num2) {
        return num1 ** num2;
    }
}

console.log(
    calculator.plus(9, 4),
    calculator.minus(9, 4),
    calculator.multiply(9, 4),
    calculator.divide(9, 4),
    calculator.remainder(9, 4),
    calculator.powerOf(9, 4)
)