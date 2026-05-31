import os

from playwright.sync_api import expect
class homePage:

    def __init__(self,page):
         self.accountsNdList = page.locator(os.getenv("accndlist"))
         self.searchBox = page.locator("input#twotabsearchtextbox")
         self.goButton = page.get_by_role("button", name="Go", exact=True)


    def clickOnAccountsNdList(self):
          self.accountsNdList.click()

    def validateTheVisibilityOfSearchBox(self):
         expect(self.searchBox).to_be_visible()

    def search_product(self, product_name):
         """Click on search box and fill product name"""
         self.searchBox.click()
         self.searchBox.fill(product_name)

    def click_search_button(self):
         """Click the Go button to search"""
         self.goButton.click()