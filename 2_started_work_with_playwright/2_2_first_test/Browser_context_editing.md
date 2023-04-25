# Редактирование контекста браузера

Если для выполнения теста вам требуются особые параметры контекста браузера(геолокация, размер браузера и тд)вы можете
на это повлиять. Вы можете создать фикстуру для редактирования контекста браузера.

Необходимо добавить в ваш проект в файл conftest.py, который служит для конфигурирования pytest. Фикстура
`browser_context_args` возвращает словарь со значениями и устанавливает эти значения в класс `browser_context`.

Рассмотрим пример использования фикстуры для изменения размера браузера

```python
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
```

Или установить cookies. Имена и параметры нужно передавать как массив словарей:

```python
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    response = authenticate(user)
    return {
        **browser_context_args
        "storage_state": {
            "cookies": [
                {
                    "name": "token",
                    "value": "sd4fFfv!x_cfc",
                },
            ]
        },
    }
```

Вы можете ознакомиться в [документации](https://playwright.dev/python/docs/api/class-browsercontext) со всеми
параметрами контекста на которые вы можете влиять.
