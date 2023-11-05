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

##### `<head> e <title>`

`<head>` contém informações sobre a página, como o título. A tag `<title>` define o título da página, que aparece na aba do navegador.

```
<head>
  <title>Minha Página</title>
</head>

```

#### `<meta> e <link>`

A tag `<meta>` define metadados, ou seja, informações sobre dados de um documento HTML. As `<meta>` tags vão dentro do elemento `<head>` e são usadas para especificar o conjunto de caracteres, o autor do documento, as configurações da janela de visualização etc.

A tag `<link>`é uma tag vazia, que contém apenas atributos e faz a relação do documento HTML com recursos externos, é comumente usado para vincular uma folha de estilo externa, como outros recursos.

#### `<style>`

A tag `<style>` é usada para declarar estilos (CSS) para um documento.

## Criando elementos em uma pagina HTML

### Titulos

 `<h1>, <h2>, <h3>, <h4>, <h5>, e <h6>`: Essas tags são usadas para criar títulos de diferentes níveis.

 ```
<h1>Título de Nível 1</h1>
<h2>Título de Nível 2</h2>
<h3>Título de Nível 3</h3>
 ```

### parágrafos

 `<p>`: A tag <p> é usada para criar parágrafos de texto.

 ```
 <p>Este é um parágrafo de exemplo.</p>

 ```

### Criando links para outras paginas

 `<a>`:A tag <a> cria links para outras páginas da web.

 ```
 <a href="https://www.exemplo.com">Visite o Exemplo.com</a>

 ```

### Inserindo imagens

 `<img>`:A tag <img> insere imagens na página.

 ```
 <img src="imagem.jpg" alt="Imagem de Exemplo">

 ```

### Listas

`<ul>, <ol>, <li>:`

`<ul>` cria listas não ordenadas.
`<ol>` cria listas ordenadas.
`<li>` define os itens da lista.

```
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

<ol>
  <li>Primeiro</li>
  <li>Segundo</li>
  <li>Terceiro</li>
</ol>

```

### Formularios, botões e campos de entrada

 `<form>, <input>, <button>`:

`<form>` cria formulários.
`<input>` cria campos de entrada, como caixas de texto.
`<button>` cria botões.

```
<form>
  <label for="nome">Nome:</label>
  <input type="text" id="nome" name="nome">
  <button type="submit">Enviar</button>
</form>

```

### A tag `<span>` e a tag `<div>` são ambas elementos HTML usados para agrupar conteúdo ou aplicar estilos, mas existem algumas diferenças importantes entre elas

Inline vs. Block-Level: A tag `<span>` é um elemento de nível inline, o que significa que ela não cria uma quebra de linha e é usada para agrupar conteúdo dentro de uma linha de texto. Por outro lado, a tag `<div>` é um elemento de nível de bloco, o que significa que ela cria uma quebra de linha antes e depois do conteúdo agrupado, geralmente sendo usada para criar blocos de conteúdo independentes.

Uso típico: A tag `<span>` é geralmente usada para aplicar estilos, atributos ou marcações a uma parte específica do texto dentro de um elemento de texto, como um parágrafo. A tag `<div>`, por outro lado, é frequentemente usada para agrupar e organizar blocos de conteúdo, como seções de uma página.

Estilo padrão: A tag `<span>` não possui estilo padrão associado a ela, enquanto a tag `<div>` normalmente tem um estilo de bloco com quebras de linha antes e depois do conteúdo agrupado.

Em resumo, embora ambas as tags sejam usadas para agrupar conteúdo, elas têm finalidades diferentes e são aplicadas em contextos diferentes. A tag `<span>` é usada para agrupar conteúdo em linha e aplicar estilos a partes específicas do texto, enquanto a tag `<div>` é usada para criar blocos de conteúdo independentes e estruturar o layout da página.

`Exemplo usando <span>`:

```
<p>Este é um parágrafo de texto. <span style="color: red;">Este texto está em vermelho.</span> E este é o restante do parágrafo.</p>

Neste exemplo, a tag <span> é usada para aplicar a cor vermelha apenas ao texto contido dentro dela.

```

`Exemplo usando <div>`:

```
<div style="background-color: lightblue; padding: 10px;">
  <h2>Este é um cabeçalho em um bloco div</h2>
  <p>Este é um parágrafo dentro do bloco div.</p>
</div>

Neste exemplo, a tag <div> é usada para criar um bloco de conteúdo que tem um fundo azul claro e espaço de preenchimento. O bloco <div> agrupa o cabeçalho e o parágrafo dentro dele.

```

Lembre-se de que esses são exemplos simples, e tanto a tag `<span>` quanto a tag `<div>` são frequentemente usadas em combinação com estilos CSS mais complexos e estrutura de página para criar layouts e estilos personalizados em páginas da web.
