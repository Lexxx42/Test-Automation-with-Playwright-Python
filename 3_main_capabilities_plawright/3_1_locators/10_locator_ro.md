# Локатор locator.or_

Создает локатор, который соответствует любому из двух локаторов.

Локатор locator.or_ используется для поиска элемента, который соответствует хотя бы одному из заданных селекторов.
Например:

```python
from playwright.sync_api import Playwright, sync_playwright


def test_or(page):
    selector = page.locator("input").or_(page.locator("text"))
    selector.fill("Hello Stepik")
```

В данном примере мы создаем локатор, который ищет первый элемент input или textarea на странице. Если элемент не найден
с помощью первого селектора, локатор будет использовать второй селектор для поиска элемента.

## Локатор locator.and_

Локатор locator.and_ используется для поиска элемента, который соответствует всем заданным селекторам.

Например:

```python
from playwright.sync_api import Playwright, sync_playwright


def test_locator_and(page):
    selector = page.get_by_role("button").and_(page.get_by_text("Stepik"))
```

В данном примере мы создаем локатор, который является кнопкой и имеет текст "Stepik"
