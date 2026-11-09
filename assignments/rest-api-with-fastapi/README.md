# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Você vai praticar rotas HTTP, validação de dados e operações CRUD (criar, consultar, atualizar e excluir) com uma coleção mantida em memória.

## 📝 Tarefas

### 🛠️ Criar a aplicação e consultar tarefas

#### Descrição
Prepare e execute a aplicação FastAPI. Crie rotas para verificar se a API está disponível e para consultar as tarefas cadastradas.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI que possa ser iniciada com `uvicorn main:app --reload`
- Implementar `GET /health`, retornando `{"status": "ok"}`
- Implementar `GET /tasks`, retornando uma lista de tarefas (vazia quando não houver tarefas)
- Exibir e permitir testar as rotas pela documentação interativa em `/docs`

### 🛠️ Criar e consultar uma tarefa

#### Descrição
Permita que clientes enviem uma tarefa nova e consultem uma tarefa específica pelo seu identificador. Use modelos Pydantic para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` com `title` obrigatório e `description` opcional
- Atribuir um identificador único e definir `completed` como `false` ao criar uma tarefa
- Retornar a tarefa criada com status HTTP `201 Created`
- Implementar `GET /tasks/{task_id}` e retornar `404 Not Found` quando o identificador não existir

### 🛠️ Atualizar, excluir e filtrar tarefas

#### Descrição
Complete as operações CRUD adicionando atualização e exclusão. Acrescente também um filtro para consultar tarefas pelo estado de conclusão.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar o título, a descrição e o estado de conclusão de uma tarefa existente
- Implementar `DELETE /tasks/{task_id}` e retornar `404 Not Found` quando o identificador não existir
- Aceitar um parâmetro opcional `completed` em `GET /tasks` para filtrar tarefas, por exemplo, `GET /tasks?completed=true`
- Retornar status HTTP apropriados e demonstrar as rotas com a documentação em `/docs`

## 🚀 Como começar

1. Instale as dependências: `pip install fastapi uvicorn`
2. Baixe o arquivo **Código inicial** e salve-o como `main.py`
3. Execute `uvicorn main:app --reload`
4. Abra `http://127.0.0.1:8000/docs` para testar a API

> Os dados ficam em memória e são reiniciados quando a aplicação é encerrada. Não é necessário configurar um banco de dados para esta atividade.
