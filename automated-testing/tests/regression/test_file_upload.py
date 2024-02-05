import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

parent_directory = "/usercode/automated-testing/files/"
uploaded_path = "/usercode/automated-testing/server/public/uploads/"

@pytest.mark.parametrize("test_case, file_name, expected_message", [
    ("Uploading valid file", "valid_file.txt", "File Uploaded!"),
    ("Uploading invalid file", "invalid_file.py", "Only text files are allowed for upload"),
    ("Uploading large file", "large_file.txt", "File size should not exceed 1MB"),
    ("Clicking upload button without choosing any file", "", "Please select a file to upload")
])
def test_file_upload(driver, test_case, file_name, expected_message):
    # Write your code below this line
    pass