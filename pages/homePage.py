import os

import allure
from playwright.sync_api import expect
class homePage:

    def __init__(self,page):
         self.accountsNdList = page.locator("//span[contains(text(),'Account & List')]")
         self.searchBox = page.locator("input#twotabsearchtextbox")
         self.goButton = page.get_by_role("button", name="Go", exact=True)

    @allure.step("Click on Accounts and List")
    def clickOnAccountsNdList(self):
          self.accountsNdList.click()

    @allure.step("Validate the visibility of search box")
    def validateTheVisibilityOfSearchBox(self):
         expect(self.searchBox).to_be_visible()
 
    @allure.step("Search for a product")
    def search_product(self, product_name):
         """Click on search box and fill product name"""
         self.searchBox.click()
         self.searchBox.fill(product_name)
         
    @allure.step("Click on search button")
    def click_search_button(self):
         """Click the Go button to search"""
         self.goButton.click()