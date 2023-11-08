# Introdução ao CSS (Cascading Style Sheets)

O CSS (Cascading Style Sheets) é uma linguagem de estilo utilizada para controlar a apresentação e o layout de documentos HTML. Ele desempenha um papel fundamental no design de páginas da web, permitindo que você defina a aparência visual dos elementos HTML, como cores, fontes, espaçamento e posicionamento. O CSS é separado do HTML, o que significa que você pode aplicar estilos a várias páginas HTML a partir de um único arquivo CSS, facilitando a manutenção e a consistência de design em todo o site.

## `Relação entre CSS e HTML`: O CSS e o HTML estão intimamente relacionados, e juntos eles formam a estrutura de uma página da web. O HTML é responsável pela estrutura e conteúdo da página, enquanto o CSS é responsável pelo estilo e aparência

Aqui está como eles se relacionam:

- `Seletores e Propriedades`: No CSS, você usa seletores para direcionar elementos HTML específicos e, em seguida, aplica propriedades de estilo a esses elementos. Por exemplo, você pode usar um seletor para selecionar todos os elementos `<p>` (parágrafos) em seu documento HTML e, em seguida, definir propriedades, como cor e tamanho de fonte, para esses elementos.

- `Ligação entre CSS e HTML`: Para vincular um arquivo CSS a um documento HTML, você usa a tag `<link>` no cabeçalho do HTML ou o atributo style diretamente em um elemento HTML. O arquivo CSS contém as regras de estilo que serão aplicadas aos elementos HTML.

### `Exemplos de CSS em HTML`

`Exemplo 1`: Vinculando um arquivo CSS externo a um documento HTML.

`HTML (index.html)`:

```

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <h1>Exemplo de CSS</h1>
    <p>Este é um parágrafo com estilo aplicado por um arquivo CSS externo.</p>
</body>
</html>

```

`CSS (styles.css)`:

```

/* Estilo para o título h1 */
h1 {
    color: blue;
    font-size: 24px;
}

/* Estilo para parágrafos */
p {
    color: green;
    font-size: 16px;
}

```

Neste exemplo, o arquivo CSS externo styles.css é vinculado ao documento HTML e define estilos para o título (`<h1>`) e parágrafos (`<p>`).

## `Separação de Conteúdo e Estilo`

Uma das vantagens do CSS é a separação clara entre o conteúdo (HTML) e o estilo (CSS). Isso permite que os desenvolvedores organizem e mantenham seus projetos de forma mais eficiente.

### `Estrutura Básica do CSS`

As regras CSS consistem em seletores e declarações de estilo.
Um seletor identifica os elementos HTML que receberão o estilo.
As declarações contêm propriedades e valores que definem o estilo. Por exemplo:

```
h1 {
    color: blue;
    font-size: 24px;
}
```

- `Seletores CSS`:

Os seletores podem ser simples, como h1, que seleciona todos os elementos `<h1>`, ou mais complexos, usando classes, IDs, e outros atributos para selecionar elementos específicos.

Exemplos de seletores:

`.classe`: para elementos com uma classe específica.

`#id`:  para um elemento com um ID específico.

`elemento[pseudo-classe]`: para selecionar elementos com base em estados, como `:hover`.

### Propriedades e Valores

O CSS define propriedades (como color, font-size, margin, etc.) e seus valores para estilizar elementos HTML. Existem muitas propriedades CSS, que afetam desde cores e fontes até layout e animações.

- `Cascata e Especificidade`: O termo "Cascading" no nome CSS refere-se ao sistema de cascata, que define como os estilos são aplicados e priorizados. A "Especificidade" refere-se a quão específico é um seletor. Estilos aplicados por seletores mais específicos têm maior prioridade.

- `Herança de Estilos`: Alguns estilos são herdados por elementos filhos de seus elementos pai. Por exemplo, a cor do texto definida no `<body>` pode afetar todos os elementos filhos, a menos que sejam especificamente substituídos.

- `Mídia e Responsividade`: CSS também é usado para criar layouts responsivos, adaptando a aparência de uma página a diferentes tamanhos de tela e dispositivos. As "Media Queries" são usadas para aplicar estilos específicos com base em características do dispositivo, como largura da tela.
Transições e Animações:

O CSS permite criar transições suaves e animações de elementos, adicionando interatividade e tornando as páginas da web mais dinâmicas.
