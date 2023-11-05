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

Resultado:

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

### Estrutura basica

#### `<!DOCTYPE html>`

 É uma declaração que define o tipo de documento HTML que o navegador deve esperar. Ela não é uma tag HTML, mas uma instrução do tipo de documento.

Esta declaração é o que chamamos de "Document Type Declaration" (DTD) e informa ao navegador que o documento HTML está seguindo o padrão HTML5. Ela deve ser a primeira linha do seu documento HTML e é importante para garantir que o navegador interprete o código corretamente.

#### `<html> e <body>`

A tag `<html>` é o elemento raiz de um documento HTML, que engloba todo o conteúdo.
A tag `<body>` contém o conteúdo visível da página.

#### `<script> e <head>`

A tag `<script>` contém instruções de script ou aponta para um arquivo de script externo por meio do atributo src.

A tag `<head>` Compreende as informações do documento que serão interpretadas pelo navegador (metadados). Como por exemplo, título do documento, links para folhas de estilo etc.

#### `<meta> e <link>`

A tag `<meta>` define metadados, ou seja, informações sobre dados de um documento HTML. As `<meta>` tags vão dentro do elemento `<head>` e são usadas para especificar o conjunto de caracteres, o autor do documento, as configurações da janela de visualização etc.

A tag `<link>`é uma tag vazia, que contém apenas atributos e faz a relação do documento HTML com recursos externos, é comumente usado para vincular uma folha de estilo externa, como outros recursos.

#### `<style>`

a tag `<style>` é usada para declarar estilos (CSS) para um documento.
