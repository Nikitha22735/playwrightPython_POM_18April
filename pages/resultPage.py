from playwright.sync_api import expect


class resultPage:
    def __init__(self, page):
        self.page = page
        self.appleOption = page.get_by_text("Apple")
        self.filterOption = page.locator("#a-autoid-1-announce")

    def select_apple_brand(self):
        """Click on Apple brand filter (nth(1))"""
        self.appleOption.nth(1).click()

    def click_filter_option(self):
        """Click on the filter option"""
        self.filterOption.click()

    def validate_search_results_visible(self):
        """Validate that search results are visible"""
        expect(self.appleOption).to_be_visible()
