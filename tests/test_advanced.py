from playwright.sync_api import sync_playwright, expect


def browserConfigs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width":1000,"height":600})
        page  = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(7000)


def mobileEmulation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        print(p.devices["iPhone XR"])
        context = browser.new_context(**p.devices["iPhone XR"])
        # context = browser.new_context('user_agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Mobile/15E148 Safari/604.1',viewport={"width":1000,"height":600})
        page  = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(7000)


def test_geoGraphyMocking():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(geolocation={"latitude":36.7783, "longitude": -119.4179} , permissions=["geolocation"])
        # context = browser.new_context('user_agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Mobile/15E148 Safari/604.1',viewport={"width":1000,"height":600})
        page  = context.new_page()
        page.goto("https://browserleaks.com/geo")
        expect(page).to_have_title("testing")
        page.wait_for_timeout(7000)

# geoGraphyMocking()

def offlineMode():
      with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        # context = browser.new_context('user_agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Mobile/15E148 Safari/604.1',viewport={"width":1000,"height":600})
        page  = context.new_page()
        context.set_offline(True)
        page.goto("https://testautomationpractice.blogspot.com/")
        
        page.wait_for_timeout(7000)


# =================

#pip install pillow

from PIL import Image, ImageChops
def visualRegression(page):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     # context = browser.new_context('user_agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.4 Mobile/15E148 Safari/604.1',viewport={"width":1000,"height":600})
    #     page  = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(3000)
        page.screenshot(full_page=True, path="actualSS.png")
        # expect().to_have_screenshot("FigmaSS.png", full_page=True)

        pixel1 = Image.open("FigmaSS.png")
        pixel2 = Image.open("actualSS.png")
        diff = ImageChops.difference(pixel1,pixel2)

        # print(diff.getbbox())
        assert diff.getbbox() is None
       


def frames():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.guru99.com/test/guru99home/")
        page.frame_locator("//iframe[contains(@src,'youtube')]").locator('//button[@aria-label="Play video"]').click()
        page.wait_for_timeout(5000)

frames()







