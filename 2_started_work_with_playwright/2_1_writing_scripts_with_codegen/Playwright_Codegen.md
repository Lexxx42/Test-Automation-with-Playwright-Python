# Playwright Codegen

Одна из мощных функций, которыми обладает Playwright, заключается в том, что он может генерировать код автотеста,
записывая ваши действия в браузере.

Вы можете буквально открыть любой веб-сайт, начать его просматривать и по мере взаимодействия с ним, ваши тесты будут
буквально написаны у вас на глазах.

В отличие от Selenium IDE, Playwright дает возможность генерировать тесты «из коробки». Т.е у вас нет необходимости
дополнительно устанавливать расширения для браузера или другой дополнительный софт.

Итак, вместо того, чтобы писать весь код с нуля, мы можем сгенерировать код с помощью наших действий в браузере, а затем
изменить код в соответствии с нашими потребностями.

Давайте запишем типичный сценарий автоматизации приложения отслеживания задач (ToDo):

+ Открыть веб сайт приложения
+ Записать задачу "Создать первый сценарий playwright"
+ Отметить задачу выполненной

Для запуска codegen откройте терминал (Pycharm, VScode), введите приведенную ниже команду и нажмите Enter.

```
playwright codegen https://playwright-todomvc.antonzimaiev.repl.co/#/
```

Эта команда откроет два окна:

+ Браузер Chromium
+ Playwright Inspector

Далее вы можете выполнить необходимое действие по сценарию в браузере, а codegen запишет и сгенерирует код для
выполняемого вами действия.

В Playwright Inspector каждое ваше взаимодействие с веб-сайтом будет отображаться как новая строка кода.

В итоге у вас должен получиться вот такой пример кода

```python
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
```

Скопируйте этот код, вставьте его в файл main.py и запустите его. Он должен выполняться по тем же шагам, которые вы
выполняли в браузере.
