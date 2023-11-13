# CRUD-in-Python



Este é um repositório contendo um código-fonte em Python para um sistema de gerenciamento de contatos. O sistema permite realizar as seguintes operações:

* Inserir novos contatos;
* Pesquisar contatos por nome, cidade ou ID;
* Atualizar dados de contatos existentes;
* Deletar contatos.

## Pré-requisitos

Para rodar o sistema, é necessário ter instalado o Python 3 e o banco de dados SQLite3.

## Instalação

Para instalar o sistema, basta clonar este repositório e executar o seguinte comando:

```python
pip install -r requirements.txt
Use o código com cuidado. Saiba mais
Uso
Para iniciar o sistema, execute o seguinte comando:

Python
main.py
Use o código com cuidado. Saiba mais
Uma vez iniciado, o sistema irá apresentar um menu com as seguintes opções:

1 - Inserir
2 - Pesquisar
3 - Atualizar
4 - Deletar
5 - Sair


Para realizar uma operação, basta selecionar a opção correspondente no menu e seguir as instruções.

### Inserir novo contato

Para inserir um novo contato, selecione a opção "Inserir" no menu e informe os seguintes dados:

* Nome;
* Rua;
* Cidade;
* Telefone.

Após informar todos os dados, pressione a tecla "Enter" para confirmar a inserção do contato.

### Pesquisar contato

Para pesquisar um contato, selecione a opção "Pesquisar" no menu e informe o seguinte critério de pesquisa:

* Nome;
* Cidade;
* ID.

Após informar o critério de pesquisa, pressione a tecla "Enter" para listar todos os contatos que atendem ao critério informado.

### Atualizar contato

Para atualizar um contato, selecione a opção "Atualizar" no menu e informe o ID do contato que deseja atualizar. Após informar o ID, o sistema irá solicitar que você informe os novos dados do contato.

### Deletar contato

Para deletar um contato, selecione a opção "Deletar" no menu e informe o ID do contato que deseja deletar. Após informar o ID, o sistema irá solicitar a confirmação da operação de deleção.
