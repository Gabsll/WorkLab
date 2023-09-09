//Escopo, defini a limitação e visibilidaed de um bloco de codigo.
//Escopo Global - Quando uma variavel é definidade fora de um bloco, sua visibilidade é disponivel em todo o codigo.

var escopoGlobal = 'Global';
console.log(escopoGlobal)

//Escopo loval - Ao declarar uma variavel dentro de um bloco, a variavel se torna visivel ou não.



function escopoLocal() {
    let escopoLocalInterno = 'local';
    console.log(escopoLocalInterno)
}

//console.log(escopoLocal)
escopoLocal()