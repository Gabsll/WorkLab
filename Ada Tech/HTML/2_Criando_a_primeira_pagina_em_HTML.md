# Primeira pagina de HTML

## Vscode: Dicas de extensões

O Visual Studio Code (VS Code) é uma ferramenta altamente extensível, e você pode adicionar extensões para aprimorar sua experiência de desenvolvimento de HTML. Abaixo, listo algumas das extensões populares e úteis para trabalhar com HTML no VS Code:

```
Passo 1: Acessar a Galeria de Extensões

Na barra lateral esquerda, clique no ícone que se parece com uma caixa de quebra-cabeça, que é a "Galeria de Extensões" (ou use o atalho Ctrl+Shift+X no Windows/Linux ou Cmd+Shift+X no macOS).

Passo 2: Pesquisar e Instalar Extensões

Na barra de pesquisa no topo, digite o nome da extensão que você deseja instalar ou uma palavra-chave relacionada. Por exemplo, você pode pesquisar por "HTML" se estiver procurando extensões relacionadas a HTML.

Aparecerão várias extensões relacionadas à sua pesquisa. Clique em uma extensão específica para ver mais detalhes.

Na página de detalhes da extensão, clique no botão "Instalar" para instalar a extensão.
```

- `Auto Close Tag`: Fecha automaticamente as tags HTML assim que você as abre, economizando tempo na digitação.

- `Auto Rename Tag`: Atualiza automaticamente o par de abertura/fechamento de uma tag quando você renomeia um deles.

- `Prettier - Code Formatter`: Formata automaticamente o código HTML (e também CSS e JavaScript) para um estilo consistente.

- `TML Snippets`: Fornece uma série de snippets (fragmentos de código) para tags HTML comuns, economizando tempo na digitação.

- `Live Server`: Uma das extensões obrigatórias para quem trabalha com front-end através do Visual Studio Code. Sabe aquele projeto html, css e javascriptque quando precisamos ver as alterações que fizemos no código damos refresh no navegador para ver o resultado? Esse plugin cria um localhost da aplicação e toda alteração que é salva no projeto, é atualizada automaticamente, evitando dar refresh na página a cada modificação no código feita. Assim que instalado, é só clicar no botão Go Live e o localhost será aberto no seu navegador padrão.

- `Visual Studio IntelliCode`:É uma extensão que utliza a inteligência artifical e o contexo do seu código para criar, e te oferecer autocompletes referentes ao código que está escrevendo e acelerando o desenvolvimento do seu projeto.

## Os principais elementos do HTML

O HTML é composto por uma variedade de elementos, que são tags e atributos usados para estruturar e formatar o conteúdo de uma página da web. Aqui estão alguns dos elementos HTML mais comuns:

- `<!DOCTYPE>:` Define a versão do HTML sendo usada e a declaração de tipo de documento.

- `<html>`: Envolve todo o conteúdo da página.

- `<head>`: Contém metadados, como o título da página e informações sobre a codificação de caracteres.

- `<meta>`: Define metadados, como a codificação de caracteres da página.

- `<title>`: Define o título da página, que é exibido na guia do navegador.

- `<link>`: Liga o documento a arquivos externos, como folhas de estilo CSS.

- `<script>`: É usado para incluir código JavaScript na página.

- `<style>`: Permite definir estilos CSS diretamente na página.

- `<body>`: Contém o conteúdo visível da página, como texto, imagens, links e outros elementos.

- `Cabeçalhos (<h1>, <h2>, <h3>, etc.)`: São usados para definir títulos e subtítulos, com `<h1>` sendo o título principal e `<h2>`, `<h3>`, etc., para hierarquias menores.

- `<p>`: Define parágrafos de texto.

- `<a>`: Cria hiperlinks para outras páginas ou recursos.

- `<img>`: Insere imagens na página.

- `Listas (<ul>, <ol>, <li>)`: São usadas para criar listas não ordenadas `(<ul>)` e listas ordenadas `(<ol>)`, com os elementos `<li>` representando os itens da lista.

- `<table>`: Define uma tabela, com elementos como `<thead>`, `<tbody>`, `<tr>`, `<th>`, e `<td>` usados para organizar o conteúdo da tabela.

- `<form>`: Cria um formulário interativo que permite a entrada de dados do usuário.

- `<input>`: Define campos de entrada, como caixas de texto, botões de opção e caixas de seleção, dentro de um formulário.

- `<textarea>`: Cria uma área de texto multilinha em um formulário.

- `<button>`: Cria botões interativos em formulários.

- `<div> e <span>`: São elementos de contêiner usados para agrupar outros elementos HTML e aplicar estilos ou scripts a eles.

- `<hr>`: Cria uma linha horizontal para separar o conteúdo.

- `<br>`: Insere uma quebra de linha.

Estes são apenas alguns dos elementos HTML mais comuns. Existem muitos outros elementos e atributos disponíveis no HTML, e a combinação deles permite criar páginas da web ricas e interativas. A escolha dos elementos e sua estrutura depende do tipo de conteúdo que você deseja criar.

## Dando os primieros passos em HTML

### Crie uma extensão ".html"

No vscode crie um novo arquivo e salve-o com a extensão ".html". Por exemplo, você pode nomeá-lo como "index.html".
![Clique com o lado direito do mause e clique em criar novo arquivo](Criando_um_arquivo_httml_1.png)

![ crie uma extenção ".html". Pode nomeá-lo como "index.html"](Criando_um_arquivo_html_2.png)

### Estrutura Básica do HTML

Agora, adicione a estrutura básica do HTML ao seu arquivo "index.html". Aqui está um exemplo simples:

```
<!DOCTYPE html>
<html>
<head lang="pt-br">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Primeira Página HTML</title>
</head>
<body>
    <h1>Olá, Mundo!</h1>
    <p>Esta é a minha primeira página HTML.</p>
</body>
</html>

```

#### Iniciar o Live Server

Com o arquivo "index.html" aberto no VS Code, clique com o botão direito do mouse no arquivo no painel de navegação à esquerda.

Selecione "Abrir com o Live Server" a partir das opções.

Isso iniciará o Live Server e abrirá automaticamente o seu navegador padrão com a página HTML. Qualquer alteração que você fizer no arquivo HTML será refletida em tempo real no navegador, graças ao Live Server.

Agora você deve ver a sua primeira página HTML no navegador. Você pode fazer alterações no código HTML e ver as atualizações imediatamente no navegador, sem a necessidade de recarregar manualmente a página.

Este é um método conveniente para desenvolver e testar páginas da web em tempo real. A partir daqui, você pode continuar a aprender HTML, CSS e JavaScript para criar páginas mais avançadas e interativas.
