import time


def test_radio_buttons(page):
    page.goto('https://checks-radios.antonzimaiev.repl.co/', wait_until='domcontentloaded')
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()
    time.sleep(4)
