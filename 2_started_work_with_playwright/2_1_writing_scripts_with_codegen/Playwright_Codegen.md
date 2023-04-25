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

## Давайте попробуем разобрать основную часть сгенерированного кода.

Для того чтобы получить доступ ко всем функциям, методам и классам playwright, необходимо импортировать его в наш код,
что делает приведенная строка кода ниже

```python
from playwright.sync_api import Playwright, sync_playwright, expect
```

Следующие три строки отвечают за запуск браузера и создание в нем контекста

```python
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
```

запуск браузера chromium

```python
playwright.chromium.launch
```

`headless=False` - дает команду, чтобы браузер chromium отображался и был видимым при запуске кода. Ели вы установите
`True`, то браузер не будет отображаться. Но при этом все записанные в коде действия сценария будут выполнены.

`new_context()` - создает изолированный сеанс браузера.

`new_page()`  - открывает новую страницу(tab) в браузере

После того как браузер открыт и подготовлен, можно начать с ним работать.

```python
page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
```

Метод `page.goto()` необходим, чтобы открыть веб-сайт.

С помощью метода `get_by_placeholder("What needs to be done?")` playwright находит в DOM дереве веб-элемент c атрибутом
тега `placeholder` и значением атрибута `What needs to be done?`

Далее мы начинаем взаимодействовать с этим веб-элементом

`click()`- эмулирует клик левой кнопкой мышки по веб-элементу

`fill()` - этот метод вводит значения, переданные ему в качестве аргумента в веб-элемент.
В нашем случае это текст - "Создать первый сценарий playwright"

`press("Enter")` - эмулирует нажатие клавиши Enter на клавиатуре.
