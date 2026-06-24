"""
Test cases for Automation Practice Website - Name Input Field
Tests to verify the visibility and functionality of the name input field
"""

import allure
import pytest
from playwright.sync_api import expect
from pages.automationPracticePage import AutomationPracticePage


@pytest.fixture(scope="function")
def automationPracticePage(page):
    """Fixture to initialize AutomationPracticePage"""
    automation_page = AutomationPracticePage(page)
    automation_page.navigate_to_website()
    return automation_page


# ===================== Name Field Visibility Tests =====================

@pytest.mark.automationPractice
@pytest.mark.smoke
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Visibility")
@allure.title("Verify Name Input Field is Visible")
def test_name_field_is_visible(automationPracticePage):
    """Test to verify that the name input field is visible on the page"""
    assert automationPracticePage.verify_name_field_is_visible()


@pytest.mark.automationPractice
@pytest.mark.smoke
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Visibility")
@allure.title("Verify Name Input Field has Correct ID")
def test_name_field_has_correct_id(automationPracticePage):
    """Test to verify that the name input field has id='name'"""
    assert automationPracticePage.verify_name_field_id()


@pytest.mark.automationPractice
@pytest.mark.smoke
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Visibility")
@allure.title("Verify Name Input Field Properties")
def test_name_field_properties(automationPracticePage):
    """Test to verify name field attributes (type, maxlength, placeholder, required)"""
    assert automationPracticePage.verify_name_field_properties()


@pytest.mark.automationPractice
@pytest.mark.smoke
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Visibility")
@allure.title("Verify Name Input Field is Enabled")
def test_name_field_is_enabled(automationPracticePage):
    """Test to verify that the name input field is enabled and can receive input"""
    assert automationPracticePage.verify_name_field_is_enabled()


# ===================== Name Field Functionality Tests =====================

@pytest.mark.automationPractice
@pytest.mark.regression
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Functionality")
@allure.title("Test Filling Name Field with Valid Input")
def test_fill_name_field_with_valid_input(automationPracticePage):
    """Test to fill the name field with valid text and verify the value is set"""
    test_name = "John Doe"
    automationPracticePage.fill_name_field(test_name)
    actual_value = automationPracticePage.get_name_field_value()
    assert actual_value == test_name, f"Expected '{test_name}', but got '{actual_value}'"


@pytest.mark.automationPractice
@pytest.mark.regression
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Functionality")
@allure.title("Test Name Field Max Length Validation")
def test_name_field_max_length(automationPracticePage):
    """Test to verify that the name field enforces maxlength='15'"""
    long_name = "ThisIsAVeryLongName"  # 19 characters
    automationPracticePage.fill_name_field(long_name)
    actual_value = automationPracticePage.get_name_field_value()
    assert len(actual_value) <= 15, f"Field accepted {len(actual_value)} characters, max should be 15"


@pytest.mark.automationPractice
@pytest.mark.regression
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Functionality")
@allure.title("Test Clearing Name Field")
def test_clear_name_field(automationPracticePage):
    """Test to verify that the name field can be cleared"""
    automationPracticePage.fill_name_field("Test Name")
    automationPracticePage.clear_name_field()
    actual_value = automationPracticePage.get_name_field_value()
    assert actual_value == "", f"Field should be empty, but contains: '{actual_value}'"


@pytest.mark.automationPractice
@pytest.mark.regression
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Functionality")
@allure.title("Test Clicking on Name Field")
def test_click_name_field(automationPracticePage):
    """Test to verify that the name field can be focused by clicking"""
    automationPracticePage.click_name_field()
    automationPracticePage.fill_name_field("Clicked")
    actual_value = automationPracticePage.get_name_field_value()
    assert actual_value == "Clicked", "Field should have received the input after clicking"


# ===================== Name Field Edge Cases Tests =====================

@pytest.mark.automationPractice
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Edge Cases")
@allure.title("Test Name Field with Special Characters")
def test_name_field_with_special_characters(automationPracticePage):
    """Test to fill the name field with special characters"""
    special_name = "John@#$"
    automationPracticePage.fill_name_field(special_name)
    actual_value = automationPracticePage.get_name_field_value()
    assert actual_value == special_name, f"Expected '{special_name}', but got '{actual_value}'"


@pytest.mark.automationPractice
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Edge Cases")
@allure.title("Test Name Field with Numbers")
def test_name_field_with_numbers(automationPracticePage):
    """Test to fill the name field with numeric values"""
    numeric_name = "12345"
    automationPracticePage.fill_name_field(numeric_name)
    actual_value = automationPracticePage.get_name_field_value()
    assert actual_value == numeric_name, f"Expected '{numeric_name}', but got '{actual_value}'"


@pytest.mark.automationPractice
@allure.feature("Automation Practice Website")
@allure.story("Name Input Field Edge Cases")
@allure.title("Test Name Field with Spaces")
def test_name_field_with_spaces(automationPracticePage):
    """Test to fill the name field with spaces"""
    name_with_spaces = "John  Doe"
    automationPracticePage.fill_name_field(name_with_spaces)
    actual_value = automationPracticePage.get_name_field_value()
    assert actual_value == name_with_spaces, f"Expected '{name_with_spaces}', but got '{actual_value}'"
