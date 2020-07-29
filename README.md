# Medicações do Usuário

Este é um simples projeto feito em Django simulando o cadastro de medicamentos de um usuário.

Esse conta com um CRUD completo em relação aos medicamentos (CREATE, READ, UPDATE and DELETE) e uma funcionalidade de
login, provendo o token de autenticação de um usuário específico já cadastrado (funcionalidade de cadastro de usuários
feito exclusivamente pelo django admin).

## Como Executar

Siga a lista de comandos abaixo para organizar todas as necessidades e fazer com que a aplicação execute.</br>

Obs.: Este projeto foi criado utilizando o python 3.8. Sugiro que o utilize para evitar conflitos que possam acontecer a partir do versionamento dos pacotes. </br>

```text
1. Crie o ambiente virtual do projeto: python3 -m venv venv
2. Ative-o: source venv/bin/activate
3. Instale suas dependências: pip3 install -r requirements.txt
4. Crie o banco de dados executando as migrations: python3 manage.py migrate
5. Crie um usuário primário: python3 manage.py createsuperuser
6. Inicie o Servidor: python3 manage.py runserver
```
E pronto, a aplicação estará executando de forma local na porta 8000.

## Objetos

Abaixo estão listadas a estrutura de cada objeto contido na aplicação (usuário/login e medicamento).

Credenciais de Autenticação (corpo da requisição para autenticação):

```json
{
  "username": "nome de usuário",
  "password": "senha do usuário"
}
```

Usuaŕio (retorno da requisição para realizar login):
```json
{
  "auth_token": "token de autenticação",
  "user": {
    "id": 0,
    "nome": "nome do usuário (apresentando o first name concatenado ao last name do usuário)"
  },
  "created": "a data de quando o usuário foi criado no formato yyyy-mm-ddThh:mm:ss:mmmmmmZ"
}
```

Medicamento
```json
{
  "id": 0 // id do medicamento,
  "user_id": 0, // id do usuário, dono do medicamento
  "nome": "nome do medicamento - obrigatório",
  "descricao": "descrição do medicamento - facultativo",
  "validade": "data de validade do medicamento no formato yyyy-mm-dd - obrigatório",
  "created_at": "data de criação do medicamento no formato yyyy-mm-dd - criado automaticamente"
}
```

Obs.: Em relação ao retorno dos medicamentos, quando utilizada uma rota geral (index), requisitando todos os
medicamentos de um único usuário, ao invés de um objeto, irá retornar uma lista de medicamentos, ou seja, irá
ter retorno na seguinte estrutura:
```json
[
  {
    "id": 1 // id do medicamento,
    "user_id": 0, // id do usuário, dono do medicamento
    "nome": "nome do medicamento - obrigatório",
    "descricao": "descrição do medicamento - facultativo",
    "validade": "data de validade do medicamento no formato yyyy-mm-dd - obrigatório",
    "created_at": "data de criação do medicamento no formato yyyy-mm-dd - criado automaticamente"
  },
  {
    "id": 2 // id do medicamento,
    "user_id": 0, // id do usuário, dono do medicamento
    "nome": "nome do medicamento - obrigatório",
    "descricao": "descrição do medicamento - facultativo",
    "validade": "data de validade do medicamento no formato yyyy-mm-dd - obrigatório",
    "created_at": "data de criação do medicamento no formato yyyy-mm-dd - criado automaticamente"
  },
  ...
]
```

## Rotas da API

Como dito anteriormente, no projeto são utilizadas duas estruturas de objeto: a de autenticação, retornando os dados
do usuário (id e nome) junto ao token do mesmo, e do medicamento considerando todos os atributos colocados acima.

Primeiro, abaixo se apresenta uma tabela que consta com rotas relacionadas á autenticação. Neste caso, só existe
uma única rota: a de autenticação (login):

| Método | Nome   | Rota                                      |
|--------|--------|-------------------------------------------|
| POST   | Login  | http://localhost:8000/api/accounts/login  |

Por último, abaixo se apresenta uma tabela que consta com rotas relacionadas à operações com os medicamentos dos
usuários:

| Método | Nome   | Rota                                                      | Descrição                                                                                                                                                                             |
|--------|--------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GET    | Index  | http://localhost:8000/api/core/users/:user_id/medications | Listar todos os medicamentos do usuário cujo id foi fornecido no lugar de ```:user_id```.                                                                                             |
| GET    | Show   | http://localhost:8000/api/core/medications/:medication_id | Retornar um único medicamento de acordo com seu id (fornecido no lugar de ```:medication_id```).                                                                                      |
| POST   | Add    | http://localhost:8000/api/core/medications                | Adicionar um medicamento com o envio dos dados seguindo a estrutura do objeto apresentado.                                                                                            |
| PUT    | Edit   | http://localhost:8000/api/core/medications/:medication_id | Editar um medicamento com o envio dos dados do medicamento seguindo a estrutura do objeto apresentado e com o id do medicamento existente fornecido no lugar de ```:medication_id```. |
| DELETE | Delete | http://localhost:8000/api/core/medications/:medication_id | Excluir um medicamento existente, cujo id deve ser fornecido no lugar de ```:medication_id```.
