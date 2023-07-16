let number1 = 3;
let number2 = 2;
let soma = number1 + number2;
if (soma % 2 === 0 && number1 && number2 % 2 !== 0) {
    console.log("Numeros são impar: " + number1 + ", " + number2)
    console.log("Soma é par: " + soma)
} else if (number1 && number2 && soma % 2 === 0) {
    console.log("Numeros são Par: " + number1 + ", " + number2)
    console.log("Soma é par: " + soma)
} else if (number1 && soma % 2 === 0 && number2 % 2 !== 0) {
    console.log("Par: " + number1)
    console.log("impar: " + number2)
    console.log("Soma é par: " + soma)
} else if (number1 % 2 === 0 && number2 && soma % 2 !== 0) {
    console.log("Par: " + number1)
    console.log("impar: " + number2)
    console.log("Soma é impar: " + soma)
} else if (number2 % 2 === 0 && number1 && soma % 2 !== 0) {
    console.log("Par: " + number2)
    console.log("impar: " + number1)
    console.log("Soma é impar: " + soma)
} else {

    console.log("Numeros são impar: " + number1 + ", " + number2)
    console.log("Soma é impar: " + soma)
};
;