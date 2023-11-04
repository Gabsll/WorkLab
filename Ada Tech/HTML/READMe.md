# HTML - HyperText Markup Language

HTML (Linguagem de Marcação de HiperTexto) é o bloco de construção mais básico da web. Define o significado e a estrutura do conteúdo da web. Outras tecnologias além do HTML geralmente são usadas para descrever a aparência/apresentação (CSS) ou a funcionalidade/comportamento (JavaScript) de uma página da web.

## Links uteis

[HTML - HTML Documentation](https://developer.mozilla.org/pt-BR/docs/Web/HTML)

[HTML - Estrutura do documento HTML antes e depois do HTML5](https://html.com/document/#ixzz8I2py3eJ8)

[HTML - Referencia de tags](https://www.w3schools.com/tags/default.asp)

## Introdução a HTML

HTML, que significa Hypertext Markup Language, é a linguagem fundamental da web. Foi criada por Tim Berners-Lee no início dos anos 1990 e desempenhou um papel crucial no desenvolvimento da World Wide Web. HTML é uma linguagem de marcação que permite a criação e formatação de documentos para a web. Ela define a estrutura e o conteúdo de uma página da web, permitindo a incorporação de texto, imagens, links, mídia e muito mais.

Neste contexto, o HTML atua como a espinha dorsal da internet, fornecendo a estrutura básica em que os navegadores da web interpretam e exibem o conteúdo de uma página. As páginas da web são construídas com elementos HTML, que são tags e atributos que especificam como o conteúdo deve ser apresentado. Os elementos HTML são organizados em uma hierarquia, criando uma estrutura lógica que permite aos desenvolvedores web criar sites informativos e interativos.

Nesta introdução ao HTML, exploraremos os conceitos fundamentais, incluindo as tags mais comuns, a estrutura básica de um documento HTML e como criar links e imagens. O HTML é uma linguagem essencial para qualquer pessoa que deseja criar conteúdo na web, e é o ponto de partida para o desenvolvimento web.

---

### O que é marcação em HTML?

- `marcação/marcas - > Tags`; A marcação em HTML refere-se ao processo de adicionar "marcas" ou "tags" a um documento para indicar a estrutura e o significado dos elementos dentro desse documento, Por exemplo:

 ```
<h1> As tags HTML são elementos especiais <h1>

```

Essas tags são usadas para criar um documento estruturado que pode ser interpretado e renderizado pelos navegadores da web.

As tags HTML são elementos especiais que envolvem o conteúdo de uma página da web e fornecem informações sobre como esse conteúdo deve ser exibido ou interpretado. Por exemplo, a tag `<p>` é usada para marcar parágrafos de texto, a tag `<img>` é usada para inserir imagens e a tag `<a>` é usada para criar links.

A marcação em HTML é essencial para a criação de páginas da web, pois permite que os desenvolvedores especifiquem a estrutura lógica do documento e como o conteúdo deve ser apresentado. Isso inclui a formatação do texto, a inclusão de imagens, a criação de hiperlinks, a organização de tabelas, a definição de formulários e muito mais.

A marcação em HTML é feita usando um conjunto de tags e atributos, e seguir uma estrutura específica é importante para garantir que as páginas da web sejam exibidas corretamente em diferentes navegadores. A semântica das tags é crucial, pois ajuda os motores de busca a compreender o conteúdo da página e melhora a acessibilidade para pessoas com deficiência.

No geral, a marcação em HTML é o processo de estruturar e definir o conteúdo de uma página da web por meio de tags HTML, permitindo que os navegadores interpretem e exibam o conteúdo de maneira adequada.

---

### Principais pontos ao criar marcação

Ao criar marcação em HTML, é importante considerar diversos pontos-chave para garantir que sua página da web seja bem estrutsurada, acessível e compatível com diferentes navegadores. Aqui estão os principais pontos a serem observados:

I - Estrutura Básica: Todo documento HTML deve começar com uma estrutura básica que inclui as tags `<!DOCTYPE>`,`<html>`, `<head>` e `<body>`. O `<!DOCTYPE>` define a versão do HTML, `<html>` envolve todo o documento, `<head >` contém metadados e informações sobre a página, e `<body>` contém o conteúdo visível da página.

II - Semântica: Use tags HTML de forma semântica, ou seja, escolha as tags que melhor descrevem o significado do conteúdo. Isso ajuda a tornar o conteúdo mais acessível e compreensível para os motores de busca e leitores de tela.

II - Títulos: Utilize as tags `<h1>`, `<h2>`, `<h3 >`, etc... para criar títulos e subtítulos que indicam a hierarquia de informações na página. O `<h1>` deve ser o título principal, seguido de `<h2>`, `<h3 >`, e assim por diante.

III - Parágrafos e Texto: Use a tag `<p>` para criar parágrafos de texto. Utilize as tags de formatação de texto, como `<strong>` para texto em negrito e `<em >` para texto em itálico, quando apropriado.

IV - Listas: Utilize as tags `<ul>` para listas não ordenadas e `<ol>` para listas ordenadas. Dentro dessas tags, use `<li>` para cada item da lista.

V - Links: Use a tag `<a>` para criar links. Certifique-se de incluir o atributo href com a URL de destino do link. Adicione um texto de âncora descritivo para melhorar a usabilidade.

VI - Imagens: Utilize a tag `<img>` para inserir imagens. Inclua o atributo src com o caminho para a imagem e o atributo alt com uma descrição significativa da imagem para fins de acessibilidade.

VII - Tabelas: Ao criar tabelas, use as tags `<table>`, `<thead>`, `<tbody >`, `<tr>` para definir a estrutura da tabela e `<th>` para cabeçalhos de coluna. As células de dados devem ser marcadas com `<td>`. Evite o uso excessivo de tabelas para layout.

VIII - Formulários: Utilize as tags `<form>` para criar formulários. Inclua elementos como `<input>`, `<textarea>`, `<select>` e `<button>` para coletar informações dos usuários. Associe rótulos apropriados aos campos de entrada usando a tag `<label>`.

IX - Comentários: Você pode adicionar comentários ao código HTML usando <!-- para iniciar o comentário e --> para encerrá-lo. Isso é útil para documentar o código e fazer anotações para outros desenvolvedores.

X - Validação: Verifique sempre se o seu código HTML é válido, ou seja, está em conformidade com os padrões estabelecidos pelo W3C. Você pode usar ferramentas online de validação HTML para isso.

Teste em Diferentes Navegadores: Certifique-se de que sua marcação funcione corretamente em diferentes navegadores, garantindo uma experiência consistente para os usuários.

Ao seguir esses pontos-chave ao criar marcação HTML, você estará no caminho certo para criar páginas da web bem estruturadas, acessíveis e compatíveis com os padrões da web. Isso resultará em uma melhor experiência para os usuários e uma maior facilidade de manutenção do seu código.

## Aprendendo a usar HTML

[1 - O que e uma IDE?](1_O_que_é_uma_IDE.md)
[2 - Criando a primeira pagina em HTML](Criando_a_primeira_pagina_em_HTML.md)
