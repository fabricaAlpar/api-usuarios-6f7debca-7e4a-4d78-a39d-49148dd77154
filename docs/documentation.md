# Documentação da API de Usuários

Este é um código de API simples escrito em FastAPI para gerenciar operações CRUD (Criar, Ler, Atualizar, Excluir) em uma lista de usuários.

## Classes

### User

A classe `User` é a representação do modelo de usuário. Ela possui quatro campos:

- `id: int` - O identificador único do usuário.
- `name: str` - O nome do usuário.
- `email: str` - O endereço de email do usuário.
- `password: str` - A senha do usuário.

## Endpoints

### GET /users

Retorna uma lista de todos os usuários.

**Exemplo de uso:**

```python
response = client.get("/users")
```

### GET /users/{user_id}

Retorna um único usuário pelo ID.

**Parâmetros:**

- `user_id: int` - O identificador único do usuário.

**Exemplo de uso:**

```python
response = client.get("/users/1")
```

### POST /users

Cria um novo usuário.

**Parâmetros:**

- `user: User` - O objeto usuário a ser criado.

**Exemplo de uso:**

```python
user = {"name": "John", "email": "john@example.com", "password": "password123"}
response = client.post("/users", json=user)
```

### PUT /users/{user_id}

Atualiza um usuário existente.

**Parâmetros:**

- `user_id: int` - O identificador único do usuário.
- `user: User` - O objeto usuário com as informações atualizadas.

**Exemplo de uso:**

```python
user = {"name": "John Updated", "email": "john@example.com", "password": "password123"}
response = client.put("/users/1", json=user)
```

### DELETE /users/{user_id}

Exclui um usuário.

**Parâmetros:**

- `user_id: int` - O identificador único do usuário.

**Exemplo de uso:**

```python
response = client.delete("/users/1")
```

## Notas Importantes

- Ao atualizar e excluir um usuário, se o `user_id` fornecido não existir na lista de usuários, uma exceção `HTTPException` será levantada com o código de status 404 e uma mensagem "User not found".

## Dependências Necessárias

- FastAPI: É um framework moderno, rápido (alta performance), web framework para construir APIs com Python 3.6+ baseado em standard Python type hints.
- Pydantic: É uma biblioteca de análise de dados e serialização usando validação de Python type annotations.

Para instalar as dependências, você pode usar o pip:

```bash
pip install fastapi
pip install pydantic
```

Para executar a aplicação, você pode usar um servidor ASGI, como Uvicorn ou Hypercorn:

```bash
uvicorn main:app --reload
```