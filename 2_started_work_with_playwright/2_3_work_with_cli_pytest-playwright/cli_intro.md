CLI - Интерфейс командной строки (англ. Command Line Interface, CLI). Передавая различные параметры в командной строке,
вы можете менять поведение в работе playwright.

Рассмотрим подробнее команды для управления playwright с помощью cli.

`--headed` - playwright по умолчанию запускает браузеры в безголовом(headless) режиме. При использовании данного
аргумента, запуск теста произойдет в режиме headed.

`--browser` - запускать тесты в другом браузере chromium, firefox или webkit. Может быть указано несколько раз (по
умолчанию: chromium).

```shell
pytest --headed --browser webkit --browser firefox
```

`--browser-channel` - возможно вам потребуется запускать тесты в браузерах Chrome и Edge, установленных на вашем
компьютере.

```shell
pytest --browser-channel=msedge --headed
```

`--slowmo` - используется для замедления выполнения теста на указанное количество миллисекунд.

```shell
pytest pytest --slowmo 1000
```

`--device` - можно использовать для имитации поведения браузера для определенного устройства.

В качества параметра передайте поддерживаемый девайс.
Список поддерживаемых девайсов вы сможете посмотреть
по [ссылке](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json)

```shell
pytest --device="iPhone 13 Mini"
```

`--output` Каталог для артефактов, создаваемых тестами (по умолчанию: test-results).

`--tracing` Записывать ли трассировку для каждого теста. on, off или retain-on-failure (по умолчанию: off).

`--video` Записывать ли видео для каждого теста. on, off или retain-on-failure (по умолчанию: off).

`--screenshot` Должен ли автоматически делаться снимок экрана после каждого теста. on, off или only-on-failure (по
умолчанию: off).

Кроме CLI, на выполнение теста можно влиять с помощью декораторов pytest.

## Пропустить тест браузером

```python
import pytest

@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...
```

## Запуск в определенном браузере

```python
import pytest


@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...
```

С помощью какой команды CLI можно запустить тесты в браузере Chrome

> --browser-channel=chrome
