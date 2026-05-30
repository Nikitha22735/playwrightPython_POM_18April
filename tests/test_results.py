from playwright.sync_api import expect
import pytest
from pages.homePage import homePage
from pages.resultPage import resultPage


@pytest.mark.results
def test_search_and_filter_iphone(page, launchAmazon):
    """Test to search for iPhone and filter by Apple brand"""
    homePageObj = homePage(page)
    resultPageObj = resultPage(page)
    
    # Search for iPhone
    homePageObj.search_product("iphone")
    homePageObj.click_search_button()
    page.wait_for_timeout(2000)
    
    # Filter by Apple brand
    resultPageObj.select_apple_brand()
    page.wait_for_timeout(2000)
    
    # Click on additional filter option
    resultPageObj.click_filter_option()
    page.wait_for_timeout(2000)
    
    # Validate search results are displayed
    resultPageObj.validate_search_results_visible()
