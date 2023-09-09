//https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array
// Vetores ou Arrays -  São um tipo de lista, ou matriz de variaveis onda cada variavel possui um indice(os valores podem ser de varios tipos)
let array = ['string', 'number', 1, true, 2 , 3, 5 ,6 , 7];
console.log(array) ;

// Um array pode conter outro array.
let arrayInArray = ['um', 2 , ['Array', 1, 2, [3, 4, 5]]];
console.log(arrayInArray);

// Manipulando Arrays
// metodo > forEach() - itera um array;

array.forEach(function(item, index){console.log(item, index)});

// metodo > push() aiciona um item no final do array.
array.push("Novo item");
console.log(array);

// metodo > pop() - retira um item no final do array
array.pop();
console.log(array);

// metodo > shift() - remove um item no inicio do array.
array.shift();
console.log(array);

// metodo > ubshift() - adiciona um item no inicio do array.
array.unshift('Novo item');
console.log(array);

// metodo > indexOf() - retorna o index de um valor
console.log(array.indexOf(true));

// metodo > splice() - remove ou substitui um item pelo indice;
array.splice(0, 3);
console.log(array);

//metodo > slice() - retorna uma parte de um array existente. 
let novoAray = array.slice(0, 4)
console.log(array)


