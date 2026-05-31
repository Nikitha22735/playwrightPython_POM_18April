from playwright.sync_api import sync_playwright
import pytest

from pages import homePage, loginPage


@pytest.fixture(scope="session")
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

@pytest.fixture(scope="function")
def homePageObj(page):
    homePageObj = homePage(page)
    return homePageObj

@pytest.fixture(scope="function")
def loginPageObj(page):
    loginPageObj = loginPage(page)
    return loginPageObj


# @pytest.fixture()
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context(viewport={"width": 1280, "height": 720})
#         page = context.new_page()
#         yield page
#         browser.close()