import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("test_case, username, password, expected_message", [
    ("Valid credentials test", "admin", "admin", "You logged into a secure area!"),
    ("Invalid credentials test", "admin1", "admin1", "Invalid username or password!"),
    ("Empty credentials test", "", "", "Username or password field is empty!")
])
def test_form_authentication(driver, test_case, username, password, expected_message):
    # Write your code below this line
    pass