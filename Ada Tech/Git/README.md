# Git

# Links uteis

[Git - git Documentation](https://git-scm.com/docs/git/pt_BR)

---

## Git Comando

Existem diversos comandos no Git, mas alguns dos principais são:

- `git init`: inicia um novo repositório Git
- `git clone`: cria uma cópia de um repositório Git existente
- `git add`: adiciona arquivos ao índice do Git para serem commitados
- `git commit`: salva as alterações no repositório local
- `git push`: envia as alterações para um repositório remoto
- `git pull`: obtém as atualizações do repositório remoto e mescla com o repositório local
- `git branch`: cria, lista ou exclui branches (ramificações) do repositório
- `git merge`: mescla as alterações de uma branch com outra
- `git status`: verifica o estado atual do repositório e dos arquivos
- `git log`: exibe um histórico de commits do repositório

Existem muitos outros comandos e opções no Git, mas esses são alguns dos mais comuns e úteis para começar a utilizar o sistema de controle de versões.

## Exemplos de Comandos do Git

### `git init`

Para iniciar um novo repositório Git, basta executar o comando `git init` no diretório que deseja tornar um repositório. Por exemplo:

```
$ cd my-project
$ git init

```

### `git clone`

Para criar uma cópia de um repositório Git existente, utilize o comando `git clone`, seguido da URL do repositório. Por exemplo:

```
$ git clone <https://github.com/user/repo.git>

```

### `git add`

Para adicionar arquivos ao índice do Git, utilize o comando `git add`, seguido do nome do arquivo. Por exemplo:

```
$ git add index.html

```

### `git commit`

Para salvar as alterações no repositório local, utilize o comando `git commit`, seguido de uma mensagem de commit. Por exemplo:

```
$ git commit -m "Adiciona arquivo index.html"

```

### `git push`

Para enviar as alterações para um repositório remoto, utilize o comando `git push`, seguido do nome do repositório remoto e da branch que deseja enviar. Por exemplo:

```
$ git push origin main

```

### `git pull`

Para obter as atualizações do repositório remoto e mesclá-las com o repositório local, utilize o comando `git pull`, seguido do nome do repositório remoto e da branch que deseja obter. Por exemplo:

```
$ git pull origin main

```

### `git branch`

Para criar uma nova branch no repositório, utilize o comando `git branch`, seguido do nome da nova branch. Por exemplo:

```
$ git branch feature-branch

```

### `git merge`

Para mesclar as alterações de uma branch com outra, utilize o comando `git merge`, seguido do nome da branch que deseja mesclar. Por exemplo:

```
$ git merge feature-branch

```

### `git status`

Para verificar o estado atual do repositório e dos arquivos, utilize o comando `git status`. Por exemplo:

```
$ git status

```

### `git log`

Para exibir um histórico de commits do repositório, utilize o comando `git log`. Por exemplo:

$ git log