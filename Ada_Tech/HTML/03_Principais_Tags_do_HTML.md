# Principais Tags do HTML

As tags HTML são elementos usados para estruturar e formatar o conteúdo de uma página da web. Cada tag é geralmente composta por uma tag de abertura e uma tag de fechamento. Aqui está uma explicação curta sobre esses conceitos:

Tag de Abertura: É a primeira parte de uma tag e indica o início de um elemento HTML. Geralmente é escrita com o nome da tag entre < e >, por exemplo `<p>` para parágrafos ou `<a>` para links.

Tag de Fechamento: É a segunda parte da tag e marca o final do elemento HTML. A tag de fechamento é semelhante à tag de abertura, mas inclui uma barra antes do nome da tag, por exemplo `</p>` para parágrafos ou `</a>` para links.

Exemplo de uso de uma tag com abertura e fechamento:

```
<p>Este é um parágrafo de exemplo.</p>
```

Algumas tags, como `<img>` para imagens, não têm uma tag de fechamento, pois são tags autocontidas que não possuem conteúdo interno. É importante lembrar de fechar as tags corretamente para que o navegador interprete o código HTML da maneira desejada e a página seja exibida conforme planejado.

## Estrutura básica

O VS Code utiliza por padrão o Emmet Abbreviations, que traz o aparecimento automático de linhas de código que fazem parte da estrutura básica do HTML ao digitar o ponto de exclamação. Dessa forma:

```
Digite: !

logo em seguida precione TAB

```

Resuktando:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>

```

### `<html> e <body>`

A tag `<html>` é o elemento raiz de um documento HTML, que engloba todo o conteúdo.
A tag `<body>` contém o conteúdo visível da página.
