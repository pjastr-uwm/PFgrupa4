from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_finding_elements(driver):
    driver.get("https://the-internet.herokuapp.com/")
    # Finding element by tag name
    heading = driver.find_element(By.TAG_NAME, "h1")
    assert heading.text == "Welcome to the-internet"

    # Finding element by link text
    form_auth = driver.find_element(By.LINK_TEXT, "Form Authentication")
    assert "Form Authentication" in form_auth.text

    # Finding element by partial link text
    checkboxes = driver.find_element(By.PARTIAL_LINK_TEXT, "Checkboxes")
    assert "Checkboxes" in checkboxes.text

    # Finding elements by CSS selector
    links = driver.find_elements(By.CSS_SELECTOR, "li a")
    assert len(links) > 10  # Making sure we found multiple links

    # Finding element by XPath
    footer = driver.find_element(By.XPATH, "//div[@id='page-footer']")
    assert "Powered by" in footer.text

def test_checkboxes(driver):
    # Open the page with checkboxes
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Find checkboxes
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    # Check initial state (first unchecked, second checked)
    assert not checkboxes[0].is_selected()
    assert checkboxes[1].is_selected()

    # Check the first checkbox
    checkboxes[0].click()
    assert checkboxes[0].is_selected()

    # Uncheck the second checkbox
    checkboxes[1].click()
    assert not checkboxes[1].is_selected()


def test_dropdown(driver):
    # Open the page with dropdown
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # Find dropdown
    from selenium.webdriver.support.select import Select
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    # Select option by visible text
    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1"

    # Select option by value
    dropdown.select_by_value("2")
    assert dropdown.first_selected_option.text == "Option 2"