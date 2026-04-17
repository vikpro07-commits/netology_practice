"""
Автотесты для сервиса PostmanEcho (https://postman-echo.com)
Проверяют поведение GET и POST эндпоинтов с разными типами запросов.
"""

import pytest
import requests

BASE_URL = "https://postman-echo.com"


# ─────────────────────────────────────────────
# Тест 1: GET-запрос без параметров
# ─────────────────────────────────────────────
def test_get_no_params():
    """GET /get без query-параметров: статус 200, args пустой."""
    response = requests.get(f"{BASE_URL}/get")

    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}"
    )

    body = response.json()
    assert "args" in body, "В ответе отсутствует поле 'args'"
    assert body["args"] == {}, f"Ожидался пустой args, получено: {body['args']}"


# ─────────────────────────────────────────────
# Тест 2: GET-запрос с query-параметрами
# ─────────────────────────────────────────────
def test_get_with_query_params():
    """GET /get с параметрами: сервер отражает их в 'args'."""
    params = {"foo": "bar", "city": "Moscow"}
    response = requests.get(f"{BASE_URL}/get", params=params)

    assert response.status_code == 200

    body = response.json()
    assert body["args"]["foo"] == "bar", "Параметр 'foo' не совпадает"
    assert body["args"]["city"] == "Moscow", "Параметр 'city' не совпадает"


# ─────────────────────────────────────────────
# Тест 3: POST-запрос с JSON-телом
# ─────────────────────────────────────────────
def test_post_json_body():
    """POST /post с JSON: сервер отражает тело в 'json'."""
    payload = {"username": "tester", "age": 25}
    response = requests.post(f"{BASE_URL}/post", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert "json" in body, "В ответе отсутствует поле 'json'"
    assert body["json"]["username"] == "tester", "Поле 'username' не совпадает"
    assert body["json"]["age"] == 25, "Поле 'age' не совпадает"


# ─────────────────────────────────────────────
# Тест 4: POST-запрос с form-data
# ─────────────────────────────────────────────
def test_post_form_data():
    """POST /post с form-data: сервер отражает данные в 'form'."""
    form_data = {"field1": "value1", "field2": "value2"}
    response = requests.post(f"{BASE_URL}/post", data=form_data)

    assert response.status_code == 200

    body = response.json()
    assert "form" in body, "В ответе отсутствует поле 'form'"
    assert body["form"]["field1"] == "value1", "Поле 'field1' не совпадает"
    assert body["form"]["field2"] == "value2", "Поле 'field2' не совпадает"


# ─────────────────────────────────────────────
# Тест 5: GET-запрос — проверка заголовков ответа
# ─────────────────────────────────────────────
def test_get_response_headers():
    """GET /get: ответ содержит Content-Type application/json."""
    response = requests.get(f"{BASE_URL}/get")

    assert response.status_code == 200
    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, (
        f"Ожидался Content-Type application/json, получен: {content_type}"
    )


# ─────────────────────────────────────────────
# Тест 6: POST-запрос с кастомным заголовком
# ─────────────────────────────────────────────
def test_post_custom_header():
    """POST /post с кастомным заголовком: сервер отражает его в 'headers'."""
    headers = {"X-Custom-Header": "hello-postman"}
    response = requests.post(f"{BASE_URL}/post", headers=headers)

    assert response.status_code == 200

    body = response.json()
    assert "headers" in body, "В ответе отсутствует поле 'headers'"
    # PostmanEcho возвращает заголовки в нижнем регистре
    assert body["headers"].get("x-custom-header") == "hello-postman", (
        "Кастомный заголовок не отражён в ответе"
    )


# ─────────────────────────────────────────────
# Тест 7: POST-запрос с query-параметрами
# ─────────────────────────────────────────────
def test_post_with_query_params():
    """POST /post с query-параметрами: сервер отражает их в 'args'."""
    params = {"action": "create", "version": "2"}
    response = requests.post(f"{BASE_URL}/post", params=params)

    assert response.status_code == 200

    body = response.json()
    assert body["args"]["action"] == "create", "Параметр 'action' не совпадает"
    assert body["args"]["version"] == "2", "Параметр 'version' не совпадает"


# ─────────────────────────────────────────────
# Тест 8: GET-запрос — структура ответа
# ─────────────────────────────────────────────
def test_get_response_structure():
    """GET /get: ответ содержит обязательные поля args, headers, url."""
    response = requests.get(f"{BASE_URL}/get")

    assert response.status_code == 200

    body = response.json()
    for field in ("args", "headers", "url"):
        assert field in body, f"В ответе отсутствует обязательное поле '{field}'"

    # url должен содержать корректный адрес
    assert "postman-echo.com/get" in body["url"], (
        f"Неожиданный url в ответе: {body['url']}"
    )
