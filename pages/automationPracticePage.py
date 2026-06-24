import allure
from playwright.sync_api import expect


class AutomationPracticePage:
    """Page Object Model for Test Automation Practice Website"""

    def __init__(self, page):
        """Initialize page elements using locators"""
        self.page = page
        self.name_input = page.locator("input#name")
        self.email_input = page.locator("input#email")
        self.phone_input = page.locator("input#phone")
        self.address_input = page.locator("textarea")
        self.male_radio = page.locator("input[value='male']")
        self.female_radio = page.locator("input[value='female']")
        self.submit_button = page.locator("button[type='submit']")

    @allure.step("Navigate to Automation Practice Website")
    def navigate_to_website(self):
        """Navigate to the test automation practice website"""
        self.page.goto("https://testautomationpractice.blogspot.com/")
        self.page.wait_for_load_state("networkidle")

    @allure.step("Verify Name Input Field is Visible")
    def verify_name_field_is_visible(self):
        """Check if the name input field is visible on the page"""
        expect(self.name_input).to_be_visible()
        return True

    @allure.step("Verify Name Input Field Properties")
    def verify_name_field_properties(self):
        """Verify name field has correct attributes"""
        expect(self.name_input).to_have_attribute("type", "text")
        expect(self.name_input).to_have_attribute("maxlength", "15")
        expect(self.name_input).to_have_attribute("placeholder", "Enter Name")
        expect(self.name_input).to_have_attribute("required", "")
        return True

    @allure.step("Verify Name Input Field is Enabled")
    def verify_name_field_is_enabled(self):
        """Check if the name input field is enabled"""
        expect(self.name_input).to_be_enabled()
        return True

    @allure.step("Verify Name Input Field has Correct ID")
    def verify_name_field_id(self):
        """Verify the name field has id='name'"""
        expect(self.name_input).to_have_id("name")
        return True

    @allure.step("Fill Name Field with Value: {value}")
    def fill_name_field(self, value):
        """Fill the name input field with provided value"""
        self.name_input.fill(value)

    @allure.step("Get Name Field Value")
    def get_name_field_value(self):
        """Get the current value of the name field"""
        return self.name_input.input_value()

    @allure.step("Clear Name Field")
    def clear_name_field(self):
        """Clear the name input field"""
        self.name_input.clear()

    @allure.step("Click on Name Field")
    def click_name_field(self):
        """Click on the name input field"""
        self.name_input.click()
