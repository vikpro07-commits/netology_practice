# PostmanEcho API Tests

Автотесты для сервиса [PostmanEcho](https://postman-echo.com) — учебного REST API для практики.

## Стек

| Инструмент | Версия |
|------------|--------|
| Python | 3.8+ |
| pytest | 8.x |
| requests | 2.x |

## Структура проекта

```
.
├── test_echo.py          # Автотесты (8 штук)
├── requirements.txt      # Зависимости
├── README.md
└── .github/
    └── workflows/
        └── ci.yml        # GitHub Actions CI
```

## Запуск локально

```bash
# 1. Установить зависимости
pip install -r requirements.txt

# 2. Запустить тесты
pytest test_echo.py -v
```

## Тесты

| # | Название | Метод | Что проверяет |
|---|----------|-------|---------------|
| 1 | `test_get_no_params` | GET | Статус 200, пустой `args` |
| 2 | `test_get_with_query_params` | GET | Отражение query-параметров в `args` |
| 3 | `test_post_json_body` | POST | Отражение JSON-тела в `json` |
| 4 | `test_post_form_data` | POST | Отражение form-data в `form` |
| 5 | `test_get_response_headers` | GET | Content-Type в заголовках ответа |
| 6 | `test_post_custom_header` | POST | Отражение кастомного заголовка |
| 7 | `test_post_with_query_params` | POST | Query-параметры в POST-запросе |
| 8 | `test_get_response_structure` | GET | Обязательные поля в теле ответа |

## CI/CD

Тесты автоматически запускаются при каждом `push` и `pull_request` через GitHub Actions.
# netology_practice
