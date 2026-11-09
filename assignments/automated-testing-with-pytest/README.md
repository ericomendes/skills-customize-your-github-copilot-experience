# 📘 Assignment: Testes Automatizados com pytest

## 🎯 Objective

Aprenda a escrever testes automatizados com `pytest` para verificar funções, o comportamento de uma classe e endpoints de uma API FastAPI. Use os arquivos iniciais como código sob teste e crie os arquivos de teste correspondentes.

## 📝 Tasks

### 🛠️ Testar Funções com pytest

#### Descrição
Crie `test_school_tools.py` e escreva testes para as funções disponíveis em `school_tools.py`.

#### Requisitos
O programa concluído deve:

- Instalar `pytest` com `python -m pip install pytest`
- Verificar que `is_even()` retorna os resultados corretos para números pares e ímpares, incluindo zero
- Verificar que `calculate_average()` calcula a média de uma lista com vários valores
- Usar `pytest.raises` para confirmar que uma lista vazia causa `ValueError`
- Executar os testes com `python -m pytest -q`

### 🛠️ Testar o Comportamento de uma Classe

#### Descrição
Acrescente testes para `MileageTracker`, cobrindo seu estado inicial, uma atualização válida e a regra que impede a quilometragem de diminuir.

#### Requisitos
O programa concluído deve:

- Confirmar que um novo `MileageTracker` começa com quilometragem zero
- Confirmar que `update_mileage()` registra uma quilometragem maior
- Usar `pytest.raises` para verificar que uma quilometragem menor causa `ValueError`
- Manter cada comportamento em um teste separado com um nome descritivo

### 🛠️ Testar Endpoints com FastAPI TestClient

#### Descrição
Crie `test_api.py` e teste as rotas implementadas em `main.py` usando `TestClient`. Use uma fixture para preparar o cliente e isolar os dados entre testes.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install pytest fastapi httpx`
- Confirmar que `GET /health` retorna status `200` e `{"status": "ok"}`
- Testar a listagem vazia e a criação e consulta de uma tarefa
- Verificar `404` para uma tarefa inexistente e `422` quando a criação não inclui `title`
- Instalar `fastapi` e `httpx` com `python -m pip install fastapi httpx`
- Executar todos os testes com `python -m pytest -q`