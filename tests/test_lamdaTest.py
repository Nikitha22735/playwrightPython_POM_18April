import json

from playwright.sync_api import sync_playwright, expect
import urllib
capabilities = {
    'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': 'Windows 10',
        'build': 'Playwright Python Build',
        'name': 'Playwright Python Test',
        'user': 'nikithathripuram',
        'accessKey': 'LT_mdwSuSZ2SrRa7ZX9fI8nFWpCeXDK0COkVnrNl5pQGL8Wcuo',
        'network': True,
        'video': True,
        'console': True
    }
}
def test_lamndaTest():
     with sync_playwright() as p:
        browser = p.chromium.connect('wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(
        json.dumps(capabilities)))

        context = browser.new_context(geolocation={"latitude":36.7783, "longitude": -119.4179} , permissions=["geolocation"])
        # context = browser.new_context('user_agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Mobile/15E148 Safari/604.1',viewport={"width":1000,"height":600})
        page  = context.new_page()
        page.goto("https://browserleaks.com/geo")
        page.wait_for_timeout(7000)