from playwright.sync_api import sync_playwright,expect
import pytest


@pytest.mark.login
def test_positiveLogin(page,launchAmazon):
    page.locator("//span[contains(text(),'Account & List')]").click()
    page.locator("#ap_email_login").fill("trainingplaywright@gmail.com")
    page.locator('//input[@type="submit"]').click()
    page.locator("#ap_password").fill("Welcome@04")
    page.locator('//input[@type="submit"]').click()
    expect(page.locator("input#twotabsearchtextbox")).to_be_visible()

