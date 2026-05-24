from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="session", autouse=True)
def precondition4():
    print("launching amazon")
    yield
    print("closing amazon")



@pytest.fixture(scope="function")
def precondition2():
    print("amazon2")
    yield
    print("amazon2 closing")

@pytest.fixture(scope="function")
def launchAmazon(page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(3000)


# @pytest.fixture(scope="function")
# def page():
#      with sync_playwright() as p:
#         browser = p.chromium.launch()
#         context = browser.new_context()
#         page = context.new_page()