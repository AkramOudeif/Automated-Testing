import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import os

downloaded_path = "/root/Downloads/"

if os.path.exists(downloaded_path):
    for filename in os.listdir(downloaded_path):
        file_path = os.path.join(downloaded_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def test_file_download(driver):
    # Write your code below this line
    pass