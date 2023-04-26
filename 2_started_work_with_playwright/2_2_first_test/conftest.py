import pytest
from playwright.sync_api import Playwright, BrowserType


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        "viewport": {
            "width": 1920,
            "height": 1080
        },
        "is_full_screen": True
    }


@pytest.fixture(scope="session")
def browser_type(playwright: Playwright):
    return playwright.chromium


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": False
    }


@pytest.fixture(scope="session")
def context(browser_type: BrowserType, browser_type_launch_args, browser_context_args):
    context = browser_type.launch_persistent_context("./foobar", **{
        **browser_type_launch_args,
        **browser_context_args,
        "locale": "en-GB",
    })
    yield context
    context.close()
