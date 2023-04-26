# Fixtures - Pytest-playwright

Fixtures — это функции, выполняемые pytest до или после тестовых функций. Это способ выполнения действий для теста, но
не внутри тестовой функции. Основная задача фикстуры - создание соответствующего тестового окружения.

Чтобы сообщить pytest, что данная функция является фикстурой, необходимо импортировать библиотеку pytest и использовать
декоратор@pytest.fixture для функции которая будет выступать фикстурой. Для того чтобы задействовать фикстуру для теста,
необходимо передать имя данной фикстуры в список параметров тестовой функции.

```python
import pytest


@pytest.fixture
def my_fixture():
    pass


def test_add_todo(my_fixture):
    pass
```

Вы можете реализовать собственную фикстуру на основе уже имеющегося кода.

```python
@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()
```

Но ребята из команды разработки Playwright подготовили готовое решение и этого вопроса.

## pytest-playwright

Аддон pytest-playwright реализует несколько фикстур. Наиболее широко используемой из которых является фикстура - "page".
Фикстура page предоставляет новую веб-страницу для запуска теста и функции для работы с ней.

Перепишем записанный код для запуска его с помощью pytest и фикстур из аддона pytest-playwright

```python
def test_add_todo(page):
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
```

Код стал намного чище и лаконичнее 😎

По умолчанию pytest-playwright делает браузер headless(безголовым). Если вы хотите выполнить в режиме headed, передайте
параметр, как показано ниже.

pytest --headed
