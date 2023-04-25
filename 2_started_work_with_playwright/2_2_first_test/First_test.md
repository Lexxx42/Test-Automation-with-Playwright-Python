# Первый тест

У нас есть записанный скрипт Playwright, и мы понимаем некоторые основные функции Playwright. Однако, для создания
реальных E2E тестов обычно используется специализированный фреймворк/тестовый раннер.

Pytest - наиболее популярный фреймворк с открытым исходным кодом. С помощью pytest можно запускать определенные тесты,
пропускать их, хранить тестовые примеры в структурированном виде.

Pytest автоматически сканирует ваш код на наличие тестовых модулей, файлов, следующих соглашению об именовании:

+ Пакет/директория: `"test*"`
+ Файлы `test_*.py` или `*_test.py`
+ Классы `Test*`
+ функций `test_*()`

Давайте перепишем ранее записанный скрипт так, чтобы он мог запускаться с помощью pytest.

Первое, что нужно сделать - переименовать файл, чтобы он следовал соглашению по именованию в pytest. Назовем наш файл
`test_todo.py`.

Вторым шагом переименуем название функции в `test_add_todo`.

Поскольку запуском тестовых функций будет заниматься pytest, в коде уже нет необходимости явно вызывать функцию. Удаляем
код отвечающий за это.

```
with sync_playwright() as playwright:
    run(playwright)
```

У нас должен получиться такой код.

```python
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    context.close()
    browser.close()
```

Вы можете запустить тесты, написав в терминале pytest и нажав Enter.

После выполнения появится отчет о количестве найденных тестов и об успешности их прохождения.

Каждый раз запускать тест с помощью консоли - не самый удобный вариант. У Pycharm есть решение данной проблемы. Нажмите
Ctrl-Shift-A(для Windows) или Cmd-Shift-A(для MacOS). В открывшемся окне введите pytest. Откроется меню настроек Python
Integrated Tools с выбором тест-раннера. Выберите в качестве тест-раннера по умолчанию pytest.
